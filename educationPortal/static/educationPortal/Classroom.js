//text editor stuff
let output = document.getElementById("textDiv");
let buttons = document.getElementsByClassName("tool--btn");
for (let btn of buttons) {
  btn.addEventListener("click", () => {
    let cmd = btn.dataset["command"];
    if (cmd === "createlink") {
      let url = prompt("Enter a link: ");
      document.execCommand(cmd, false, url);
    } else {
      document.execCommand(cmd, false, null);
    }
  });
}

function showAnnouncementMaker() {
  document
    .getElementsByClassName("makeAnnouncement")[0]
    .classList.toggle("textEditorActive");
}

async function postAnnouncement(code) {
  let body = document.getElementById("textDiv").innerHTML;

  await fetch(`/makeAnnouncement/`, {
    method: "POST",
    body: JSON.stringify({
      body: body,
      code: code,
    }),
    headers: { "X-CSRFToken": getCookie("csrftoken") },
  });

  location.reload();
}

async function postComment(id, text) {
  id = parseInt(id.substring(id.indexOf(":") + 1));

  if (text != "") {
    await fetch(`/addComment/`, {
      method: "POST",
      body: JSON.stringify({
        text: text,
        id: id,
      }),
      headers: { "X-CSRFToken": getCookie("csrftoken") },
    });

    location.reload();
  }
}

function viewComments(id) {
  let element = document.getElementById(id);
  element.hidden = !element.hidden;
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
