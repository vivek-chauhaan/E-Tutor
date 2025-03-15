# Teachers and Students Management System

## Project Overview  
This is a **Teachers and Students Management System** built using **Python, Django, and MySQL**. The system provides an efficient way to manage teachers, students, courses, and academic records. It includes an **admin panel** for easy management and ensures seamless interaction between students and teachers.  

## Features  
- **Admin Panel**: Manage students, teachers, courses, and class schedules.  
- **Teacher Module**: View assigned classes, manage student records and attendance.  
- **Student Module**: Access courses, assignments, grades, and attendance reports.  
- **Authentication**: Secure login system for admins, teachers, and students.  
- **Database Management**: MySQL integration for efficient data handling.  

## Technologies Used  
- **Backend**: Python, Django  
- **Database**: MySQL  
- **Frontend**: HTML, CSS, JavaScript (if applicable)  

## Installation Guide  

### Prerequisites  
Ensure you have the following installed on your system:  
- Python (>= 3.8)  
- MySQL  
- pip (Python package manager)  
- virtualenv (optional but recommended)  

### Steps to Set Up Locally  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
**DataBse**

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
<h4>Apply migrations</h4>
python manage.py migrate

Create a superuser for admin access
python manage.py createsuperuser
