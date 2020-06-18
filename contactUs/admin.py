from django.contrib import admin
from .models import workRequest,coverImage
from django.http import HttpResponse
import codecs
class workRequestAdmin(admin.ModelAdmin):
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

        columns = ['ﻥﺎﻣ', 'ﻥﺎﻣ ﺥﺎﻧﻭﺍﺩگی',"ﻥﺎﻣ پﺩﺭ","ﺶﻣﺍﺮﻫ کﺩ ﻢﻟی","ﺶﻣﺍﺮﻫ ﺶﻧﺎﺴﻧﺎﻤﻫ","ﺕﺍﺮﻴﺧ ﺕﻮﻟﺩ", "ﻢﺤﻟ ﺹﺩﻭﺭ ﺶﻧﺎﺴﻧﺎﻤﻫ","ﻮﻀﻋیﺕ ﺕﺎﻬﻟ","ﺂﺧﺭیﻥ ﻡﺩﺭک ﺖﺤﺻیﻝی","ﺮﺸﺘﻫ","ﻥﻮﻋ ﺎﺴﺘﺧﺩﺎﻣ","ﺕﺍﺭیﺥ ﺎﺴﺘﺧﺩﺎﻣ","ﻭﺎﺣﺩ ﺱﺍﺰﻣﺎﻧی","ﻢﻨﻄﻘﻫ","ﺱﻭﺎﺒﻗ ﺥﺪﻤﺗی","ﺖﺴﻠﻃ ﺏﺭ ﺰﺑﺎﻧ ﺎﻧگﻝیﺱی","ﺖﺴﻠﻃ ﺏﺭ کﺎﻣپیﻮﺗﺭ","ﺖﺴﻠﻃ ﺏﺭ ﺖﺨﺘﻫ ﻩﻮﺸﻤﻧﺩ","ﻢﻫﺍﺮﺗ ﻩﺍی ﺩیگﺭ","ﻉﻼﻘﻫ ﻢﻧﺩ ﺐﻫ ﺕﺩﺭیﺱ پﺍیﻩ","ﻥﺎﻣ ﻢﻋﺮﻓ ﺍﻮﻟ","ﻥﺎﻣ ﺥﺎﻧﻭﺍﺩگی ﻢﻋﺮﻓ ﺍﻮﻟ","ﺁﺩﺮﺳ ﻢﻧﺰﻟ یﺍ ﻢﺤﻟ کﺍﺭ ﺏﺍ ﺖﻠﻔﻧ ﻢﻋﺮﻓ ﺍﻮﻟ","ﻥﺎﻣ ﻢﻋﺮﻓ ﺩﻮﻣ","ﻥﺎﻣ ﺥﺎﻧﻭﺍﺩگی ﻢﻋﺮﻓ ﺩﻮﻣ","ﺁﺩﺮﺳ ﻢﻧﺰﻟ یﺍ ﻢﺤﻟ کﺍﺭ ﺏﺍ ﺖﻠﻔﻧ ﻢﻋﺮﻓ ﺩﻮﻣ","ﺕﻮﺿیﺡﺎﺗ"]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        rows = queryset.all()
        for row in rows:
            row_num += 1
            col=[row.Name,row.familyName,row.fatherName,row.idNumber,row.bsNumber,row.dateOfBirth,row.placeofbirth,row.married,row.lastGraduate,row.major,row.employment,row.employmentDate,row.organizationUnit,row.district,row.background,row.englishLevel,row.computerSkills,row.smartBoardSkills,row.otherSkills,row.grade,row.firstName,row.firstFamilyName,row.firstAddress,row.secondName,row.secondFamilyName,row.secondAddress,row.other]
            for col_num in range(len(col)):
                ws.write(row_num, col_num, col[col_num], font_style)

        wb.save(response)
        return response
    download_excel.short_description = "ﺩﺎﻨﻟﻭﺩ ﺎﻃﻼﻋﺎﺗ"      

admin.site.register(coverImage)
admin.site.register(workRequest, workRequestAdmin)                                                

