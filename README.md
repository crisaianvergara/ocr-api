## Create virtual environment
py -3.11 -m venv .venv
.venv\Scripts\activate
pip install django
pip install django_rest_framework
django-admin startproject ocrapi .
django-admin startapp apis
django-admin startapp users

## Setup Django, DRF, MySQL
pip install black
pip install mysqlclient
pip install djangorestframework-simplejwt
pip install django-cors-headers

## Install docTR
pip install "python-doctr[tf]"
pip install rapidfuzz==2.13.7
pip install nltk

## Modify settings.py

## Create users.py files in-order
1. managers.py
2. models.py
3. forms.py
4. admin.py
5. serializers.py
6. views.py
7. urls.py

** Modify urls.py

pip freeze > requirements.txt
python.exe -m pip install --upgrade pip
