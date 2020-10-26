//THIS IS A PLUGGABLE LIBRARY
//WRITTEN BY ANTON GLADYSHEV
//MIT LICENSE
//inser this include to main file
/*
include = function (url, fn) {
	var e = document.createElement("script");
	e.onload = fn;
	e.src = url;
	e.async=true;
	document.getElementsByTagName("head")[0].appendChild(e);
};
*/
//entry point
//document.onload = loadStartLocale();
//now we need some language for start
itemName = "sailmaster-lang";
function loadStartLocale(page){
		//check whether browser support localStorage
		isLocalStorageSupport = checkLocalStorageSupport();
		if (isLocalStorageSupport===true) { //for all modern browsers, including IE8 and newer
			language = localStorage.getItem(itemName); //try load
			if (language === null) {
				language = getBrowserLanguage();
			}
		} else {
			//read cookies and find language

			//var regex = new RegExp("/(?:(?:^|.*;\\s*)/" + itemName + "/\\s*\\=\\s*([^;]*).*$)|^.*$/");
			//language = document.cookie.replace(regex, "$1");

			//PAY ATTENTION THERE IS A HAMMERED VALUE mmo-lang cause the code above doesn't work
			language = document.cookie.replace(/(?:(?:^|.*;\s*)sailmaster-lang\s*\=\s*([^;]*).*$)|^.*$/, "$1");
			if (language === null) {
				language = getBrowserLanguage();
			}
		}
		if (language.indexOf('en')!==-1) {
			language = 'en-US';
		}
		if (language.indexOf('ru')!==-1) {
			language = 'ru-RU';
		}
		locales = ['en-US','ru-RU'];
		default_locale = 'en-US';
		if (checkValue(language, locales)===1) {
			loadLocale(language, page);
		} else {
			loadLocale(default_locale, page);
		}
	}
function checkValue(value,arr){
		var status = -1;
		for(var i=0; i<arr.length; i++){
			var name = arr[i];
			if(name == value){
				status = 1;
				break;
			}
		}
		return status;
	}
function getBrowserLanguage() {
		//if not set, then
		try { //try to get the browser language
			language = navigator.language;
		} catch(e) { //in case we use IE9, IE8
			language = navigator.userLanguage;
		}
		if (language===null) {//just to be sure about IE9, IE8
			language = navigator.userLanguage;
		}
		return language;
	}
function checkLocalStorageSupport() {
		var test = 'test';
		try {
			localStorage.setItem(test, test);
			localStorage.removeItem(test);
			return true;
		} catch(e) {
			return false;
		}
	}
function loadLocale(language, page){
	file = 'languages/'+page+'-'+language+'.js';
	include(file,function(){
		console.log('we are in second level include');
		localeCallback(language);
	});
	isLocalStorageSupport = checkLocalStorageSupport();
	if (isLocalStorageSupport===true) { //for all modern browsers, including IE8 and newer
		localStorage.setItem(itemName, language); //try save
	} else {
		document.cookie = itemName+"="+language;
	}
};

