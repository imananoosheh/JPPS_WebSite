//getting the cookie's value and checking it in order to change or keep the language

function getCookie(cname) {
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for (var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

function checkCookie() {
  var langValue = getCookie("lang");
  if (langValue == "en") { document.getElementsByTagName("HTML")[0].setAttribute("lang", "en");}
  else if (langValue == "fa") { document.getElementsByTagName("HTML")[0].setAttribute("lang", "fa");}
}
