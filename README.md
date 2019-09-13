# TITLE: Pitch

## Built By HUDSON HUKISH


## Description
Perfect Pitch is an application that allows you to Post a pitch based on various categories.You can view other pitches as long as you have an account

You can view the site at:

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:
* i would like to sign to an account
* add a pitch
* comment in a pitch
* create a profile

## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display Welcome Message | **On page load** | Select between Add a pitch and View Pitch|
| Display Pitch Form | **Click add pitch** | Redirected to a page where He types the title and content and then selects the category from the drop-down arrow|
| Display the Pitch| **Click view pitch** | Each pitch displays  title, description and category|



## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* virtualenv

## Running the Application
* Creating the virtual environment

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Flask and other Modules

        $ python3.6 -m pip install Flask
        $ python3.6 -m pip install Flask-Bootstrap
        $ python3.6 -m pip install Flask-Font-Mail
        $ python3.6 -m pip install Flask-upload
        $ python3.6 -m pip install Flask-login
        $ python3.6 -m pip install Flask-Alchemy
        $ python3.6 -m pip install Flask-Simplemde



* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

## Technologies Used
        * Python3.6
        * Flask
