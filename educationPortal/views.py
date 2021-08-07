from datetime import date, datetime, time
import educationPortal
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import AllowAllUsersModelBackend
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse
import json
from .models import Assignment, Comment, Conversation, FileModel, MCanswer, MultipleChoiceQuestion, Quiz, QuizSubmission, Submission, User, Classroom, Announcement, Text
from django.shortcuts import redirect
import uuid
import sys
from django.db.models import Q
import time
from django.core.mail import send_mail
from django.core import serializers
import boto3
import os


def index(request):
    if request.user.is_authenticated:

        import os
        is_prod = os.environ.get('IS_HEROKU', None)
        print(is_prod)

        conversations = Conversation.objects.filter(
            Q(user1=request.user, readUser1=False) | Q(user2=request.user, readUser2=False))

        if request.user.userType.lower() == "teacher":
            allClasses = Classroom.objects.all().filter(teacher=request.user)
            return render(request, "educationPortal/index.html", {
                "classes": allClasses,
                "user": request.user,
                "newMail": (conversations.count()) > 0
            })
        if request.user.userType.lower() == "student":
            allClasses = Classroom.objects.filter(students=request.user)
            print(allClasses)
            return render(request, "educationPortal/index.html", {
                "classes": allClasses,
                "user": request.user,
                "newMail": (conversations.count()) > 0
            })

    else:
        return login_view(request)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "educationPortal/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "educationPortal/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]

        userType = request.POST["userType"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "educationPortal/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = firstname
            user.last_name = lastname
            user.userType = userType
            user.profile_pic = request.FILES.get('img')
            user.save()
        except IntegrityError:
            return render(request, "educationPortal/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "educationPortal/register.html")


def createNewClassroom(request, name):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data["name"]

        classroom = Classroom()
        classroom.name = name
        classroom.teacher = request.user
        classroom.theme = data["theme"]
        classroom.subject = data["subject"]

        allclasses = Classroom.objects.all()
        code = uuid.uuid4().hex[:8].upper()
        unique = True
        for c in allclasses:
            if c.code == code:
                unique = False

        # checking for uniqueness of code
        while unique == False:
            code = uuid.uuid4().hex[:8].upper()
            for c in allclasses:
                if c.code == code:
                    unique = False

        classroom.code = code
        classroom.save()

    elif request.method == "DELETE":
        data = json.loads(request.body)
        id = data["id"]
        allclasses = Classroom.objects.filter(id=id).delete()

    return HttpResponse()


def JoinClassroom(request, code):
    if request.method == "GET":

        set = Classroom.objects.all().values_list('code', flat=True)
        codes = []
        for s in set:
            codes.append(s)

        return JsonResponse({
            'codes': codes
        })

    if request.method == "PUT":
        data = json.loads(request.body)
        code = data["code"]

        classroom = Classroom.objects.get(code=code)
        classroom.students.add(request.user)
        classroom.save()
        print('hey')
        return render(request, "educationPortal/ViewClassroom.html", {
            "class": classroom
        })

    if request.method == "DELETE":
        data = json.loads(request.body)
        code = data["code"]

        classroom = Classroom.objects.get(code=code)
        classroom.students.remove(request.user)
        classroom.save()

        return render(request, "educationPortal/ViewClassroom.html", {
            "class": classroom
        })


def ViewClassroom(request, code):
    if request.user.is_authenticated:
        selectedClass = Classroom.objects.get(code=code)

        announcements = Announcement.objects.filter(
            classroom=selectedClass).order_by('-date')

        return render(request, "educationPortal/ViewClassroom.html", {
            "class": selectedClass,
            "announcements": announcements
        })
    else:
        return login_view(request)


def makeAnnouncement(request):

    if request.method == "POST":
        data = json.loads(request.body)
        print()

        announcement = Announcement()
        announcement.body = data["body"]
        announcement.creator = request.user
        announcement.date = datetime.now()
        announcement.classroom = Classroom.objects.get(code=data["code"])

        announcement.save()

    return HttpResponse()


def addComment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data["text"])
        print(data["id"])

        comment = Comment()
        comment.commenter = request.user
        comment.text = data["text"]
        comment.date = datetime.now()
        comment.save()

        announcement = Announcement.objects.get(id=data["id"])
        announcement.comments.add(comment)
        announcement.save()

    return HttpResponse()


def conversations(request):
    if request.user.is_authenticated:
        convos = (Conversation.objects.filter(
            Q(user1=request.user) | Q(user2=request.user))).order_by('-lastInteracted')

        print(convos)
        return render(request, "educationPortal/conversations.html", {
            "students": User.objects.all().exclude(id=request.user.id),
            "conversations": convos
        })
    else:
        return login_view(request)


def addConversation(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data["username"]
        to = User.objects.get(username=username)

        if not Conversation.objects.filter(user1=request.user, user2=to).exists() and not Conversation.objects.filter(user1=to, user2=request.user).exists():
            conversation = Conversation()
            conversation.user1 = request.user
            conversation.user2 = to
            conversation.lastInteracted = time.time()
            conversation.save()

    if request.method == "DELETE":
        data = json.loads(request.body)
        id = data["id"]
        Conversation.objects.get(id=id).delete()

    return HttpResponse()


def sendText(request):
    if request.method == "POST":
        data = json.loads(request.body)

        id = data["id"]
        sender = request.user
        text = data["text"]
        reciever = None
        conversation = Conversation.objects.get(id=id)
        if sender == conversation.user1:
            reciever = conversation.user2
        else:
            reciever = conversation.user1

        newText = Text()
        newText.sender = sender
        newText.reciever = reciever
        newText.date = datetime.now()
        newText.text = text

        newText.save()
        conversation.texts.add(newText)
        conversation.lastInteracted = time.time()
        conversation.save()

        if conversation.user1 == request.user:
            conversation.readUser2 = False
            conversation.readUser1 = True
        elif conversation.user2 == request.user:
            conversation.readUser1 = False
            conversation.readUser2 = True

        conversation.save()

    return HttpResponse()


def editProfileImage(request):
    if request.method == "POST":
        user = request.user
        # print(request.__dict__, file=sys.stderr)
        user.profile_pic.delete()
        user.profile_pic = request.FILES.get('img')
        user.save()
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)


def assignments(request, code):
    classroom = Classroom.objects.get(code=code)
    assignments = Assignment.objects.filter(classroom=classroom)
    return render(request, "educationPortal/assignments.html", {
        "class": classroom,
        "date":  datetime.now(),
        "assignments": assignments
    })


def createAssignment(request, code):

    classroom = Classroom.objects.get(code=code)
    if request.method == "POST":

        assignment = Assignment()
        assignment.title = request.POST["title"]
        assignment.description = request.POST["instructions"]
        assignment.classroom = classroom
        assignment.duedate = request.POST["assignmentDueDate"]
        assignment.save()

        for f in request.FILES.getlist('files'):
            file = FileModel()
            file.file = f
            file.save()
            assignment.givenFiles.add(file)

        assignment.save()

    return render(request, "educationPortal/assignments.html", {
        "class": classroom,
        "defaultDate":  datetime.now(),
        "assignments": Assignment.objects.filter(classroom=classroom)
    })


def viewAssignment(request, code, id):
    classroom = Classroom.objects.get(code=code)
    assignment = Assignment.objects.get(id=id)

    submission = None
    if(assignment.submissions.filter(user=request.user).exists()):  # for student
        submission = assignment.submissions.get(user=request.user)

    allSubmissions = assignment.submissions.all()  # all submissions
    allUserNamesSubmitted = assignment.submissions.values(
        'user__username')  # all usersnames who have submitted

    non_submitters = classroom.students.exclude(
        username__in=allUserNamesSubmitted)  # students who haven't submitted

    return render(request, "educationPortal/viewAssignment.html", {
        "class": classroom,
        "assignment": assignment,
        "submission": submission,  # one student submission (for student)
        "allSubmissions": allSubmissions,  # for teacher
        "non_submitters": non_submitters,  # for teacher
        "overdue": datetime.now().replace(tzinfo=None) > (assignment.duedate).replace(tzinfo=None)
    })


def submitAssignment(request, code, id):

    assignment = Assignment.objects.get(id=id)

    if request.method == "POST":

        if not assignment.submissions.filter(user=request.user).exists():
            submission = Submission()
            submission.description = request.POST["description"]
            submission.user = request.user
            submission.date = datetime.now()
            submission.save()

            for f in request.FILES.getlist('files'):
                file = FileModel()
                file.file = f
                file.save()
                submission.files.add(file)

            submission.save()
            assignment.submissions.add(submission)
            assignment.save()

        else:
            submission = assignment.submissions.get(user=request.user)
            submission.description = request.POST["description"]
            submission.user = request.user
            submission.date = datetime.now()
            submission.files.clear()
            submission.resubmitted = True
            submission.save()

            for f in request.FILES.getlist('files'):
                file = FileModel()
                file.file = f
                file.save()
                submission.files.add(file)

            submission.save()

    return viewAssignment(request, code, id)


def gradeAssignment(request, code, assignmentId, id):

    submission = Submission.objects.get(id=id)
    assignment = Assignment.objects.get(id=assignmentId)
    submitter = submission.user
    if request.method == "POST":
        submission.grade = request.POST["grade"]
        submission.save()

        # send email to user's email address
        subject = "E-learning Classroom: " + \
            str(assignment.title) + " - Score Recieved: "
        message = "Hello " + request.user.first_name + \
            ", Your score for this assignment is " + \
            str(submission.grade) + " / 100"
        send_mail(
            subject,  # subject
            message,  # message
            'e.learningportal.0@gmail.com',  # from email
            [submitter.email],  # to email
        )

    return viewAssignment(request, code, assignmentId)


def quizzes(request, code):
    classroom = Classroom.objects.get(code=code)
    quizzes = Quiz.objects.filter(classroom=classroom)

    return render(request, "educationPortal/quizzes.html", {
        "class": classroom,
        "quizzes": quizzes,
        "date": datetime.now()
    })


def createQuiz(request):
    if request.method == "POST":
        data = json.loads(request.body)
        classroom = Classroom.objects.get(code=data["code"])

        print(data)
        name = data['name']
        questions = data['questions']

        quiz = Quiz()
        quiz.name = name
        quiz.classroom = classroom
        quiz.duedate = data['duedate']
        quiz.save()

        for q in questions:
            mc = MultipleChoiceQuestion()
            mc.question = q['question']
            mc.option1 = q['option1']
            mc.option2 = q['option2']
            mc.option3 = q['option3']
            mc.option4 = q['option4']
            mc.correctOption = int(q['correct'])
            mc.save()
            quiz.questions.add(mc)
        quiz.save()

    return HttpResponse()


def viewQuiz(request, code, id):
    classroom = Classroom.objects.get(code=code)
    quiz = Quiz.objects.get(id=id)

    allSubmissions = quiz.submissions.all()

    allUserNamesSubmitted = quiz.submissions.values(
        'user__username')  # all usersnames who have submitted
    non_submitters = classroom.students.exclude(
        username__in=allUserNamesSubmitted)  # students who haven't submitted

    # array of student answer arrays
    answersArray = []
    for sub in allSubmissions:
        answersArray.append(list(sub.answers.values_list('answer', flat=True)))

    print(answersArray)

    # will be used for the student to see his/her result and grade
    submission = quiz.submissions.get(user=request.user) if quiz.submissions.filter(
        user=request.user).exists() else None

    answers = None
    correctanswers = None
    correctanswers = list(
        quiz.questions.values_list('correctOption', flat=True))
    if submission:
        answers = list(submission.answers.values_list('answer', flat=True))

    return render(request, "educationPortal/ViewQuiz.html", {
        "class": classroom,
        "quiz": quiz,
        "submission": submission,
        "allSubmissions": allSubmissions,  # teacher stuff
        "non_submitters": non_submitters,  # teacher stuff
        "answers": answers,
        "correctanswers": correctanswers,  # teacher and student stuff
        "answersArray": answersArray

    })


def submitQuiz(request, code, id):
    if request.method == "POST":
        quiz = Quiz.objects.get(id=id)

        data = json.loads(request.body)
        answers = data["answers"]

        correct = 0

        s = QuizSubmission()
        s.date = datetime.now()
        s.save()

        # form multiple choice questions from this array. This array is an array of numbers representing the selected option per question.
        questions = quiz.questions.all()
        for i in range(len(questions)):
            m = MCanswer()
            m.answer = answers[i]
            m.save()
            s.answers.add(m)

            if answers[i] == questions[i].correctOption:
                correct = correct + 1

        s.grade = correct
        s.user = request.user
        s.save()
        quiz.submissions.add(s)
        quiz.save()

    return viewQuiz(request, code, id)
