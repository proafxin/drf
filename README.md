# ReST API Using Django Rest Framework (DRF) and Testing

This is a tutorial project that demonstrates how to use DRF to create ReSTful APIs. You can use the `requirements.txt` file to install all dependencies with `pip install -r requirements.txt`

Go to your root project directory where you want to run this project and clone this repo. From the root directory, run typical django commands `python manage.py makemigrations` and `python manage.py migrate` which should generate the necessary sqlite database. Then you can test the API endpoints (unit test, integration test and functional test are all included) using the command `python manage.py test`

A few notes
* The project was created with `django-admin startproject tutorial .` instead of the typical `django-admin startproject tutorial` which creates unnecessary directories inside directories.
* The test module was divided into different modules instead of using it as a single module `tests.py`
