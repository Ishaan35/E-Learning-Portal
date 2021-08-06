let currentSelectedClassCode = "";

function setCode(code) {
  currentSelectedClassCode = code;
}
document.addEventListener("mouseup", function (e) {
  let profileDiv = document.getElementById("profilePopUp");
  let sideBar = document.getElementById("sideMenu");

  if (
    !profileDiv.contains(e.target) &&
    profileDiv.classList.contains("profilePopUpActive")
  ) {
    profileDiv.classList.toggle("profilePopUpActive");
  }

  if (
    !sideBar.contains(e.target) &&
    sideBar.classList.contains("sideMenuActive")
  ) {
    sideBar.classList.toggle("sideMenuActive");
  }
});

document.getElementById("menuBars").addEventListener("click", (e) => {
  document.getElementById("sideMenu").classList.toggle("sideMenuActive");
});

function newClass() {
  document
    .getElementsByClassName("greyBackground")[0]
    .classList.toggle("greyBackgroundActive");

  document
    .getElementsByClassName("newClassModal")[0]
    .classList.toggle("modalActive");

  if (document.getElementById("notValidCode")) {
    document.getElementById("notValidCode").hidden = true;
  }
}

async function createClass(name, subject) {
  let colorSelections = document.getElementsByClassName("colorSelect");
  let theme = "cardBlue";

  for (let i = 0; i < colorSelections.length; i++) {
    if (colorSelections[i].checked) {
      theme = colorSelections[i].value;
    }
  }

  await fetch(`createNewClassroom/${name}/`, {
    method: "POST",
    body: JSON.stringify({
      name: name,
      subject: subject,
      theme: theme,
    }),
    headers: { "X-CSRFToken": getCookie("csrftoken") },
  });

  location.reload();
}

async function joinClass(code) {
  let response = await fetch("/JoinClassroom/0");
  const data = await response.json();

  console.log(data.codes);
  let valid = false;
  for (let i = 0; i < data.codes.length; i++) {
    if (data.codes[i] == code) {
      valid = true;
      break;
    }
  }

  if (!valid) {
    document.getElementById("notValidCode").hidden = false;
  } else {
    //continue on with the process
    document.getElementById("notValidCode").hidden = true;

    await fetch(`JoinClassroom/${code}/`, {
      method: "PUT",
      body: JSON.stringify({
        code: code,
      }),
      headers: { "X-CSRFToken": getCookie("csrftoken") },
    });

    location.reload();
  }
}

async function leave(code) {
  setCode(code);

  document
    .getElementById("unEnrollBackground")
    .classList.toggle("greyBackgroundActive");

  document.getElementById("unEnrollModal").classList.toggle("modalActive");
}
async function leaveClass() {
  await fetch(`JoinClassroom/${currentSelectedClassCode}/`, {
    method: "DELETE",
    body: JSON.stringify({
      code: currentSelectedClassCode,
    }),
    headers: { "X-CSRFToken": getCookie("csrftoken") },
  });

  location.reload();
}

async function deleteClass(name, id) {
  console.log(id);

  await fetch(`createNewClassroom/${name}/`, {
    method: "DELETE",
    body: JSON.stringify({
      id: id,
    }),
    headers: { "X-CSRFToken": getCookie("csrftoken") },
  });

  location.reload();
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function profilePopUp() {
  document
    .getElementById("profilePopUp")
    .classList.toggle("profilePopUpActive");
}

function editPic() {
  document.getElementById("imageEdit").hidden =
    !document.getElementById("imageEdit").hidden;
}
