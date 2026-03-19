# NGO Management Platform

A Django-based web application designed to help non-governmental organizations manage members, charity initiatives, donations, and internal communication through a centralized platform.

The system was originally developed for the NGO **Unique Group of Mankind** and used in production to manage member registrations, charity alerts, and donation tracking.

This repository contains a **sanitized development version** of the platform. Sensitive credentials, production infrastructure, and real user data have been removed.

---

# Features

### Member Management

* Member registration and profile management
* Email-based authentication with a custom Django user model
* Role-based access for officials and normal members
* Identity verification with document uploads

### Charity & Donation System

* Charity alert generation for members
* Donation tracking and verification
* Integration with Razorpay payment gateway
* Transaction ID verification workflow

### Media & Activity Management

* NGO event and activity posts
* Image and video gallery management
* Media uploads with validation

### Administration & Communication

* Notice system for announcements
* Charity alerts for donation campaigns
* Admin-controlled management of members and alerts

---

# Tech Stack

**Backend**

* Python
* Django

**Database**

* SQLite (development version)
* PostgreSQL (Production version)

**Authentication**

* Custom Django User Model
* Email-based login

**Payments**

* Razorpay Payment Gateway Integration

**Media Handling**

* Django Media File Management

**Email Service**

* SMTP (Gmail)

---

# Project Structure

```
ngo-management-platform
│
├── ugmt/                 # Main Django project settings
├── userLogin/            # Custom authentication & models
├── templates/            # HTML templates
├── static/               # Static assets (CSS, JS, images)
├── media/                # Uploaded files (ignored in Git)
│
├── manage.py
├── requirements.txt
└── README.md
```

---

# Local Setup

### 1. Clone the Repository

### 2. Create Virtual Environment

### 3. Install Dependencies

### 4. Run Database Migrations

```
python manage.py migrate
```

This will automatically create the development database.

### 5. Create Admin User

```
python manage.py createsuperuser
```

### 6. Run the Development Server
---

# Important Notes

* This repository is a **development/demo version** of the original platform.
* Production credentials, payment keys, and sensitive data have been removed.
* Uploaded media files are not included for privacy reasons.

---


# License

This project is provided for **educational and demonstration purposes**.
