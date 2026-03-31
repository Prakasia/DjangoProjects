# 📚 Simple Django Bookstore
A lightweight Django web application built to practice the fundamentals of the framework. This project focuses on  
- URL routing  
- View logic  
- Django HTML using static data.  


### 🚀 Purpose
The goal of this project was to understand how Django handles web requests. By using static data instead of a database, I focused on:  
- Mapping URLs to Python functions (Views).
- Passing data dictionaries (Context) to HTML templates.
- Using Template Inheritance ({% extends %}) to keep code DRY (Don't Repeat Yourself).

### 🔬 Focus: Regex URL Routing
In modern Django, we often use simple strings for paths. However, this project utilizes the older url() patterns to master complex string matching.


### 🛠️ Tech Stack
*Framework*: Django1.11  
*Language*: Python3.5  
*Frontend*: HTML5, CSS (Basic)  

### 📂 Features & Logic
*Home Page*: Displays a Welcome message.  
*About Us* : Gives a small message on vision and mission  
*Find Books* : Displays a list of books using a static list of dictionaries.   
*Base Templates*: Utilizes a base.html file to maintain a consistent header and footer across all pages.  

### 🏃 How to Run Locally
1. Clone the repository:  

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
2. Create and activate a virtual environment:

```bash
python3.5 -m venv venv
# On Windows:
venv\Scripts\activate
```
3. Install Django:

```bash
python -m pip install django==1.11
```

4. Launch the server:

```bash
python manage.py runserver
```

5. Visit in your browser!

### 🎓 Lessons Learned
- How to use ^ and $ to anchor URL patterns.

- The difference between capturing positional arguments vs keyword arguments in views.

- Managing Django templates without a database backend.

### ⚠️ A Note
Since this project uses Python 3.5 and Django 1.11 (both of which are End-of-Life), this repository is strictly for educational purposes and practicing regex logic.