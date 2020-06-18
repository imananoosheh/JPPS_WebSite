import json
import urllib.request as reqq
import urllib 

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from .models import registered,coverImage
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def registration(request):
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
        name = request.POST.get('studentname')
        familyName = request.POST.get('studentlastname')
        idNumber = request.POST.get('idnumber')
        bsNumber = request.POST.get('bsnumber')
        placeofbirth = request.POST.get('placeofbirth')
        bssnumber = request.POST.get('bssnumber')
        dateofbirth = request.POST.get('dateofbirth')
        regfor = request.POST.get('regfor')
        yourreference = request.POST.get('yourreference')
        religion = request.POST.get("religion")
        currentschool = request.POST.get("currentschool")
        avgscore = request.POST.get("avgscore")
        mathscore = request.POST.get("mathscore")
        disciplinescore = request.POST.get("disciplinescore")
        sciencescore = request.POST.get("sciencescore")
        talent = request.POST.get("talent")
        fathername = request.POST.get("fathername")
        fatherdateofbirth = request.POST.get("fatherdateofbirth")
        fatheridnumber = request.POST.get("fatheridnumber")
        fatheredu = request.POST.get("fatheredu")
        PTCM = request.POST.get("PTCM")
        VF = request.POST.get("VF")
        fatheroccupation = request.POST.get("fatheroccupation")
        worknumber = request.POST.get("worknumber")
        fathermobile = request.POST.get("fathermobile")
        fatheremail = request.POST.get("fatheremail")
        mothername = request.POST.get("mothername")
        motherdateofbirth = request.POST.get("motherdateofbirth")
        motheridnumber = request.POST.get("motheridnumber")
        motheredu = request.POST.get("motheredu")
        PTCMM = request.POST.get("PTCMM")
        VM = request.POST.get("VM")
        motheroccupation = request.POST.get("motheroccupation")
        worknumberm = request.POST.get("worknumberm")
        mothermobile = request.POST.get("mothermobile")
        motheremail = request.POST.get("motheremail")
        siblingsedu = request.POST.get("siblingsedu")
        accsituation = request.POST.get("accsituation")
        familysituation = request.POST.get("familysituation")
        stulivewith = request.POST.get("stulivewith")
        homeaddress = request.POST.get("homeaddress")
        postalcode = request.POST.get("postalcode")
        housetelephone = request.POST.get("housetelephone")
        otherinfo = request.POST.get("otherinfo")
        personalPhoto = request.FILES['profilepic']
        if VM is None:
            VM = False
        else:
            VM = True
        if VF is None:
            VF = False
        else:
            VF = True

        #adding the values in a context variable 
        #returing the template 
        newform = registered(
            Name = name,
            familyName = familyName,
            idNumber = idNumber,
            bsNumber = bsNumber,
            placeofbirth = placeofbirth,
            bssnumber = bssnumber,
            dateOfBirth = dateofbirth,
            regfor = regfor,
            yourreference = yourreference,
            religion = religion,
            personalPhoto = personalPhoto,
            currentSchool = currentschool,
            average = avgscore,
            mathGrade = mathscore,
            disciplineGrade = disciplinescore,
            scienceGrade = sciencescore,
            specialSkillsAndTalents = talent,
            fatherName = fathername,
            fatherDateOfBirth = fatherdateofbirth,
            fatherNationalCodeNumber = fatheridnumber,
            fatherEdu = fatheredu,
            fatherprantsCouncilExp = PTCM,
            fatherparentsCouncil = VF,
            fatherJob = fatheroccupation,
            fatherWorkPhone = worknumber,
            fatherPhoneNumber = fathermobile,
            fatherEmail = fatheremail,
            motherName = mothername,
            motherDateOfBirth = motherdateofbirth,
            motherNationalCodeNumber = motheridnumber,
            motherEdu = motheredu,
            motherprantsCouncilExp = PTCMM,
            motherparentsCouncil = VM,
            motherJob = motheroccupation,
            motherWorkPhone = worknumberm,
            motherPhoneNumber = mothermobile,
            motherEmail = motheremail,
            UM = siblingsedu,
            HS = accsituation,
            FS = familysituation,
            WITSLW = stulivewith,
            houseAddress = homeaddress,
            postalCode = postalcode,
            phoneNumber = housetelephone,
            otherInfo = otherinfo,
        )
        if result['success']:
            try:
                cover = coverImage.objects.latest('id')
            except ObjectDoesNotExist:
                cover = None
            context = {
                'cover' : cover,
            }
            newform.save()
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
        return render(request, 'registration.html', context)