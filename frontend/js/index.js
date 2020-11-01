//polyfill for ES5 include
include = function (url, fn) {
  var e = document.createElement("script");
  e.onload = fn;
  e.src = url;
  e.async=true;
  document.getElementsByTagName("head")[0].appendChild(e);
};
//main code
setInterval(checkStatuses,1000);
function checkStatuses () {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
      back_response = this.responseText;
      console.log(back_response)
    }
  };
  xhttp.open("GET", "http://localhost:6689/api/v1.0/heartbeat", true);
  //xhttp.setRequestHeader("Content-type", "application/json");
  xhttp.send();
}
function autoLogin () {
  if (localStorage.getItem('sailmaster-token')!==null) {
    //TODO check sessionKey
    console.log("login with existing token");
    loginWithToken();
  } else {
    console.log("create new account");
    createTempAcc();
  }
}
function loginWithToken () {
    window.location.href = "char.html";
}
function createTempAcc () {
  resTempAcc    = null;
  dataToParse   = "";
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
      resTempAcc    = JSON.parse(this.responseText);
      accToken      = resTempAcc["token"];
      console.log(accToken);
      localStorage.setItem('sailmaster-token', accToken);
      console.log("login with existing token");
      loginWithToken();
    }
  };
  xhttp.open("POST", "http://mydiod.ga:6689/api/v1.0/account_create", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send(dataToParse);
}
function showLoginForm () {
  console.log("show login form");
}
//localization
page = "index";
include('js/vendor/localization.js',function(){
  loadStartLocale(page);
});
function reloadLang() {
  var x = document.getElementById("selectLng").selectedIndex;
  var y = document.getElementById("selectLng").options;
  language = y[x].value; //y[x].id, text, index
  loadLocale(language, page);
}
function localeCallback(returnLanguage) {
  if (returnLanguage==='en-US') {
    document.getElementById("selectLng").selectedIndex=0;
  }
  if (returnLanguage==='ru-RU') {
    document.getElementById("selectLng").selectedIndex=1;
  }
  for (key in pageLogin) {
    if (pageLogin.hasOwnProperty(key)) {
      document.getElementById(key).innerText=pageLogin[key];
    }
  }
}
