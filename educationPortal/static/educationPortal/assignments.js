function newAssignmentModal() {
  try {
    document.getElementById("textDiv").innerHTML = "";
    document.getElementById("instructionsInput").value = null;
    document.getElementById("files").value = null;
    document.getElementById("assignmentForm").reset();

    let list = document.getElementById("fileList");
    list.innerHTML = "";
  } catch {}

  document
    .getElementsByClassName("greyBackground")[0]
    .classList.toggle("greyBackgroundActive");

  document
    .getElementsByClassName("newAssignmentModal")[0]
    .classList.toggle("modalActive");

  try {
    document.getElementsByClassName("custom-file-upload")[0].hidden =
      !document.getElementsByClassName("custom-file-upload")[0].hidden;
  } catch {}

  try {
    let items = document.getElementsByClassName("submitBtn");
    for (let i = 0; i < items.length; i++) {
      items[i].hidden = !items[i].hidden;
    }
  } catch {}
}

try {
  document.getElementById("textDiv").addEventListener("input", function () {
    value = document.getElementById("textDiv").innerHTML;
    document.getElementById("instructionsInput").value = value;
  });
} catch {}

function displayFiles() {
  let files = document.getElementById("files").files;
  let list = document.getElementById("fileList");
  list.innerHTML = "";

  for (let i = 0; i < files.length; i++) {
    list.innerHTML += `<pre style='font: inherit; overflow:hidden'><i class="fas fa-file" style="color: gray; padding-right:10px"></i>${files[i].name}</pre>`;
  }
}

function setDate(value) {
  let str1 = value.substring(0, value.indexOf("_"));
  let str2 = value.substring(value.indexOf("_") + 1);

  date = str1 + "T" + str2;
  console.log(date);

  document.getElementById("assignmentDueDate").value = date;
}
