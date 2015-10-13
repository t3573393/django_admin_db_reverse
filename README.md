# django_admin_db_reverse

reverse the db schema to the django models.py and admin.py
now just support the mysql database.
it composes of these step:
1. get the db schema data
2. translate the schema info the django model info
3. generate code by the django template engine
4. compress to zip and download the last result 


requires :
Django >= 1.8.4

may be work on the old version:

# project info
username: root
password: root