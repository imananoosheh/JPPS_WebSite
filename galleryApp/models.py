import os
import shutil
import zipfile

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.core.urlresolvers import reverse


from .validators import validate_file_extension,validate_file_extension_coverImage

GALLERY_ROOT = settings.MEDIA_ROOT + '//Galleries//'

class coverImage(models.Model):
    cover = models.ImageField(upload_to='Cover/',verbose_name="عکس پشت تیتر",null=True)
   
    def __str__(self):
        return "عکس پشت تیتر"

    class Meta:
        verbose_name = "عکس پشت تیتر"
        verbose_name_plural = "عکس پشت تیتر"
    
class galleryCategory(models.Model):
    name = models.CharField(max_length = 64, null = True, verbose_name = "نام به انگلیسی")
    farsiName = models.CharField(max_length = 64, null = True, verbose_name = "نام به فارسی")
    slug = models.SlugField(max_length=140, unique=True, null =True, editable= False)
    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while galleryCategory.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def __str__(self):
        return self.farsiName
    class Meta:
        verbose_name = "بخش"
        verbose_name_plural = "بخش"

class Gallery(models.Model):
    galleryName = models.CharField(max_length = 64, null = True, verbose_name="نام به انگلیسی")
    slug = models.SlugField(max_length=140, unique=True, null =True, editable= False)
    farsiGalleryName = models.CharField(max_length = 64, null = True,  verbose_name="نام به فارسی")
    galleryFile = models.FileField( upload_to='Galleries/',validators=[validate_file_extension],null=True , verbose_name="آرشیو")
    galleryPath = models.CharField(max_length = 256, null = True, editable=False)
    galleryFolder = models.CharField(max_length = 256, null = True, editable = False)
    pictureCount = models.IntegerField(null=True, editable= False)
    category = models.ForeignKey(galleryCategory, on_delete=models.CASCADE, null = True, verbose_name="بخش")
    shortDescription = models.TextField(max_length = 400, null = True, verbose_name="خلاصه به انگلیسی")
    farsiShortDescription = models.TextField(max_length = 400, null = True, verbose_name="خلاصه به فارسی")
    coverImage = models.ImageField( upload_to='GalleryCovers/', null = True,  verbose_name="عکس کاور", validators=[validate_file_extension_coverImage])

    def __str__(self):
        return self.galleryName
    class Meta:
        verbose_name = "گالری"
        verbose_name_plural = "گالری"

    def _get_unique_slug(self):
        slug = slugify(self.galleryName)
        unique_slug = slug
        num = 1
        while Gallery.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
    def get_absolute_url(self):
        return reverse("galleries:detail" , kwargs={"slug" : self.slug})
        #return "/posts/%s/" %(self.slug)


@receiver(pre_save, sender=Gallery, dispatch_uid='extarct')
def extractArchive(sender, instance, **kwargs):
    def _get_unique_slug2(self):
        slug = slugify(self.galleryName)
        unique_slug = slug
        num = 1
        while galleryCategory.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
    galleryFolder = _get_unique_slug2(instance)
    galleryFolder = galleryFolder.replace("-","_")
    galleryFolder = galleryFolder.replace(" ","_")
    zip_gallery = zipfile.ZipFile(instance.galleryFile, 'r')
    zip_gallery.extractall(GALLERY_ROOT +  galleryFolder)
    zip_gallery.close()
    counter = 0
    os.chdir(GALLERY_ROOT +  galleryFolder)
    for Pic in os.listdir(GALLERY_ROOT +  galleryFolder):
        os.rename(Pic, str(counter) + ".jpg" )
        counter += 1
    instance.pictureCount = counter
    
    instance.galleryPath = GALLERY_ROOT +  galleryFolder 
    instance.galleryFolder = galleryFolder
    os.chdir(settings.BASE_DIR)


@receiver(pre_delete, sender=Gallery, dispatch_uid='clean')
def cleanUp(sender, instance, **kwargs):
    try:
        shutil.rmtree(instance.galleryPath)
        os.remove(instance.galleryFile.path)
    except:
        os.remove(instance.galleryFile.path)

@receiver(pre_save, sender=Gallery, dispatch_uid='slugify3')
def generateSlugG(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = instance._get_unique_slug()

@receiver(pre_save, sender=galleryCategory, dispatch_uid='slugify4')
def generateSlugC(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = instance._get_unique_slug()
