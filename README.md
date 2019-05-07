UserDetails Django Application, This Application uses mongodb for database


Building
=========

Requirements:
======================
python 3.6

1.Install requirements.txt
===================
$ pip install -r requirements.txt

2.see the .env file and set the logpath, logpath is required for this application to maintain errors and information.
======

3. make sure you have mongodb and mongodb should be start on your localhost, 
We can change database credentials(username, password, database name, host, port).
According database credentials we can set db parameter in settings.py file.
This application uses only local host and mongodb default port 27017.


4.Run migrate command to interection with database
=
$ python manage.py migrate UserDetailsApp

5.Run Application
=
$ python manage.py runserver

6.Hit url from any rest client(Postman, Restlet Client , etc)
=


Django TestCase:
=================
Django uses Unittest cases of python


Run TestCase:
==============
go to in current working dir
$./manage.py test
I wrote three test cases like wise we can write more such cases of an dajngo application

Master git repository:
======================
https://github.com/rahulbaliyan/UserService

Licensing
========
*****