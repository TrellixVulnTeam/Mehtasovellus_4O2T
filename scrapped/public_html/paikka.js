
//fetch('https://bgpo5j271l.execute-api.eu-west-1.amazonaws.com/dev/v1/all');

//let obj = JSON.parse(response[getCookie(point)]);

function setCookie(name,value,days) {
  var expires = "";
  if (days) {
      var date = new Date();
      date.setTime(date.getTime() + (days*24*60*60*1000));
      expires = "; expires=" + date.toUTCString();
  }
  document.cookie = name + "=" + (value || "")  + expires + "; path=/";
}
function getCookie(c_name) {
  var i, x, y, ARRcookies = document.cookie.split(";");
  for (i = 0; i < ARRcookies.length; i++) {
      x = ARRcookies[i].substr(0, ARRcookies[i].indexOf("="));
      y = ARRcookies[i].substr(ARRcookies[i].indexOf("=") + 1);
      x = x.replace(/^\s+|\s+$/g, "");
      if (x == c_name) {
          return unescape(y);
      }
  }
}
function eraseCookie(name) {   
  document.cookie = name+'=; Max-Age=-99999999;';  
}

document.getElementById("movebtn").onclick = () => {
  setCookie("doc", "0", 1)
  window.location.href = "jotain.html";
}
