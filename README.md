# File-Management-System
Python Django and React based File Management System , RESTful API
file upload REST API


# Setup Instructions

git clone https://github.com/amplify-tech/File-Management-System.git
cd File-Management-System



2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate


3. Install Dependencies
pip install -r requirements.txt


4. Run Migrations
python manage.py makemigrations
python manage.py migrate

6. Run Server
python manage.py runserver

open in browser: http://localhost:8000/api/