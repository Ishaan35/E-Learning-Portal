

<!-- PROJECT LOGO -->
<br />
<div align="left">
  <a href="https://e-learning-portal-ishaan.herokuapp.com/" style="display:flex; align-items:center;">
    <img src="https://raw.githubusercontent.com/Ishaan35/E-Learning-Portal/main/Logo.png" alt="Logo" width="80" height="80" style="margin-right:20px">
	<h1>BloodSense</h1>
	</h1>
  </a>


<!-- ABOUT THE PROJECT -->
## About The Project


E-learning Portal is a web application that is meant for providing easy access between students and teachers during online learning. You can register as a teacher, or as a student. If you register as a teacher, you can create classrooms, and inside those classrooms, you can create quizzes, assignments with files, and announcements. If you register as a student, you can join classes with a unique code generated for that class. Students will be able to submit assignments and quizzes, while the teacher can grade the assignments. Quizzes are marked automatically since they are multiple-choice. Students and teachers are both able to post announcements and class comments in the classroom. Class comments are a good way to communicate with other peers in the class, however, not everyone would like to communicate publicly. For this reason, there is also a feature where users can communicate privately with other students or other teachers. In addition to the base functionality of classrooms, assignments, quizzes, and conversations, users can upload profile pictures to customize their profile.

### Built With

* [![Django][Django]][Django-url]
* [![][MySQL]][SQL-url]
* [![Heroku][Heroku]][Heroku-url]
* [![AWS-S3][AWS-S3]][AWS-S3-url]
* [![][Python]][Python-url]
* ![][JavaScript]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Status -->
## Status

This project is currently production-ready [here](https://e-learning-portal-ishaan.herokuapp.com).



## Usage

1. Log in or create a new account.
2. Once logged in, you will be directed to the dashboard. The dashboard will show all the classrooms you are in as a student, or the classrooms you have created as a teacher. The sidebar will contain a link to the private conversations section of the app.
3. Teachers can create a new classroom and share the unique code. Students AND teachers are able to join a classroom made by another teacher.


## Screenshots

##### Dashboard
<img src="https://github.com/Ishaan35/E-Learning-Portal/blob/main/static/images/Dashboard.png?raw=true">
##### Inside Classroom
<img src="https://github.com/Ishaan35/E-Learning-Portal/blob/main/static/images/InsideClassroom.png?raw=true">

##### Assignment Creator
<img src="https://github.com/Ishaan35/E-Learning-Portal/blob/main/static/images/Assignment%20Creator.png?raw=true">

##### Quiz Creator
<img src="https://github.com/Ishaan35/E-Learning-Portal/blob/main/static/images/Quiz%20Creator.png?raw=true">

##### Viewing Past Assignments
<img src="https://github.com/Ishaan35/E-Learning-Portal/blob/main/static/images/Assignment%20List.png?raw=true">

##### Conversations
<img src="https://github.com/Ishaan35/E-Learning-Portal/blob/main/static/images/Conversations.png?raw=true">


<!-- ROADMAP -->
## Roadmap

- [ ] Add sub-profiles
- [ ] Add custom notes feature for every record
- [ ] Appointment booking reminder

## How to run:

To run this project, make sure you have a version of **python** that is greater than **3.8** installed on your computer. When you download the project, open the **main parent directory of the entire project** in any text editor with a built-in terminal (such as Visual Studio Code), or open the directory in your computer's terminal/command prompt. Once you have the terminal open at the same directory as the manage.py file, execute

```bash
pip install -r requirements.txt.
```

This will install all the dependencies the project uses. Next, run

```bash
python manage.py runserver
```

in your terminal. This will open a local server in your browser window where you can use this app.





<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.




<!-- CONTACT -->
## Contact

Ishaan Patel  -  toishaanpatel@gmail.com

LinkedIn:  https://www.linkedin.com/in/ishaan35/

Personal Website: https://www.ishaanpatel.info/

Project Link: https://app.bloodsense.online








<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png


[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Express.js]: https://img.shields.io/badge/Express.js-35495E?style=for-the-badge&logo=express
[Express-url]: https://expressjs.com/
[Passport.js]:https://img.shields.io/badge/Passport.js-4a4a55?style=for-the-badge&logo=passport
[Passport-url]:https://www.passportjs.org/
[MySQL]:https://img.shields.io/badge/MySQL-ccd4ed?style=for-the-badge&logo=mysql&logoColor=910000
[SQL-url]:https://www.mysql.com/
[Google Cloud]: https://img.shields.io/badge/Google%20Cloud-5c5866?style=for-the-badge&logo=google-cloud
[GoogleCloud-url]: https://cloud.google.com/
[Microsoft Azure]: https://img.shields.io/badge/Microsoft%20Azure-343440?style=for-the-badge&logo=microsoft-azure&logoColor=42adff
[Azure-url]: https://azure.microsoft.com/en-us/
[Vercel]:https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=ffffff
[Vercel-url]:https://vercel.com/dashboard
[Render]:https://img.shields.io/badge/Render-4351e8?style=for-the-badge&logo=render&logoColor=ffffff
[Render-url]:https://render.com/
[NameCheap]:https://img.shields.io/badge/NameCheap-ff8c44?style=for-the-badge&logo=namecheap&logoColor=ffffff
[Namecheap-url]:https://www.namecheap.com/domains/

[Django]:https://img.shields.io/badge/Django-103e2e?style=for-the-badge&logo=django&logoColor=ffffff
[Django-url]:https://www.djangoproject.com/
[Heroku]:https://img.shields.io/badge/Heroku-6c67a9?style=for-the-badge&logo=heroku&logoColor=ffffff
[Heroku-url]:https://www.heroku.com/
[AWS-S3]:https://img.shields.io/badge/AWS%20S3-222e3d?style=for-the-badge&logo=amazon-s3&logoColor=f79400
[AWS-S3-url]:https://aws.amazon.com/s3/
[Python]:https://img.shields.io/badge/Python-112a45?style=for-the-badge&logo=python&logoColor=ffc537
[Python-url]:https://www.python.org/
[JavaScript]: https://img.shields.io/badge/JavaScript-141529?style=for-the-badge&logo=JavaScript&logoColor=ffc537
