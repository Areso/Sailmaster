//polyfill for ES5 include
include = function (url, fn) {
  var e = document.createElement("script");
  e.onload = fn;
  e.src = url;
  e.async=true;
  document.getElementsByTagName("head")[0].appendChild(e);
};
//main code
function getRaces () {
  resRaces      = null;
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState === 4) {
      if (this.status === 200) {
        resRaces      = JSON.parse(this.responseText);
        resRaces      = resRaces["msg"];
        populateSelRaces();
      }
    }
  };
  xhttp.open("GET", "http://mydiod.ga:6689/api/v1.0/get_races", true);
  xhttp.send();
}
getRaces();
function populateSelRaces() {
  
}
//localization
page = "char";
include('js/vendor/localization.js',function(){
  loadStartLocale(page);
});
function localeCallback(returnLanguage) {
  for (key in pageChar) {
    if (pageChar.hasOwnProperty(key)) {
      document.getElementById(key).innerText=pageChar[key];
    }
  }
}
