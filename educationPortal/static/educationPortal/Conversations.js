const element = document.querySelectorAll(".texts")[0];
element.scrollTo(element.scrollHeight, element.scrollHeight);

function showSuggestions() {
  let inputfieldvalue = document.getElementById(
    "newConversationInputField"
  ).value;
  let suggestionsDiv = document.getElementById("suggestionDiv");

  if (inputfieldvalue.trim().length == 0) {
    suggestionsDiv.hidden = true;
  } else {
    suggestionsDiv.hidden = false;
    let results = suggestionsDiv.querySelectorAll("#suggestionDiv > div");

    let visibleCounter = 0;

    //max 8 results at a time
    for (let i = 0; i < results.length; i++) {
      if (visibleCounter < 8) {
        if (
          results[i].id.toUpperCase().indexOf(inputfieldvalue.toUpperCase()) < 0
        ) {
          results[i].hidden = true;
        } else {
          results[i].hidden = false;
          visibleCounter++;
        }
      } else {
        results[i].hidden = true;
      }
    }
  }
}

async function addConversation(userDivId) {
  let username = userDivId.substring(0, userDivId.indexOf(" "));

  await fetch(`/addConversation/`, {
    method: "POST",
    body: JSON.stringify({
      username: username,
    }),
    headers: { "X-CSRFToken": getCookie("csrftoken") },
  });

  location.reload();
}

function selectConversation(id) {
  let conversations = document.querySelectorAll(".entireConversation");
  let textLists = document.querySelectorAll(".texts");
  id = id.substring(id.indexOf(":") + 1); //the current conversation buttons on the left panel each have an id. Just extract the number and get the actual conversation div using that number in the id

  for (let i = 0; i < conversations.length; i++) {
    if (conversations[i].id == `conversation:${id}`) {
      conversations[i].hidden = false;
      textLists[i].scrollTo(
        textLists[i].scrollHeight,
        textLists[i].scrollHeight
      );
    } else {
      conversations[i].hidden = true;
    }
  }
}
async function deleteConversation(id) {
  id = parseInt(id);
  await fetch(`/addConversation/`, {
    method: "DELETE",
    body: JSON.stringify({
      id: id,
    }),
    headers: { "X-CSRFToken": getCookie("csrftoken") },
  });

  location.reload();
}

async function sendMessage(id) {
  id = parseInt(id);
  let text = document.getElementById(`messageField:${id}`).value;

  await fetch(`/sendText/`, {
    method: "POST",
    body: JSON.stringify({
      id: id,
      text: text,
    }),
    headers: { "X-CSRFToken": getCookie("csrftoken") },
  });

  location.reload();
}
