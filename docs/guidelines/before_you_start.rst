================
Before you start
================

Some things you should do before you start to code.

Sites
=====

Django comes with a "sites" framework, it's used to handle multiple
similar sites with the same django instalation. See the docs for more
information https://docs.djangoproject.com/en/dev/ref/contrib/sites/

If you don't need this functionality, DEACTIVATE IT!

Go to your settings and comment this line::

    'django.contrib.sessions',
    # 'django.contrib.sites',  # "sites" framework
    'django.contrib.messages',

.. note::
  Let me know if you find a reason not to do this.
