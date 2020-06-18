
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from .validators import validate_file_extension_coverImage

class coverImage(models.Model):
    cover = models.ImageField(upload_to='Cover/',verbose_name="عکس پشت تیتر",null=True)

    def __str__(self):
        return "عکس پشت تیتر"

    class Meta:
        verbose_name = "عکس پشت تیتر"
        verbose_name_plural = "عکس پشت تیتر"
    
class category(models.Model):
    name = models.CharField(max_length = 64, verbose_name = "نام به انگلیسی")
    farsiName = models.CharField(max_length = 64, verbose_name = "نام به فارسی")
    slug = models.SlugField(max_length=140, unique=True, null =True, editable= False)

    def __str__(self):
        return self.farsiName
    class Meta:
        verbose_name = "بخش"
        verbose_name_plural = "بخش"
    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while category.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

class article(models.Model):
    title = models.CharField(max_length = 64, null = True, verbose_name="تیتر به انگلیسی")
    slug = models.SlugField(max_length=140, unique=True, null =True, editable= False)
    farsiTitle = models.CharField(max_length = 64, null = True, verbose_name="تیتر به فارسی")
    shortDescription = models.TextField(max_length = 400, null = True, verbose_name="خلاصه به انگلیسی")
    farsiShortDescription = models.TextField(max_length = 400, null = True, verbose_name="خلاصه به فارسی")
    articleImage = models.ImageField( upload_to='news/', verbose_name="عکس کاور", validators = [validate_file_extension_coverImage])
    description = RichTextUploadingField(config_name='awesome_ckeditor', null = True, verbose_name="توضیحات به انگلیسی")
    farsiDescription = RichTextUploadingField(config_name='awesome_ckeditor', null = True, verbose_name="توضیحات به فارسی")
    category = models.ManyToManyField(category, verbose_name="Categories") #models.ForeignKey(category, on_delete = models.CASCADE, null = True)
    date = models.CharField(max_length = 64, null = True, verbose_name="تاریخ میلادی")
    Farsidate = models.CharField(max_length = 64, null = True, verbose_name="تاریخ شمسی")
    authorName = models.CharField(max_length = 64, null = True, verbose_name="نام نویسنده به انگلیسی")
    farsiAuthoName = models.CharField(max_length = 64, null = True, verbose_name="نام نویسنده به فارسی")
    def __str__(self):
        return self.farsiTitle
    
    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while article.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
    def get_absolute_url(self):
        return reverse("news:detail" , kwargs={"slug" : self.slug})
        #return "/posts/%s/" %(self.slug)
    class Meta:
        verbose_name_plural = "خبر"


@receiver(pre_save, sender=category, dispatch_uid='slugify1')
def generateSlugC(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = instance._get_unique_slug()

@receiver(pre_save, sender=article, dispatch_uid='slugify2')
def generateSlugA(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = instance._get_unique_slug()
