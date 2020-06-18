import json
import urllib.request as reqq
import urllib

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from .models import workRequest,coverImage
from django.views.decorators.csrf import csrf_exempt


def contactUs(request):
    if request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req =  reqq.Request(url, data=data)
        response = reqq.urlopen(req)
        result = json.loads(response.read().decode())
        #getting values from post
        name = request.POST.get('applicantname')
        familyName = request.POST.get('applicantlastname')
        idNumber = request.POST.get('idnumber')
        bsNumber = request.POST.get('bsnumber')
        placeofbirth = request.POST.get('placeofbirth')
        bssnumber = request.POST.get('bssnumber')
        dateofbirth = request.POST.get('dateofbirth')
        fathername = request.POST.get("applicantfathername")
        marriageStatus = request.POST.get("marriagestatus")
        edulevel = request.POST.get("edulevel")
        major = request.POST.get("major")
        contracttype = request.POST.get("contracttype")
        contractdate = request.POST.get("contractdate")
        orgname = request.POST.get("orgname")
        orgdistrict = request.POST.get("orgdistrict")
        workxp = request.POST.get("workxp")
        englishlvl = request.POST.get("englishlvl")
        computerlvl = request.POST.get("computerlvl")
        smartboard = request.POST.get("smartboard")
        otherskills = request.POST.get("otherskills")
        intrestedgrade = request.POST.get("intrestedgrade")
        nameintroducer1 = request.POST.get("name-introducer-1")
        lastnameintroducer1 = request.POST.get("lastname-introducer-1")
        addressintroducer1 = request.POST.get("address-introducer-1")
        nameintroducer2 = request.POST.get("name-introducer-2")
        lastnameintroducer2 = request.POST.get("lastname-introducer-2")
        addressintroducer2 = request.POST.get("address-introducer-2")
        othernotes = request.POST.get("othernotes")
        #adding the values in a context variable 
        #returing the template 
        newform = workRequest(
            Name = name,
            familyName = familyName,
            fatherName = fathername,
            idNumber = idNumber,
            bsNumber = bsNumber,
            dateOfBirth = dateofbirth,
            placeofbirth = placeofbirth,
            married = marriageStatus,
            lastGraduate = edulevel,
            major = major,
            employment = contracttype,
            employmentDate = contractdate,
            organizationUnit = orgname,
            district = orgdistrict,
            background = workxp,
            englishLevel = englishlvl,
            computerSkills = computerlvl,
            smartBoardSkills = smartboard,
            otherSkills = otherskills,
            grade = intrestedgrade,
            #recomendations
            firstName = nameintroducer1,
            firstFamilyName =  lastnameintroducer1,
            firstAddress = addressintroducer1,
            secondName = nameintroducer2,
            secondFamilyName =  lastnameintroducer2,
            secondAddress = addressintroducer2,
            other = othernotes
        )
        if result['success']:
            try:
                cover = coverImage.objects.latest('id')
            except ObjectDoesNotExist:
                cover = None
            context = {
                'cover' : cover,
            }
            return render(request, 'submitmessage.html', context)
        else:
            try:
                cover = coverImage.objects.latest('id')
            except ObjectDoesNotExist:
                cover = None
            context = {
                'cover' : cover,
            }
            return render(request, 'formerror.html', context)
    else:
        try:
            cover = coverImage.objects.latest('id')
        except ObjectDoesNotExist:
            cover = None
        context = {
            'cover' : cover,
        }
        return render(request, 'contactus.html', context)
