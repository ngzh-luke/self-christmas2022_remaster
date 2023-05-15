// Helper functions

// Welcome popup
function hit() {
  Swal.fire({
    title: "Surprise Present is ready for you!",
    html: "Aren't you excited?",
    icon: "info",
    confirmButtonText: "Exciting!",
    confirmButtonAriaLabel: "Thumbs up, sure!",
  }).then(() => {
    window.location.assign("/login");
  });
}

// Pre-defined account checker
async function theChecker(loc = "") {
  if (loc == "login-integrated") {
    var htmlCode =
      '<form class="form" action="/check/" method="POST"> ' +
      "<h3 style='font-weight: bold; color: red'>Check pre-defined account</h3>" +
      '<input class="col-8 my-2" type="search" placeholder="Search Here" aria-label="Search" autocapitalize="characters" name="account_" id="account_"/><br>' +
      // '<p>(Ex. If your name is John Blue, type in "John" or "JOHN" or "john")</p>' +
      '<input type="submit" value="Search Now!" class="btn-lg" />' +
      "</form>";
  } else {
    var htmlCode =
      '<form class="form" action="/check-account/by-first-name/" method="POST"> ' +
      "<h3 style='font-weight: bold; color: red'>Check pre-defined account</h3>" +
      '<input class="col-8 my-2" type="search" placeholder="Search Here" aria-label="Search" autocapitalize="characters" name="account_" id="account_"/><br>' +
      '<input type="submit" value="Search Now!" class="btn-lg" />' +
      "</form>";
  }
  Swal.fire({
    title: "Submit your Firstname",
    html: htmlCode,
    showCancelButton: true,
    showConfirmButton: false,
    showLoaderOnConfirm: true,

    allowOutsideClick: () => !Swal.isLoading(),
  });
}

// Account password changer
async function theChanger(alias = "") {
  if (alias != "") {
    var htmlCode =
      '<form class="form" action="/' +
      alias +
      '/account-management/change-password/" method="POST"> ' +
      "<h4 style='color:red;' >New password should have at least 8 charecters long and must not be easily guess</h4>" +
      '<input class="col-6 my-2" type="password" placeholder="Current Password" name="current" id="current"  /><br>' +
      '<input class="col-6 my-2" type="password" placeholder="New Password" name="new" id="new"  /><br>' +
      '<input class="col-6 my-2" type="password" placeholder="Confirm New Password" name="confirmNew" id="confirmNew" /> <br>' +
      '<input type="submit" value="Confirm Changes" class="btn btn-lg btn-success" />' +
      "</form>";
  } else {
    var htmlCode =
      "You can't change account password when you didn't login to the system";
  }
  Swal.fire({
    title: "Account Password Changer",
    html: htmlCode,
    showCancelButton: true,
    showConfirmButton: false,
    showLoaderOnConfirm: true,
    allowOutsideClick: false,
  });
}

// System security warning
async function warner(msg = "") {
  var htmlCode =
    "<div " +
    'class="text-center my-2 px-2 mx-2 " align="center">' +
    "<a href='/wanna-change-password/'>" +
    '<button class="btn btn-lg btn-success" >' +
    "Change Now!</button></a><br />" +
    '<a href="/"> ' +
    '<button class="btn btn-dark" >Maybe Later</button></a></div>' +
    '<div style="font-weight: bolder; color: red">' +
    "<h3>" +
    msg +
    "</h3>" +
    "</div>";
  Swal.fire({
    // title: "Warning!",
    html: htmlCode,
    icon: "warning",
    showCancelButton: false,
    showConfirmButton: false,
    allowOutsideClick: false,
    allowEscapeKey: false,
  });
}

// Account risk level manually check
async function riskLevelChecker() {
  var htmlCode =
    '<form class="form" action="/@system-@security-check/account-risk-level-check/" method="POST"> ' +
    "<h3>Please confirm your password in order to process</h3>" +
    '<input class="col-8 my-2" type="password" placeholder="Password" name="confirmPassword" /><br>' +
    '<input type="submit" value="Process" class="btn btn-lg btn-info" />' +
    "</form>";
  Swal.fire({
    // title: "Warning!",
    html: htmlCode,
    icon: "question",
    showCancelButton: true,
    showConfirmButton: false,
    allowOutsideClick: true,
    allowEscapeKey: true,
  });
}

// Pop up contact info
async function contactMe() {
  htmlCode =
    '<div class="email py-1 mx-1"><strong>Email:</strong> <i>contact@lukecreated.com</i></div>';
  Swal.fire({
    title: "Reach me via...",
    icon: "info",
    html: htmlCode,
    showCancelButton: false,
    showConfirmButton: true,
    showLoaderOnConfirm: true,
    confirmButtonText: "OKAY!",
    confirmButtonAriaLabel: "okay!",

    allowOutsideClick: () => !Swal.isLoading(),
  });
}

// Question query
async function query() {
  var htmlCode =
    '<form class="form" action="/Kan/have-fun-with-my-game/questions-management/query/" method="POST"> ' +
    "<h3>What question you would like to manage</h3>" +
    '<input class="col-5 my-2" type="number" placeholder="Question id" name="id" /><br>' +
    '<input type="submit" value="Continue" class="btn btn-lg btn-info" /></form>' +
    '<br> Add new? <a href="/add"> <button class="btn btn-warning" >New Question</button></a>' +
    '<br><a href="/question-manager/"> <button class="btn btn-danger" >Cancel</button></a>';
  Swal.fire({
    title: "Question ID",
    html: htmlCode,
    icon: "question",
    showCancelButton: false,
    showConfirmButton: false,
    allowOutsideClick: false,
    allowEscapeKey: false,
  });
}

// set lang helper
async function langHelper(lan = "") {
  if (lan == "EN") {
    var title = "ภาษาจะเปลี่ยนเมื่อเว็บไซต์รีโหลดโดยอัตโนมัติ";
  } else {
    title = "Language will be changed after automatically reloaded";
  }
  const Toast = Swal.mixin({
    toast: true,
    position: "top-end",
    showConfirmButton: false,
  });
  Toast.fire({
    title: title,
    icon: "info",
    showCancelButton: false,
    showConfirmButton: false,
    allowOutsideClick: false,
    allowEscapeKey: false,
  });
}
