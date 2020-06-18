
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .validators import validate_file_extension_coverImage


class coverImage(models.Model):
    cover = models.ImageField(upload_to='Cover/',verbose_name="عکس پشت تیتر",null=True)
    
    def __str__(self):
        return "عکس پشت تیتر"

    class Meta:
        verbose_name = "عکس پشت تیتر"
        verbose_name_plural = "عکس پشت تیتر"
    
        
class achievement(models.Model):
    title = models.CharField(max_length = 64, null = True ,verbose_name="تیتر به انگلیسی")
    slug = models.SlugField(max_length=140, unique=True, null =True, editable= False)
    farsiTitle = models.CharField(max_length = 64, null = True, verbose_name="تیتر به فارسی")
    shortDescription = models.TextField(max_length = 400, null = True, verbose_name="خلاصه به انگلیسی")
    farsiShortDescription = models.TextField(max_length = 400, null = True,  verbose_name="خلاصه به فارسی")
    image = models.ImageField( upload_to='achievements/', verbose_name="عکس کاور", validators = [validate_file_extension_coverImage])
    description = RichTextUploadingField(config_name='awesome_ckeditor', null = True,  verbose_name="توضیحات به انگلیسی")
    farsiDescription = RichTextUploadingField(config_name='awesome_ckeditor', null = True, verbose_name="توضیحات به فارسی")

    class Meta:
        verbose_name = "دستاورد"
        verbose_name_plural = "دستاوردها"

    def __str__(self):
        return self.farsiTitle
    
    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while achievement.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

@receiver(pre_save, sender=achievement, dispatch_uid='slugify3')
def generateSlug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = instance._get_unique_slug()
