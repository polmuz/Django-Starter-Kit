===================
Django Registration
===================

Setup
=====

Install
-------

We'll use the last version of django-registration that is not on PyPI
yet, but comes with many improvements and it's stable even if it says
it's alpha.

You can install it directly from BitBucket::

  $ pip install https://bitbucket.org/ubernostrum/django-registration/downloads/django-registration-0.8-alpha-1.tar.gz

Settings
--------

Add django-registration to `INSTALLED_APPS`::

  INSTALLED_APPS = (
      'django.contrib.auth',
      'django.contrib.sites',
      'registration',  # django-registration
  )

  ACCOUNT_ACTIVATION_DAYS = 7

Update the database::

  $ python manage.py syncdb

URLs
----

Add django-registration to your urls::

  (r'^accounts/', include('registration.backends.default.urls')),
