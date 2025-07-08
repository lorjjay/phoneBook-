# 📱 PhoneBook – Contact Management Web App

PhoneBook is a Django-based web application that allows users to securely manage their personal contacts. It supports user authentication and provides full CRUD functionality to create, view, update, and delete contacts. The project also features a clean and responsive UI using Bootstrap 5.

---

## 🚀 Features

- ✅ User registration and login
- 📇 Add, edit, delete, and view contacts
- 🔒 Authentication and session handling
- 🎨 Clean UI using Bootstrap 5
- 📂 Organized structure with Django best practices

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: Html, Css, Javascript
- **Database**: SQLite (development) / PostgreSQL (optional for production)
- **Authentication**: Django built-in auth
- **Environment Management**: `python-dotenv`
- **Version Control**: Git + GitHub

---

## 📁 Project Structure
django-learning/
├── MainProject/ # Django settings and root config
│ ├── settings.py
│ └── urls.py
├── PhoneBook/ # Main app with views and models
├── static/ # Static files (CSS, JS)
├── templates/ # HTML templates
├── manage.py
├── requirements.txt
└── .env # Secret environment variables (not pushed)


---

## ⚙️ Setup Instructions

### 🔧 Prerequisites

- Python 3.8+
- Git
- Virtualenv

### Follow the following procedures for Local Development Setup  ###

1. **Clone the repository**
   '''terminal
   git clone https://github.com/Canopus-Tz/phonebook-django.git
   cd phonebook-django

2. **Create and activate virtual environment**
     '''terminal
    python -m venv venv
    venv\Scripts\activate   # Windows

3. **Install dependencies**
    pip install -r requirements.txt

4. **Create .env file**
    SECRET_KEY= PhoneBook_Type_Of_Shit
    DEBUG=True
    ALLOWED_HOSTS=127.0.0.1,localhost

5. **Apply migrations**
     python manage.py migrate

6. **Run the server**
     python manage.py runserver

7. **Visit http://127.0.0.1:8000 in your browser**

   



