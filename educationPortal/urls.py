from os import stat
from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createNewClassroom/<str:name>/", views.createNewClassroom,
         name="createNewClassroom"),
    path("ViewClassroom/<str:code>/", views.ViewClassroom, name="ViewClassroom"),
    path("JoinClassroom/<str:code>/",
         views.JoinClassroom, name="JoinClassroom"),

    path("makeAnnouncement/", views.makeAnnouncement, name="makeAnnouncement"),
    path("addComment/", views.addComment, name="addComment"),
    path("conversations/",
         views.conversations, name="conversations"),
    path("addConversation/", views.addConversation, name="addConversation"),
    path("sendText/", views.sendText, name="sendText"),
    path("editProfileImage/", views.editProfileImage, name="editProfileImage"),

    # assignmentStuff
    path("ViewClassroom/<str:code>/assignments",
         views.assignments, name="assignments"),
    path("ViewClassroom/<str:code>/assignments/createAssignment",
         views.createAssignment, name="createAssignment"),
    path("ViewClassroom/<str:code>/assignments/viewAssignment/<int:id>",
         views.viewAssignment, name="viewAssignment"),

    path("ViewClassroom/<str:code>/assignments/viewAssignment/<int:id>/submit",
         views.submitAssignment, name="submitAssignment"),
    path("ViewClassroom/<str:code>/assignments/viewAssignment/<int:assignmentId>/<int:id>/grade",
         views.gradeAssignment, name="gradeAssignment"),

    # quiz Stuff
    path("ViewClassroom/<str:code>/quizzes", views.quizzes, name="quizzes"),
    path("ViewClassroom/quizzes/createQuiz",
         views.createQuiz, name="createQuiz"),
    path("ViewClassroom/<str:code>/quizzes/viewQuiz/<int:id>",
         views.viewQuiz, name="viewQuiz"),

    path("ViewClassroom/<str:code>/quizzes/viewQuiz/<int:id>/submit",
         views.submitQuiz, name="submitQuiz"),
]
