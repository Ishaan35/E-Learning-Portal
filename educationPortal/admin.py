from typing import Text
from django.contrib import admin

from .models import Assignment, Comment, Conversation, FileModel, MCanswer, MultipleChoiceQuestion, Quiz, QuizSubmission, Submission, User, Text, Classroom

# Register your models here.
admin.site.register(User)
admin.site.register(Classroom)
admin.site.register(Conversation)
admin.site.register(Text)
admin.site.register(FileModel)
admin.site.register(Submission)
admin.site.register(Assignment)
admin.site.register(Quiz)
admin.site.register(QuizSubmission)
admin.site.register(MultipleChoiceQuestion)
admin.site.register(MCanswer)
admin.site.register(Comment)
