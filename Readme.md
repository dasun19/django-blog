
Index No: 20APP5021
Name: P.L.D.K.Cooray
Git repository: https://github.com/dasun19/django-blog.git


Django Project
==============

This is a Django web application. Follow the steps below to set up and run the project on your local machine.

Prerequisites
-------------
Ensure you have the following installed on your system:
- Python (>=3.x)
- pip (Python package manager)
- virtualenv (Optional but recommended)

Setup Instructions
------------------

1. Clone the Repository
-----------------------
git clone https://github.com/dasun19/django-blog.git
cd django-blog

2. Create and Activate Virtual Environment
------------------------------------------

Windows (Command Prompt):
python -m venv venv
venv\Scripts\activate

macOS / Linux (Terminal):
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
-----------------------
Run the following command to install all required packages:
pip install -r requirements.txt

4. Apply Migrations
-------------------
python manage.py migrate

5. Create a Superuser (Optional)
--------------------------------
python manage.py createsuperuser

Follow the prompts to set up an admin user.

6. Run the Development Server
-----------------------------
python manage.py runserver

The application should now be running at:
http://127.0.0.1:8000/

Environment Variables
---------------------
If your project uses .env files, create one in the root directory:

DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url

You may need to install python-dotenv if your project relies on environment variables:

pip install python-dotenv

Additional Commands
-------------------
Run tests:
python manage.py test

Check for missing migrations:
python manage.py makemigrations --dry-run

Notes:
------
- If you face issues with the virtual environment, try deleting it and recreating it:
  rm -rf venv  # Linux/macOS
  rmdir /s /q venv  # Windows
  python -m venv venv

- Make sure you activate the virtual environment before running any commands.


