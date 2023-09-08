# To-Do List App

## Introduction
Welcome to the To-Do List App! This application is a simple and efficient tool to manage tasks and stay organized. Please take note that this is still a projects in the works and is not yet finalised.

## Features
- **Create Multiple To-Do Lists:** You can create and manage multiple to-do lists, each with its own set of tasks.
- **Add Titles:** Give each to-do list a meaningful title to help you categorize and organize your tasks.
- **List Items:** Under each title, you can add multiple list items. These represent your individual tasks.
- **Task Details:** Add important details to each list item, such as due dates, descriptions, and notes.
- **Task Status:** Easily mark tasks as complete or incomplete to keep track of your progress.
- **Edit and Delete:** You have the flexibility to edit or delete titles, list items, and their details as needed.

## Getting Started
To get started with the To-Do List App, follow these steps:

1. **Installation:**
   - Clone this repository to your local machine.
   - Ensure you have Python and Django installed.

2. **Setting up the Environment:**
   - Navigate to the project directory.
   - There is no  requirements.txt file included yet so you can not Run `pip install -r requirements.txt` to install the necessary dependencies.
   - You will need to have Django and Python installed to work with the project as requirements for now

3. **Database Setup:**
   - Run `python manage.py migrate` to set up the database.
   - Create a superuser with `python manage.py createsuperuser` to manage the admin panel (optional).

4. **Running the Application:**
   - Start the development server with `python manage.py runserver`.
   - Access the app in your browser at `http://localhost:8000`.

5. **Usage:**
   - Create your to-do lists, add titles, list items, and details.
   - Manage your tasks by marking them as complete or editing/deleting them.
   
6. **Admin Panel:**
   - Access the admin panel at `http://localhost:8000/admin` (if you created a superuser).
   - Manage users, to-do lists, and tasks through the admin interface.

## Contributing
We welcome contributions from the community to improve and enhance this To-Do List App.

## Contact
If you have any questions, feedback, or issues, please feel free to reach out to us.

Thank you.
