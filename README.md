# Student Management System

This is a student management system built using **Django 4**, **HTML 5**, **CSS 3**, and **Bootstrap 5**.

<img width="964" alt="ScreenShots of the system" src="https://github.com/iamawmrit/student-manegement-system-with-CRUD-operations/blob/master/assets/sc.png">

## Table of Contents 
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Run the application](#run-the-application)
- [View the application](#view-the-application)


## Prerequisites

Install the following prerequisites:

1. [Python 3.10.4 or higher](https://www.python.org/downloads/)
2. [Visual Studio Code](https://code.visualstudio.com/download)


## Installation

### 1. Create a virtual environment

From the **root** directory run:

```bash
python -m venv venv
```

### 2. Activate the virtual environment

From the **root** directory run:

On macOS:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\scripts\activate
```

### 3. Install required dependencies

From the **root** directory run:

```bash
pip install -r requirements.txt
```

### 4. Run migrations

From the **root** directory run:

```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

### 5. Create an admin user to access the Django Admin interface

From the **root** directory run:

```bash
python manage.py createsuperuser
```

When prompted, enter a username, email, and password.

## Run the application

From the **root** directory run:

```bash
python manage.py runserver
```

## View the application

Go to http://127.0.0.1:8000/ to view the application.


## Credits:
Bob's Programming Academy
