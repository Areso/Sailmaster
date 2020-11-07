//polyfill for ES5 include
include = function (url, fn) {
  var e = document.createElement("script");
  e.onload = fn;
  e.src = url;
  e.async=true;
  document.getElementsByTagName("head")[0].appendChild(e);
};
//main code
function getPortraits () {
  var x = document.getElementById("selRace").selectedIndex;
  var y = document.getElementById("selRace").options;
  raceID = y[x].value; //y[x].id, text, index, value
  var x = document.getElementById("selGender").selectedIndex;
  var y = document.getElementById("selGender").options;
  gender = y[x].value; //y[x].id, text, index, value
  resPortraits      = null;
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState === 4) {
      if (this.status === 200) {
        resPortraits      = JSON.parse(this.responseText);
        resPortraits      = resPortraits["msg"];
        reloadPortraits(resPortraits);
        console.log(resPortraits);
      }
    }
  };
  queryPortraits = "http://mydiod.ga:6689/api/v1.0/get_portraits?race="+raceID+"&gender="+gender;
  xhttp.open("GET", queryPortraits, true);
  xhttp.send();
}
getRaces();
currentImg = 0;
function getRaces() {
  resRaces      = null;
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState === 4) {
      if (this.status === 200) {
        resRaces      = JSON.parse(this.responseText);
        resRaces      = resRaces["msg"];
        populateSelRaces(resRaces);
      }
    }
  };
  xhttp.open("GET", "http://mydiod.ga:6689/api/v1.0/get_races", true);
  xhttp.send();

}
function populateSelRaces(resRaces) {
  selRace = document.getElementById("selRace");
  for (i = 0; i < resRaces.length; i++){
    selRace.add(new Option(lblRaces[i], resRaces[i]));
  }
  selRace.selectedIndex = 0;
  getPortraits();
}
function reloadPortraits(currentImg) {
  if (resPortraits !== null) {
    document.getElementById("imgPortrait").src ="resources/portraits/"+currentImg+".png";
  }
  //xhttp.open("GET", "http://armata.ga:5000/api/v1.0/get_event_details?uid="+game.UID, true);
}
function prevImg() {

}
function nextImg() {

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
