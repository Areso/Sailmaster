//polyfill for ES5 include
include = function (url, fn) {
  var e = document.createElement("script");
  e.onload = fn;
  e.src = url;
  e.async=true;
  document.getElementsByTagName("head")[0].appendChild(e);
};
//main code
function autoLogin () {
  if (localStorage.getItem('sailmaster-acc-key')!==null) {
    //TODO check sessionKey
    console.log("login with existing token");
  } else {
    console.log("create new account");
    createTempAcc();
  }
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
    }
  };
  xhttp.open("POST", "http://mydiod.ga:6689/api/v1.0/create_acc", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send(dataToParse);
}
function showLoginForm () {
  console.log("show login form");
}
//localization
include('js/vendor/localization.js',function(){
  loadStartLocale();
  console.log('we are in first level include after loadStartLocale()');
});
function reloadLang() {
  var x = document.getElementById("selectLng").selectedIndex;
  var y = document.getElementById("selectLng").options;
  language = y[x].value; //y[x].id, text, index
  loadLocale(language);
}
function localeCallback(returnLanguage) {
  if (returnLanguage==='en-US') {
    document.getElementById("selectLng").selectedIndex=0;
  }
  if (returnLanguage==='ru-RU') {
    document.getElementById("selectLng").selectedIndex=1;
  }
  document.getElementById("mmenu-play").innerText = pagelogin.btnPlay;
  document.getElementById("mmenu-login").innerText = pagelogin.btnLogin;
}
