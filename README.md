# BrainBunny Backend (Django)

Welcome to the BrainBunny Backend repository!
**It is a simple quiz application** created using Bootstrap and Django on my [YouTube Channel](https://youtube.com/@rskcode).
This repository contains the Django backend code for the BrainBunny project.

![BrainBunny](https://github.com/rsk-2002/brainbunny-backend-django/assets/89301813/a8967efa-101c-40c7-860f-ed246af2e153)

## To run the BrainBunny backend locally:


To set up the development environment and run the BrainBunny backend locally, please follow these steps:

1. Ensure that you have Python 3.x and pip installed on your system.
2. Clone this repository using the following command:
   ```
   git clone https://github.com/rsk-2002/brainbunny-backend-django.git
   ```
3. Change into the project directory:
   ```
   cd brainbunny-backend-django
   ```
4. Create a virtual environment:
   ```
   python3 -m venv venv
   ```
5. Activate the virtual environment:
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```
   - On Windows:
     ```
     venv\Scripts\activate
     ```
6. Install the project dependencies:
   ```
   pip install -r requirements.txt
   ```
7. Apply the database migrations:
   ```
   python manage.py migrate
   ```
8. Run the development server:
   ```
   python manage.py runserver
   ```
Thank you for your interest in the BrainBunny project!
