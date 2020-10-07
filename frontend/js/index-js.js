function autoLogin () {
  if (localStorage.getItem('sailmaster-acc-key')!==null) {
    //TODO check sessionKey
    console.log("login with the sailmaster-acc-key");
  } else {
    console.log("create a temp account");
  }
}
function showLoginForm () {
  console.log("show login form");
}
