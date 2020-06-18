
import os

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.db.models.signals import pre_save, pre_delete, post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.conf import settings
from .validators import validate_file_extension_video

class coverImage(models.Model):
    cover = models.ImageField(upload_to='Cover/',verbose_name="عکس پشت تیتر",null=True)
    
    def __str__(self):
        return "عکس پشت تیتر"

    class Meta:
        verbose_name = "عکس پشت تیتر"
        verbose_name_plural = "عکس پشت تیتر"
    
class sections(models.Model):
    title = models.CharField(max_length = 64, verbose_name="تیتر به انگلیسی")
    slug = models.SlugField(max_length=140, unique=True, null =True, editable= False)
    farsi_title = models.CharField(max_length = 64, verbose_name="تیتر به فارسی")
    description = RichTextUploadingField(config_name='awesome_ckeditor',  verbose_name="توضیحات به انگلیسی")
    farsi_description = RichTextUploadingField(config_name='awesome_ckeditor', verbose_name="توضیخات به فارسی")
    def __str__(self):
        return self.farsi_title
    class Meta:
        verbose_name = "بخش"    
        verbose_name_plural = "بخش"    
    
    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while sections.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

class relatedWebsites(models.Model):
    name = models.CharField(max_length = 64, null = True, verbose_name="نام")
    link = models.CharField(max_length = 256,  verbose_name="تارنما")
    logo = models.ImageField(upload_to = 'relatedWebsites/', verbose_name="لوگو")
    def __str__(self):
       return self.name
    class Meta:
        verbose_name = "وبسایت مرتبط"
        verbose_name_plural = "وبسایت های مرتبط"

@receiver(pre_save, sender=sections, dispatch_uid='slugify')
def generateSlugC(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = instance._get_unique_slug()

class landingVideo(models.Model):
    vOp = models.FileField(upload_to='MPV/',verbose_name="ویدیو", validators = [validate_file_extension_video])
    name = models.CharField(max_length = 64, verbose_name = "نام", null = True)
    vOpm = models.FileField(upload_to='MVPMobile',verbose_name = "ویدیو (.webm)")
    class Meta:
        verbose_name = "ویدیو"
        verbose_name_plural = "ویدیو"
    def __str__(self):
        return str(self.name)


@receiver(models.signals.post_delete, sender=landingVideo)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.vOp:
        if os.path.isfile(instance.vOp.path):
            if os.path.isfile(instance.vOpm.path):
                os.remove(instance.vOpm.path)
                os.remove(instance.vOp.path)

@receiver(models.signals.pre_save, sender=landingVideo)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = landingVideo.objects.get(pk=instance.pk).vOp
        old_filem = landingVideo.objects.get(pk=instance.pk).vOpm
    except landingVideo.DoesNotExist:
        return False

    new_file = instance.vOp
    new_filem = instance.vOpm
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
    if not old_filem == new_filem:
        if os.path.isfile(old_filem.path):
            os.remove(old_filem.path)
