from django.contrib import admin
from .models import content,registered,coverImage
from django.http import HttpResponse
import codecs
class registeredAdmin(admin.ModelAdmin):
    actions = ['download_excel']
    def download_excel(self, request, queryset):
        import xlwt
        from xlwt import Workbook
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="Registred.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Registred')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['نام', 'نام خانوادگی','شماره کد ملی',"شماره شناسنامه","تاريخ تولد","محل صدور شناسنامه","شماره سريال شناسنامه","داوطلب ثبت نام در","نحوه آشنايی با مدرسه","دين و مذهب","مدرسه فعلی","معدل","ریاضی","انضباط","علوم","توانایی و استعداد خاص","نام پدر","تاريخ تولد پدر","شماره کد ملی پر", "تحصیلات پدر","سابقه عضويت در انجمن اوليا پدر","داوطلب عضويت در انجمن اوليا (پدر)","شغل پدر","تلفن محل کار پدر","شماره همراه پدر", "آدرس رايانامه پدر","نام مادر","تاريخ تولد مادر","شماره کد ملی مادر","تحصیلات مادر","سابقه عضويت در انجمن اوليا مادر","داوطلب عضويت در انجمن اوليا (مادر)", "شغل  مادر","تلفن محل کار مادر","شماره همراه مادر","آدرس رايانامه مادر", "دانشگاه و رشته تحصيلی فرزند دانشگاهی","وضعيت مسکن خانواده","وضعيت خانواده","دانش آموز با چه کسی زندگی ميکند؟","آدرس منزل","کد پستی","شماره تلفن", "توضيحات"]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        rows = queryset.all()
        for row in rows:
            row_num += 1
            tempMother = ""
            tempFather = ""
            if row.motherparentsCouncil:
                tempMother = "بله"
            else:
                tempMother = "خیر"
            if row.fatherparentsCouncil:
                tempFather = "بله"
            else:
                tempMother = "خیر"
            col=[row.Name,row.familyName,row.idNumber,row.bsNumber,row.dateOfBirth,row.placeofbirth,row.bssnumber,row.regfor,row.yourreference,row.religion,row.currentSchool,row.average,row.mathGrade,row.disciplineGrade,row.scienceGrade,row.specialSkillsAndTalents,row.fatherName,row.fatherDateOfBirth,row.fatherNationalCodeNumber,row.fatherEdu,row.fatherprantsCouncilExp,tempFather,row.fatherJob,row.fatherWorkPhone,row.fatherPhoneNumber,row.fatherEmail,row.motherName,row.motherDateOfBirth,row.motherNationalCodeNumber,row.motherEdu,row.motherprantsCouncilExp,tempMother,row.motherJob,row.motherWorkPhone,row.motherPhoneNumber,row.motherEmail,row.UM,row.HS,row.FS,row.WITSLW,row.houseAddress,row.postalCode,row.phoneNumber,row.otherInfo]
            for col_num in range(len(col)):
                ws.write(row_num, col_num, col[col_num], font_style)

        wb.save(response)
        return response
    download_excel.short_description = "دانلود اطلاعات"

admin.site.register(coverImage)
admin.site.register(content)
admin.site.register(registered, registeredAdmin)
