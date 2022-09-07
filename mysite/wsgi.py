"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""


from django.core.wsgi import get_wsgi_application


from whitenoise import WhiteNoise


application = get_wsgi_application()
application = WhiteNoise(application, root="/Users/chrishicks/Desktop/portfolio/staticfiles")
application.add_files("/Users/chrishicks/Desktop/portfolio/portfolio/static/css")