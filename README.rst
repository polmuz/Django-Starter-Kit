==================
Django Starter Kit
==================

This is a skeleton and a guide to add the most common packages to a
Django project. This is inspired by django-party-pack and I'm tired of
doing the same things each time I start a Django project and having to
look up the documentation because I don't remember how to do it.


First of all
============

Virtualenv
----------

Install last version of virtualenv::

  $ sudo pip install virtualenv

Create a virtualenv::

  $ virtualenv --no-site-packages env

Activate the environment::

  $ . env/bin/activate

Install requirements::

  $ pip install -r requirements


Gitignore
---------

(Because you are obviously using git)

Create a `.gitignore` file in the project's root and add the patterns
you don't want to have under version control.

Here are some useful patterns to ignore::

  *.pyc
  env/
  *~
  *.log
  .coverage
  _build
  db.sqlite3

Here is a very usefull list of .gitignore patterns for different
projects https://github.com/github/gitignore

Documentation
=============

From scratch
------------

Run and follow the wizard::

  $ sphinx-quickstart


Compile
-------

Run make and the output format to compile::

  $ cd docs
  $ make html


Configure
---------

To include more files in the main doc, add the names without the
extension under `toctree`::

  .. toctree::p
    :maxdepth: 2

    mydocfile


Docstrings
----------

First of all, go to `docs/conf.py` and uncomment the line
`sys.path.insert(0, os.path.abspath('.'))` and replace the `'.'` with
your django project relative path `../yourproject`. Now you'll be able to generate docs from
your docstrings.

To do this you can create a rst (lets say `yourapp.rst`) file that
looks like this::

   ======================
   Reference for Your App
   ======================

   The yourapp is a really cool app that does magical things.

   ``yourapp.models``
   =================
   .. automodule:: yourapp.models
       :members:

   ``yourapp.views``
   =================
   .. automodule:: yourapp.views
       :members:

   ``yourapp.tests``
   =================
   .. automodule:: yourapp.tests
       :members:
       :undoc-members:

Then you can include something like this in your `index.rst`::

   API/Reference Docs
   --------------------

   .. toctree::
      :maxdepth: 2

      reference_yourapp
