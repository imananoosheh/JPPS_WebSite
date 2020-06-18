var _validFileExtensions = [".jpg", ".jpeg", ".png"];    
function ValidateSingleInput(oInput) {
    if (oInput.type == "file") {
        var sFileName = oInput.value;
         if (sFileName.length > 0) {
            var blnValid = false;
            for (var j = 0; j < _validFileExtensions.length; j++) {
                var sCurExtension = _validFileExtensions[j];
                if (sFileName.substr(sFileName.length - sCurExtension.length, sCurExtension.length).toLowerCase() == sCurExtension.toLowerCase()) {
                    blnValid = true;
                    break;
                }
            }
             
            if (!blnValid) {
                var language = document.getElementsByTagName("HTML")[0].getAttribute("lang");
                if (language=="en"){
                    alert("Sorry, " + sFileName + " is invalid, allowed extensions are: " + _validFileExtensions.join(", "));
                oInput.value = "";
                return false;
                } else {
                    alert("متاسفانه فایل, " + sFileName + " به درستی وارد نشده است, پسوند های مجاز در روبرو آمده اند.: " + _validFileExtensions.join(", "));
                oInput.value = "";
                return false;
                }
                
            }
        }
    }
    return true;
}