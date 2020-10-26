//polyfill for ES5 include
include = function (url, fn) {
  var e = document.createElement("script");
  e.onload = fn;
  e.src = url;
  e.async=true;
  document.getElementsByTagName("head")[0].appendChild(e);
};
//main code

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
