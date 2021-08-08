# Generated by Django 3.2.5 on 2021-08-08 00:08

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('userType', models.CharField(default='student', max_length=20)),
                ('profile_pic', models.ImageField(blank=True, default='blankUserIcon.svg', null=True, upload_to='')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Classroom', max_length=100)),
                ('code', models.CharField(max_length=20)),
                ('subject', models.CharField(default='', max_length=50)),
                ('theme', models.CharField(default='cardBlue', max_length=20)),
                ('students', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='MCanswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='MultipleChoiceQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('option1', models.CharField(max_length=1000)),
                ('option2', models.CharField(max_length=1000)),
                ('option3', models.CharField(max_length=1000)),
                ('option4', models.CharField(max_length=1000)),
                ('correctOption', models.IntegerField(default=1)),
                ('selectedOption', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 8, 7, 20, 8, 17, 877306))),
                ('text', models.CharField(default='', max_length=1000)),
                ('reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reciever', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resubmitted', models.BooleanField(default=False)),
                ('grade', models.IntegerField(default=-1)),
                ('description', models.CharField(default='', max_length=1000)),
                ('date', models.DateField(default=datetime.datetime(2021, 8, 7, 20, 8, 17, 879300))),
                ('files', models.ManyToManyField(blank=True, to='educationPortal.FileModel')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='submitter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuizSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime(2021, 8, 7, 20, 8, 17, 881295))),
                ('grade', models.IntegerField(default=0)),
                ('answers', models.ManyToManyField(blank=True, to='educationPortal.MCanswer')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Untitled Quiz', max_length=1000)),
                ('duedate', models.DateTimeField(null=True)),
                ('classroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='educationPortal.classroom')),
                ('questions', models.ManyToManyField(blank=True, to='educationPortal.MultipleChoiceQuestion')),
                ('submissions', models.ManyToManyField(blank=True, to='educationPortal.QuizSubmission')),
            ],
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastInteracted', models.IntegerField(default=-1)),
                ('readUser1', models.BooleanField(default=True)),
                ('readUser2', models.BooleanField(default=True)),
                ('texts', models.ManyToManyField(blank=True, to='educationPortal.Text')),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 8, 7, 20, 8, 17, 876308))),
                ('text', models.CharField(default='', max_length=5000)),
                ('commenter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=500)),
                ('description', models.CharField(default='', max_length=20000)),
                ('duedate', models.DateTimeField()),
                ('classroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='belongingToClassroom', to='educationPortal.classroom')),
                ('givenFiles', models.ManyToManyField(blank=True, to='educationPortal.FileModel')),
                ('submissions', models.ManyToManyField(blank=True, to='educationPortal.Submission')),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(default='', max_length=20000)),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 8, 7, 20, 8, 17, 876308))),
                ('classroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classroom', to='educationPortal.classroom')),
                ('comments', models.ManyToManyField(blank=True, to='educationPortal.Comment')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
