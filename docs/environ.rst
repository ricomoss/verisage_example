=================
Environment Setup
=================

This guide will help you set up your development environment in order to start
working on the project.

Linux Installation (Ubuntu/Debian)
==================================

By following these steps, you can easily have a working installation of the
the website development environment.

.. note::

   The following will assume you are cloning the the website sourcecode to
   **~/projects/<project_name>**.  If you are cloning to a different
   location, you will need to adjust these instructions accordingly.

.. note::

   A dollar sign ($) indicates a terminal prompt, as your user, not root.

1.  Clone the source and create a remote for your fork.::

        $ cd ~/projects
        $ git clone git@github.com:ricomoss/verisage_example.git
        $ git remote add <your_name> git@github.com:<your_github_username>/verisage_example.git

2.  Install some required packages::

        $ sudo apt-get install python3 python3-dev python-pip build-essential postgresql postgresql-contrib libpq-dev

3.  Install virtualenv and virtualenvwrapper::

        $ sudo pip install virtualenv
        $ sudo pip install virtualenvwrapper

4.  Add the following to the end of your **~/.bashrc** file (or **~/.zshrc**)::

        source /usr/local/bin/virtualenvwrapper.sh

5.  Type the following::

        $ source /usr/local/bin/virtualenvwrapper.sh

6.  Create your project virtualenv and deactivate it::

        $ mkvirtualenv verisage -p /usr/bin/python3
        $ deactivate

7.  Add the following to the end of the file
    **~/.virtualenvs/<virtual_env_name>/bin/postactivate**::

        export DJANGO_SETTINGS_MODULE=verisage_example.settings
        export PYTHONPATH=~/projects/verisage_example/verisage_example

8.  Activate the virtualenv::

        $ workon verisage

9.  Install the required python libraries::

        (verisage)$ pip install -r ~/projects/verisage_example/requirements.pip


10. Run the Django tests::

        $ ~/project/verisage_example/verisage_example/manage.py test
