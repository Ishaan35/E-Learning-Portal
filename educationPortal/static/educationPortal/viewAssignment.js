function downloadAll() {
  let files = document.getElementsByClassName("fileLink");

  for (let i = 0; i < files.length; i++) {
    files[i].click();
  }
}

function displayFiles() {
  let files = document.getElementById("files").files;
  let list = document.getElementById("fileList");
  list.innerHTML = "";

  for (let i = 0; i < files.length; i++) {
    list.innerHTML += `<pre style='font: inherit; overflow:hidden'><i class="fas fa-file" style="color: gray; padding-right:10px"></i>${files[i].name}</pre>`;
  }
}

function toggleHiddenSubmission(id, clickedItem) {
  let infoItems = document.getElementsByClassName("studentSubmissionInfoItem");
  let submissionItems = document.getElementsByClassName("submissionItem");
  for (let i = 0; i < infoItems.length; i++) {
    infoItems[i].hidden = true;
    if (submissionItems[i].classList.contains("submissionItemSelected")) {
      submissionItems[i].classList.remove("submissionItemSelected");
    }
  }
  document.getElementById(id).hidden = false;
  clickedItem.classList.add("submissionItemSelected");
}
