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
        currentImgIndex   = 0;
        maxImgIndex       = resPortraits.length-1;
        reloadPortraits(resPortraits);
        console.log(resPortraits);
      }
    }
  };
  queryPortraits = "http://mydiod.ga:6689/api/v1.0/get_portraits?race="+raceID+"&gender="+gender;
  xhttp.open("GET", queryPortraits, true);
  xhttp.send();
}
getExistingChars();
getRaces();
currentImgIndex = 0;
maxImgIndex = 0;
function getExistingCharsRq () {
  token    = localStorage.getItem('sailmaster-token');
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
      chars    = JSON.parse(this.responseText);
      chars_msg= chars["msg"];
      console.log(char);
      getExistingChars();
    }
  };
  xhttp.open("GET", "http://mydiod.ga:6689/api/v1.0/get_chars", true);
  xhttp.setRequestHeader("Content-type", "application/json");
  xhttp.setRequestHeader("token", token);
  xhttp.send(payload);
};
function getExistingChars() {
	//
}
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
function reloadPortraits() {
  if (resPortraits !== null) {
    document.getElementById("imgPortrait").src ="resources/portraits/"+resPortraits[currentImgIndex]+".png";
  }
}
function prevImg() {
  if (currentImgIndex > 0) {
    currentImgIndex = currentImgIndex-1;
    reloadPortraits();
  } else {
    currentImgIndex = maxImgIndex;
    reloadPortraits();
  }
}
function nextImg() {
  if (currentImgIndex < maxImgIndex) {
    currentImgIndex = currentImgIndex+1;
    reloadPortraits();
  } else {
    currentImgIndex = 0;
    reloadPortraits();
  }
}
function createChar () {
  dataToParse={};
  dataToParse.Charname = document.getElementById("inpCharname").value;
  var x = document.getElementById("selRace").selectedIndex;
  var y = document.getElementById("selRace").options;
  dataToParse.Race     = parseInt(y[x].value); //y[x].id, text, index, value
  var x = document.getElementById("selGender").selectedIndex;
  var y = document.getElementById("selGender").options;
  dataToParse.Gender   = parseInt(y[x].value); //y[x].id, text, index, value
  dataToParse.Portrait = resPortraits[currentImgIndex];
  dataToParse.Token    = localStorage.getItem('sailmaster-token');
  console.log(dataToParse);
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
      resAccCreation    = JSON.parse(this.responseText);
      resAccCreation    = resAccCreation["msg"];
      console.log(resAccCreation);
    }
  };
  payload = JSON.stringify(dataToParse);
  xhttp.open("POST", "http://mydiod.ga:6689/api/v1.0/char_create", true);
  xhttp.setRequestHeader("Content-type", "application/json");
  xhttp.send(payload);
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

