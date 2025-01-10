# **Task Management System**

## **Introduction**

The **Task Management System** is a web application built using **Django**. It allows users to manage tasks, assign roles, and track progress. This project provides a basic interface for creating, viewing, and editing tasks, with user authentication and role-based permissions.

---

## **Installation and Setup**

Follow the steps below to get the project up and running on your local machine.

### **1. Clone the Repository**

Start by cloning the repository to your local machine. Open a terminal and run the following command:

```bash
git clone https://github.com/your-username/task-management-system.git
```

### **2. Navigate to the Project Directory**
Once the repository is cloned, navigate to the project directory:
```bash
cd TMS/
```

### **3. Set Up a Virtual Environment**
Create a virtual environment to manage the project's dependencies:
```bash
python -m venv .venv
```
### **4. Activate the virtual environment**
**On Windows:**
```bash
.\.venv\Scripts\activate
```
**On macOS/Linux:**
```bash
source .venv/bin/activate
```

### **5. Install Project Dependencies**
Install all the necessary project dependencies from requirements.txt:
```bash
pip install -r requirements.txt
```

### **6. Make Migrations**
Before running the migrations, you must create initial migrations based on your models. Run the following command:
```bash
python manage.py makemigrations
```
This will generate the migration files for your models.
Now you can proceed with running the migrations:
```bash
python manage.py migrate
```
This will set up your database according to the models you've defined in the project.

### **7. Run the Development Server**
Run the development server using the following command:
```bash
python manage.py runserver
```
By default, the server runs on port 8000.
**If Port 8000 is Already in Use**
you can specify a different port by running the server with an alternative port number:
```bash
python manage.py runserver 8080
```
This will run the server on port 8080 instead of the default port 8000.

### **8. Access the Application**
Now that the server is running open your browser and go to:
```bash
http://127.0.0.1:8000/
```bash





