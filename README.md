# Django To-Do List Web Application

## Overview
This is my first web application built using the Django framework. It is a simple To-Do List app that allows users to:

- Add tasks
- Mark tasks as completed
- Delete tasks

The project was created as a learning exercise to understand the basics of Django, including models, views, templates, and routing.

---

## Features

- **Add Tasks**: Users can add new tasks to their to-do list.
- **Mark as Complete**: Users can mark tasks as completed.
- **Delete Tasks**: Users can delete tasks they no longer need.
- **User-Friendly Interface**: A simple and clean design for easy task management.

---

## Tech Stack

- **Backend**: Django 4.0+
- **Frontend**: HTML, CSS, Bootstrap (optional)
- **Database**: SQLite (default with Django)

---

## Installation

Follow these steps to set up the project on your local machine:

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django-todo-list.git
   cd django-todo-list
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Open the app in your browser:
   ```
   http://127.0.0.1:8000
   ```

---

## Usage

1. Open the web app in your browser.
2. Add tasks using the input form.
3. Mark tasks as completed by clicking the checkbox.
4. Delete tasks as needed.

---

## Folder Structure

```
├── manage.py
├── todo_app/        # Django app containing the main functionality
│   ├── migrations/  # Database migrations
│   ├── templates/   # HTML templates
│   ├── models.py    # Database models
│   ├── views.py     # Application views
│   ├── urls.py      # Routing URLs
├── static/          # Static files (CSS, JS, Images)
└── db.sqlite3       # SQLite database file
```

---

## Contributing

If you'd like to contribute:

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

- The Django documentation for its detailed and beginner-friendly tutorials.
- Any online resources, forums, or mentors who helped along the way.
