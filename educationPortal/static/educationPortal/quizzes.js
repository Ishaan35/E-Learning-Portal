let QuizName = "";
let DueDate = undefined;
let questions = new Array();
questions.push({
  question: "",
  option1: "",
  option2: "",
  option3: "",
  option4: "",
  correct: 1,
});

let currentQuestion = 0;

try {
  render();
} catch (e) {}

function update(e) {
  questions[currentQuestion].question =
    document.getElementById("questionName").value;
  questions[currentQuestion].option1 =
    document.getElementById("option1Input").value;

  questions[currentQuestion].option2 =
    document.getElementById("option2Input").value;
  questions[currentQuestion].option3 =
    document.getElementById("option3Input").value;
  questions[currentQuestion].option4 =
    document.getElementById("option4Input").value;
}

function render() {
  document.getElementById("questionCounter").innerHTML = `Question ${
    currentQuestion + 1
  } of ${questions.length}`;
  document.getElementById("questionName").value =
    questions[currentQuestion].question;
  document.getElementById("option1Input").value =
    questions[currentQuestion].option1;
  document.getElementById("option2Input").value =
    questions[currentQuestion].option2;
  document.getElementById("option3Input").value =
    questions[currentQuestion].option3;
  document.getElementById("option4Input").value =
    questions[currentQuestion].option4;

  let items = document.getElementsByClassName("optionCheck");
  for (let i = 0; i < items.length; i++) {
    if (questions[currentQuestion].correct - 1 != i) {
      items[i].classList.remove("optionCorrect");
    } else {
      items[i].classList.add("optionCorrect");
    }
  }
}

function add() {
  questions.splice(currentQuestion + 1, 0, {
    question: ``,
    option1: ``,
    option2: ``,
    option3: ``,
    option4: ``,
    correct: 1,
  });
  currentQuestion++;
  render();
  makeList();

  items = document.getElementsByClassName("questionListItem");
  for (let i = 0; i < items.length; i++) {
    if (items[i].classList.contains("questionListItemSelected"))
      items[i].classList.remove("questionListItemSelected");
  }
  document
    .getElementById(`listItem:${currentQuestion}`)
    .classList.add("questionListItemSelected");
}

function setCurrentQuestion(id) {
  currentQuestion = parseInt(id.substring(id.indexOf(":") + 1));
  render();

  items = document.getElementsByClassName("questionListItem");
  for (let i = 0; i < items.length; i++) {
    if (items[i].classList.contains("questionListItemSelected"))
      items[i].classList.remove("questionListItemSelected");
  }
  document.getElementById(id).classList.add("questionListItemSelected");
}

function makeList() {
  let questionList = document.getElementById("questionList");

  questionList.innerHTML = "";
  questionList.innerHTML += "<h6>Questions:</h6>";
  for (let i = 0; i < questions.length; i++) {
    id = `listItem:${i}`;
    text =
      questions[i].question != ""
        ? `${i + 1}. ${questions[i].question}`
        : ` ${i + 1}: Unnamed Question`;
    questionList.innerHTML += `<div class='questionListItem' id=${id} onclick="setCurrentQuestion('${id}')"> ${text} </div>`;
  }

  items = document.getElementsByClassName("questionListItem");
  for (let i = 0; i < items.length; i++) {
    if (items[i].classList.contains("questionListItemSelected"))
      items[i].classList.remove("questionListItemSelected");
  }
  document
    .getElementById(`listItem:${currentQuestion}`)
    .classList.add("questionListItemSelected");

  console.log(questions);
}

function setCorrect(num) {
  questions[currentQuestion].correct = num;

  let items = document.getElementsByClassName("optionCheck");
  for (let i = 0; i < items.length; i++) {
    items[i].classList.remove("optionCorrect");
  }

  items[num - 1].classList.add("optionCorrect");
}

function discard() {
  location.reload();
}

async function postQuiz(code) {
  setDueDate();
  await fetch(`/ViewClassroom/quizzes/createQuiz`, {
    method: "POST",
    body: JSON.stringify({
      name: QuizName,
      questions: questions,
      code: code,
      duedate: DueDate,
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

function setName() {
  QuizName = document.getElementById("QuizTitle").value;
}

function setDueDate() {
  DueDate = document.getElementById("assignmentDueDate").value;
}

async function compileResults(numQuestions, code, id) {
  let answers = [];

  for (let i = 0; i < parseInt(numQuestions); i++) {
    option1 = document.getElementById(`option1:${i + 1}`);
    option2 = document.getElementById(`option2:${i + 1}`);
    option3 = document.getElementById(`option3:${i + 1}`);
    option4 = document.getElementById(`option4:${i + 1}`);

    if (option1.checked) {
      answers.push(1);
    } else if (option2.checked) {
      answers.push(2);
    } else if (option3.checked) {
      answers.push(3);
    } else if (option4.checked) {
      answers.push(4);
    } else {
      answers.push(0);
    }
  }

  await fetch(`/ViewClassroom/${code}/quizzes/viewQuiz/${id}/submit`, {
    method: "POST",
    body: JSON.stringify({
      answers: answers,
    }),
    headers: { "X-CSRFToken": getCookie("csrftoken") },
  });

  location.reload();
}

//for student
function seeResults(answers, correctAnswers) {
  answers = JSON.parse(answers);
  correctAnswers = JSON.parse(correctAnswers);
  for (let i = 0; i < answers.length; i++) {
    if (answers[i] == 1) {
      document.getElementById(`option1:${i + 1}`).checked = true;
    } else if (answers[i] == 2) {
      document.getElementById(`option2:${i + 1}`).checked = true;
    } else if (answers[i] == 3) {
      document.getElementById(`option3:${i + 1}`).checked = true;
    } else if (answers[i] == 4) {
      document.getElementById(`option4:${i + 1}`).checked = true;
    }

    document
      .getElementById(`labelOption${correctAnswers[i]}:${i + 1}`)
      .classList.add("greenHighlight");

    if (answers[i] != correctAnswers[i]) {
      document.getElementById(`incorrect:${i + 1}`).hidden = false;
      if (answers[i] >= 1 && answers[i] <= 4) {
        document
          .getElementById(`labelOption${answers[i]}:${i + 1}`)
          .classList.add("redHighlight");
      }
    }

    //id='labelOption1:{{ forloop.counter }}'
  }
}

//for teacher viewing results
function teacherViewQuiz(
  username,
  clickedItem,
  answers,
  correctAnswers,
  index
) {
  document.getElementById("message").hidden = true;
  let submissionDiv = document.getElementById(username);
  toggleHiddenSubmission(username, clickedItem);

  answers = JSON.parse(answers);
  correctAnswers = JSON.parse(correctAnswers);

  answers = answers[index];
  username = username.substring(0, username.indexOf(":"));

  // each element in the results form has an id of the following structure: 'username:{type of element i.e option2}:questionNumber
  for (let i = 0; i < answers.length; i++) {
    if (answers[i] == 1) {
      document.getElementById(`${username}:option1:${i + 1}`).checked = true;
    } else if (answers[i] == 2) {
      document.getElementById(`${username}:option2:${i + 1}`).checked = true;
    } else if (answers[i] == 3) {
      document.getElementById(`${username}:option3:${i + 1}`).checked = true;
    } else if (answers[i] == 4) {
      document.getElementById(`${username}:option4:${i + 1}`).checked = true;
    }

    document
      .getElementById(`${username}:labelOption${correctAnswers[i]}:${i + 1}`)
      .classList.add("greenHighlight");

    if (answers[i] != correctAnswers[i]) {
      document.getElementById(`${username}:incorrect:${i + 1}`).hidden = false;
      if (answers[i] >= 1 && answers[i] <= 4) {
        document
          .getElementById(`${username}:labelOption${answers[i]}:${i + 1}`)
          .classList.add("redHighlight");
      }
    }
  }
}
function toggleHiddenSubmission(id, clickedItem) {
  let infoItems = document.querySelectorAll(".studentSubmissionInfoItem");
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
