
from django.db import models

class coverImage(models.Model):
    cover = models.ImageField(upload_to='Cover/',verbose_name="عکس پشت تیتر",null=True)
    
    def __str__(self):
        return "عکس پشت تیتر"
    
    class Meta:
        verbose_name = "عکس پشت تیتر"
        verbose_name_plural = "عکس پشت تیتر"

class workRequest(models.Model):
    Name = models.CharField(max_length = 64, verbose_name = "نام")
    familyName = models.CharField(max_length = 64, verbose_name = "نام خانوادگی")
    fatherName = models.CharField(max_length = 64, verbose_name = "نام پدر")
    idNumber = models.CharField(max_length = 32,verbose_name = "شماره کد ملی")
    bsNumber = models.CharField(max_length = 32,verbose_name="شماره شناسنامه")
    dateOfBirth = models.CharField(max_length = 16, verbose_name="تاريخ تولد")
    placeofbirth = models.CharField(max_length = 64, verbose_name = "محل صدور شناسنامه")
    married = models.CharField(max_length = 64, verbose_name = "وضعیت تاهل")
    lastGraduate = models.CharField(max_length = 64, verbose_name = "آخرین مدرک تحصیلی")
    major = models.CharField(max_length = 64, verbose_name = "رشته", blank = True)
    employment = models.CharField(max_length = 64, verbose_name = "نوع استخدام", blank = True)
    employmentDate = models.CharField(max_length = 64, verbose_name = "تاریخ استخدام", blank = True)
    organizationUnit = models.CharField(max_length = 64, verbose_name = "واحد سازمانی", blank = True)
    district = models.CharField(max_length = 24, verbose_name = "منطقه", blank = True)
    background = models.CharField(max_length = 256, verbose_name = "سوابق خدمتی", blank = True)
    englishLevel = models.CharField(max_length = 12, verbose_name = "تسلط بر زبان انگلیسی", blank = True)
    computerSkills = models.CharField(max_length = 12, verbose_name = "تسلط بر کامپیوتر", blank = True)
    smartBoardSkills = models.CharField(max_length = 12, verbose_name = "تسلط بر تخته هوشمند", blank = True)
    otherSkills = models.CharField(max_length =256, verbose_name = "مهارت های دیگر", blank = True)
    grade = models.CharField(max_length = 256, verbose_name = "علاقه مند به تدریس پایه", blank = True)
    #recomendations
    firstName = models.CharField(max_length = 64, verbose_name = "نام" , blank = True)
    firstFamilyName =  models.CharField(max_length = 64, verbose_name = "نام خانوادگی", blank = True)
    firstAddress = models.CharField(max_length = 256, verbose_name = "آدرس منزل یا محل کار با تلفن", blank = True)
    secondName = models.CharField(max_length = 64, verbose_name = "نام" , blank = True)
    secondFamilyName =  models.CharField(max_length = 64, verbose_name = "نام خانوادگی", blank = True)
    secondAddress = models.CharField(max_length = 256, verbose_name = "آدرس منزل یا محل کار با تلفن", blank = True)
    other = models.CharField(max_length = 128, verbose_name = "توضیحات", blank = True)
    class Meta:
        verbose_name ="درخواست همکاری"
        verbose_name_plural ="درخواست های همکاری"
    def __str__(self):
        return (self.Name + " " + self.familyName)