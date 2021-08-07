from io import BytesIO
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import FileField, ImageField, ImageFieldFile
from django.utils.timezone import localtime, now
from datetime import datetime
import time
import os
import sys
from django.core.files.base import File
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image


class User(AbstractUser):
    userType = models.CharField(max_length=20, default="student")
    profile_pic = models.ImageField(
        null=True, blank=True, default="blankUserIcon.svg")



class Classroom(models.Model):
    name = models.CharField(max_length=100, default="Classroom")
    students = models.ManyToManyField(User, blank=True)
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="teacher")
    code = models.CharField(max_length=20)
    subject = models.CharField(max_length=50, default="")
    theme = models.CharField(max_length=20, default="cardBlue")


class Comment(models.Model):
    date = models.DateTimeField(default=datetime.now())
    text = CharField(max_length=5000, default="")
    commenter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter", null=True)


class Announcement(models.Model):
    classroom = models.ForeignKey(
        Classroom, on_delete=models.CASCADE, related_name="classroom", null=True)
    body = CharField(max_length=20000, default="")
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="creator", null=True)
    date = models.DateTimeField(default=datetime.now())
    comments = models.ManyToManyField(Comment, blank=True)


class Text(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sender")
    reciever = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reciever")
    date = models.DateTimeField(default=datetime.now())
    text = CharField(max_length=1000, default="")


class Conversation(models.Model):
    user1 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user1")
    user2 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user2")
    texts = models.ManyToManyField(Text, blank=True)
    lastInteracted = models.FloatField()
    readUser1 = models.BooleanField(default=True)
    readUser2 = models.BooleanField(default=True)


class FileModel(models.Model):
    file = models.FileField(blank=True)

    def name(self):
        return os.path.basename(self.file.name)


class Submission(models.Model):
    resubmitted = models.BooleanField(default=False)
    grade = models.IntegerField(default=-1)
    files = models.ManyToManyField(FileModel, blank=True)
    description = models.CharField(max_length=1000, default="")
    user = models.ForeignKey(
        User, null=True, related_name="submitter", on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now())


class Assignment(models.Model):
    givenFiles = models.ManyToManyField(FileModel, blank=True)
    title = models.CharField(max_length=500, default="")
    description = models.CharField(max_length=20000, default="")
    duedate = models.DateTimeField()
    submissions = models.ManyToManyField(Submission, blank=True)
    classroom = models.ForeignKey(
        Classroom, on_delete=models.CASCADE, related_name="belongingToClassroom", null=True)


class MCanswer(models.Model):
    answer = models.IntegerField(default=-1)


class MultipleChoiceQuestion(models.Model):
    question = models.CharField(max_length=1000)
    option1 = models.CharField(max_length=1000)
    option2 = models.CharField(max_length=1000)
    option3 = models.CharField(max_length=1000)
    option4 = models.CharField(max_length=1000)
    correctOption = models.IntegerField(default=1)
    selectedOption = models.IntegerField(default=-1)


class QuizSubmission(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now())
    grade = models.IntegerField(default=0)
    answers = models.ManyToManyField(MCanswer, blank=True)


class Quiz(models.Model):
    name = models.CharField(max_length=1000, default="Untitled Quiz")
    submissions = models.ManyToManyField(QuizSubmission, blank=True)
    questions = models.ManyToManyField(MultipleChoiceQuestion, blank=True)
    duedate = models.DateTimeField(null=True)
    classroom = models.ForeignKey(
        Classroom, null=True, on_delete=models.CASCADE)
