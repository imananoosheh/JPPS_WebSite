
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class coverImage(models.Model):
    cover = models.ImageField(upload_to='Cover/',verbose_name="عکس پشت تیتر",null=True)

    def __str__(self):
        return "عکس پشت تیتر"

    class Meta:
        verbose_name = "عکس پشت تیتر"
        verbose_name_plural = "عکس پشت تیتر"
        
class content(models.Model):
    title = models.CharField(max_length = 64, verbose_name="تیتر به انگلیسی")
    farsi_title = models.CharField(max_length = 64, verbose_name="تیتر به فارسی")
    description = RichTextUploadingField(config_name='awesome_ckeditor', verbose_name="توضیحات به انگلیسی")
    farsi_description = RichTextUploadingField(config_name='awesome_ckeditor', verbose_name="توضیحات به فارسی")
    def __str__(self):
        return self.farsi_title
    class Meta:
        verbose_name = "محتوی"
        verbose_name_plural ="محتوی"