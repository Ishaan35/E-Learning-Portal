# Introduction

E-learning Portal is a web application that is meant for providing easy access between students and teachers during online learning. The app has two different types of users. You can register as a teacher, or you could register as a student. If you register as a teacher, you can create classrooms, and inside those classrooms, you can create quizzes, assignments with files, and announcements. If you register as a student, you can join classes with a unique code generated for that class. Students will be able to submit assignments and quizzes, while the teacher can grade the assignments. Quizzes are marked automatically since they are multiple-choice. Students and teachers are both able to post announcements and class comments in the classroom. Class comments are a good way to communicate with other peers in the class, however, not everyone would like to communicate publicly. For this reason, there is also a feature where users can communicate privately with other students or other teachers. In addition to the base functionality of classrooms, assignments, quizzes, and conversations, users can upload profile pictures to customize their profile.

# Files

The files that make up most of the project and I changed the most are inside the **educationPortal** app/folder inside the project directory called **education-app**.

## templates

The templates folder inside the app directory contains the HTML files for the different pages on the website.

The **layout.html** template contains the base HTML code that other templates can extend from.

The next templates are **login.html** and **register.html**. These templates handle users logging in and creating new users respectively. They both have a form that sends a POST request to the **views.py** file when the user registers or signs in.

The **index.html** template is the main page the user arrives at when he/she is logged in. This page displays all of the classes the user is associated with. If the user is a teacher, the user will see all of the classes he/she teaches. If the user is a student, the index.html page will show all the classes that he/she is a part of.

The **ViewClass.html** template is the page that displays a specific classroom. On that page, classroom information, announcements, and class comments will be displayed. The user can create announcements and class comments.

The **assignments.html** and **quizzes.html** templates will show the assignments and quizzes that are part of a specific class respectively. The assignments and quizzes will be shown in a list, and if the signed-in user is the classroom teacher, he/she will be able to create assignments and quizzes from there.

The **ViewAssignments.html** template will show the details of a selected assignment. The user will see details of the assignment, but will also have the option to submit the assignment along with any files if he/she is a student. If the user is a teacher, the user will be able to see the assignment submissions from students in the class and who have not submitted the assignment.

The **ViewQuizzes.html** template will show details of a specific quiz. If the user is a student, the user will be able to start the quiz and submit it when done. Once submitted, the page will show the student the automatically graded result. If the user is a teacher, the user will be able to see the results of everyone in the class.

The **Conversations.html** template will display the page where users can direct message other users on the app. The left panel will show current conversations, while the right panel will display the text messages.

## Python Files

The main python files outside the templates directory I edited were **models.py**, **views.py**, and **urls.py**.

The models.py file has all the models in the app. In this app, there are **13 models**. Each model has a specific purpose. Here is a list of the models: **User, Classroom, Comment** (class comments on announcements), **Announcement, Text, Conversation, FileModel** (stores a file field for assignments), **Submission** (assignment submission), **QuizSubmission, Assignment** (contains details for an assignment), **Quiz** (stores quiz information such as questions), **MultipleChoiceQuestion**, and **mcAnswer** (represents answer for multiple-choice question).

### Views.py functions

The **views.py** has all the functions that handle the different paths on my website and handle the information processing.
The **index** view gets all the classes associated with the signed-in user.

The **login_view** view takes data from the incoming post request and attempts to sign the user in.

The **register** view takes incoming post request data and tries to create a new user.

The **createNewClassroom** view creates a new classroom with a unique code using the data provided from a post request (such as the name of the classroom).

The **JoinClassroom** view allows a user to join a classroom as a student if it received a post request. If it receives a delete request from a teacher, it will delete the classroom with the given code from the delete request.

The **ViewClassroom** view will send information about the classroom, and all the announcements associated with the selected classroom.

The **makeAnnouncent** view will create an announcement with an Announcement model.

The **addComment** view will add a class comment to a given announcement.

The **conversations** view will render the conversations page/template.

The **addConversations** view will create a new conversation between two people.

The **sendText** view will create a text with a receiver and sender. The 'editProfileImage' view will change a user's profile picture.

The **assignments** view will get all the assignments in the current classroom and display them through a template.

The **createAssignment** view will create a new assignment from post request data.

The **submitAssignment** view will allow a student to submit an assignment and create a Submission object.

The **gradeAssignment** view will allow the teacher to grade a student assignment submission.

The **quizzes** view will get all the quizzes in the current classroom and display them through a template.

The **createQuiz** view will create a new quiz from post request data if the user is a teacher.

The **viewQuiz** view will display the information related to the selected quiz and will allow students to write it.

The **submitQuiz** view will allow students to submit a quiz and create a 'quizSubmission' object.

The **urls.py** file has all of the different paths on my website set up. Each path has a view function, name, and URL associated with it.

## Static files

There are also many **static files** I created that are in the static folder inside the **educationPortal** app. These files include **several CSS files**. These CSS files are each associated with a template mentioned above. The CSS files help position and style the HTML content on the webpage. There are also some **icons** and images I used to make the website more visually appealing.
Lastly, some **static JavaScript files** control the front end of the website (templates).

The **assignments.js** file is responsible for allowing the teacher to create a new assignment by listening for click events on different buttons, and then send a POST request to the correct path with the data.

The **Classroom.js** file handles POST requests for making class comments and announcements while controlling the user interface and input fields.

The **conversations.js** file handles UI changes when sending texts to other people as well as making post requests of the texts.

The **index.js** file controls UI changes and post requests when making a new classroom. It also handles the side menu animation when you click on the three bars.

The **quizzes.js** file lets the teacher create quizzes by storing the questions in an array, and making the final post request when creating the quiz. It also lets students make a post request when writing the quiz to submit.

Lastly, the **viewAssignment.js** file changes the UI when the student uploads files to submit and when the teacher wants to see individual submissions from a list of people.

## Static Media Files

I have configured a directory outside the **educationPortal** app, but in the main project directory **education-app**, where uploaded files by users during runtime get saved to. This directory is also called **static/images**. To configure this directory, I had to add the following to the **settings.py** file:

```python
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_URL = '/images/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
```

# How to run:

To run this project, make sure you have a version of **python** that is greater than **3.8** installed on your computer. When you download the project, open the **main parent directory of the entire project** in any text editor with a built-in terminal (such as Visual Studio Code), or open the directory in your computer's terminal/command prompt. Once you have the terminal open at the same directory as the manage.py file, execute

```bash
pip install -r requirements.txt.
```

This will install all the dependencies the project uses. Next, run

```bash
python manage.py runserver
```

in your terminal. This will open a local server in your browser window where you can use this app.

# Distinctiveness and Complexity

I believe this project satisfies the distinctiveness and complexity requirements in the guidelines of the project. This is because this app is neither a social media app nor a social media app. This app is meant to make online learning easier and is very distinct from other projects done in the course. It has several features that social media and finance apps do not implement such as assignment creation, file uploads and downloads during runtime, and quiz creation during runtime. This project satisfies the complexity guidelines as it does not re-use code from previous projects, it has 13 models even though the minimum specified 1 model, and there are several pages a user can visit, each with separate functionality. The project utilizes many javascript files for the front end and many view functions for the python back end. The project is also fully mobile responsive.

This app also implements email functionality. Whenever a user receives a grade on an assignment from the teacher, an email is sent to their email address through Gmail's servers
