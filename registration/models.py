
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from .validators import validate_file_extension_coverImage
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
        verbose_name_plural = "محتوی"
class registered(models.Model):
    #Student information
    Name = models.CharField(max_length = 64, verbose_name = "نام")
    familyName = models.CharField(max_length = 64, verbose_name = "نام خانوادگی")
    idNumber = models.CharField(max_length = 32,verbose_name = "شماره کد ملی")
    bsNumber = models.CharField(max_length = 32,verbose_name="شماره شناسنامه")
    dateOfBirth = models.CharField(max_length = 16, verbose_name="تاريخ تولد", null = True)
    placeofbirth = models.CharField(max_length = 64, verbose_name = "محل صدور شناسنامه")
    bssnumber = models.CharField(max_length = 64 , verbose_name = "شماره سريال شناسنامه")
    regfor = models.CharField(max_length = 16, verbose_name = "داوطلب ثبت نام در", null = True)
    yourreference = models.CharField(max_length = 128, verbose_name = "نحوه آشنايی با مدرسه", null = True)
    religion = models.CharField(max_length = 16, verbose_name = "دين و مذهب", null = True)
    personalPhoto = models.ImageField(upload_to = "registered/", verbose_name= "عکس پرسنلی", null = True, validators=[validate_file_extension_coverImage])
    #Current School
    currentSchool = models.CharField(max_length = 16, verbose_name = "مدرسه فعلی",null = True)
    #Grades
    average = models.CharField(verbose_name="معدل", max_length = 32, null = True)
    mathGrade = models.CharField(verbose_name="ریاضی",max_length = 32, null = True)
    disciplineGrade = models.CharField(verbose_name="انضباط", max_length = 32, null = True)
    scienceGrade = models.CharField(verbose_name="علوم", max_length = 32, null = True)
    specialSkillsAndTalents = models.CharField(verbose_name="توانایی و استعداد خاص", max_length= 256, null = True)
    #Father's information
    fatherName = models.CharField(max_length = 64, null = True, verbose_name = "نام پدر")
    fatherDateOfBirth = models.CharField(max_length = 16, verbose_name = "تاريخ تولد پدر", null = True)
    fatherNationalCodeNumber = models.CharField(max_length = 32,verbose_name = "شماره کد ملی پر", blank = True, null = True)
    fatherEdu = models.CharField(max_length = 32, verbose_name = "تحصیلات پدر", blank = True)
    fatherprantsCouncilExp = models.CharField(max_length = 32, verbose_name = "سابقه عضويت در انجمن اوليا پدر")
    fatherparentsCouncil = models.BooleanField(verbose_name = "داوطلب عضويت در انجمن اوليا (پدر)")
    fatherJob = models.CharField(max_length = 512, verbose_name = "شغل پدر", null = True)
    fatherWorkPhone = models.CharField(max_length = 32, verbose_name = "تلفن محل کار پدر", null = True)
    fatherPhoneNumber = models.CharField(max_length = 32, verbose_name = "شماره همراه پدر", null = True)
    fatherEmail = models.CharField(max_length = 32,verbose_name = "آدرس رايانامه پدر", blank = True)
    #Mother's information
    motherName = models.CharField(max_length = 64, null = True, verbose_name = "نام مادر")
    motherDateOfBirth = models.CharField(max_length = 16, verbose_name = "تاريخ تولد مادر", null = True)
    motherNationalCodeNumber = models.CharField(max_length = 32,verbose_name = "شماره کد ملی مادر", blank = True, null = True)
    motherEdu = models.CharField(max_length = 32, verbose_name = "تحصیلات مادر", blank = True)
    motherprantsCouncilExp = models.CharField(max_length = 32, verbose_name = "سابقه عضويت در انجمن اوليا مادر", blank = True)
    motherparentsCouncil = models.BooleanField(verbose_name = "داوطلب عضويت در انجمن اوليا (مادر)")
    motherJob = models.CharField(max_length = 512, verbose_name = "شغل  مادر", null = True)
    motherWorkPhone = models.CharField(max_length = 32, verbose_name = "تلفن محل کار مادر", null = True)
    motherPhoneNumber = models.CharField(max_length = 32, verbose_name = "شماره همراه مادر", null = True)
    motherEmail = models.CharField(max_length = 64,verbose_name = "آدرس رايانامه مادر", blank = True)
    #Family Details
    UM = models.CharField(max_length = 512, verbose_name = "دانشگاه و رشته تحصيلی فرزند دانشگاهی", blank = True)
    HS = models.CharField(max_length = 32, verbose_name = "وضعيت مسکن خانواده", blank = True)
    FS = models.CharField(max_length = 32, verbose_name = "وضعيت خانواده", blank = True)
    WITSLW = models.CharField(max_length = 128, verbose_name = "دانش آموز با چه کسی زندگی ميکند؟", null = True)
    houseAddress = models.CharField(max_length = 256, verbose_name = "آدرس منزل", null = True)
    postalCode = models.CharField(max_length=32, verbose_name = "کد پستی", null = True)
    phoneNumber = models.CharField(max_length = 16, verbose_name = "شماره تلفن", null = True)
    #Other
    otherInfo = models.CharField(max_length = 512, verbose_name = "توضيحات", blank = True)
    class Meta:
        verbose_name ="درخواست ثبت نام"
        verbose_name_plural ="درخواست های ثبت نام"
    def __str__(self):
        return (self.Name + " " + self.familyName)