# -*- coding: utf-8 -*-
from django.db import models
from .validators import validate_file_extension_avatarImage

class coverImage(models.Model):
    cover = models.ImageField(upload_to='Cover/',verbose_name="عکس پشت تیتر",null=True)

    def __str__(self):
        return "عکس پشت تیتر"

    class Meta:
        verbose_name = "عکس پشت تیتر"
        verbose_name_plural = "عکس پشت تیتر"
    

class category(models.Model):
    
    name = models.CharField(max_length = 64, verbose_name="نام به انگلیسی")
    farsiName = models.CharField(max_length = 64, verbose_name="نام به فارسی")

    def __str__(self):
        return self.farsiName

    class Meta:
        verbose_name = "بخش"
        verbose_name_plural = "بخش"

class person(models.Model):
    farsiName = models.CharField(max_length = 64, verbose_name="نام به فارسی")
    name = models.CharField(max_length = 64, verbose_name="نام به انگلیسی")
    description = models.TextField(max_length=200, verbose_name="توضیحات به انگلیسی")
    farsiDescription = models.TextField(max_length=200, verbose_name="توضیحات به فارسی")
    avatar = models.ImageField(upload_to="staff/", verbose_name="عکس", validators = [validate_file_extension_avatarImage])
    Link = models.CharField(max_length = 140, verbose_name="لینک های شخصی")
    category = models.ManyToManyField(category, verbose_name="بخش")

    def __str__(self):
        return self.farsiName
    class Meta:
        verbose_name = "کارمند"
        verbose_name_plural = "کارکنان"
