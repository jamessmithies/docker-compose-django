Docker Compose project base with Django, Nginx, Gunicorn, Postgres and Redis. Based on https://www.capside.com/labs/deploying-full-django-stack-with-docker-compose/.

To use:

1] Install Docker and Docker Compose.

2] Edit 'env' and '/web/projectfiles/settings/secrets.py' as required (and uncomment them in .gitignore).

3] If you are using an external server, add your IP and/or domain name to ALLOWED_HOSTS in 'docker-compose-django/web/projectfiles/settings/based.py'

4] cd to directory containing docker-compose.yml, then 'docker-compose build' and 'docker-compose up -d'.

The Django 'It Worked!' page should be available at 127.0.0.1.


