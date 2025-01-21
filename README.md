# CodePlayground - README

## Overview
This project is a Django-based problem-solving platform designed to help users practice coding problems. Each problem has detailed descriptions, test cases, and starter code to guide users. The platform supports functionality to create, view, and solve coding problems while tracking user progress.
![image](https://github.com/user-attachments/assets/28972b37-6583-45b3-a02e-019806ebd4c7)

---

## Features
1. **Interactive Python Interpreter::**
   - Users can run Python code directly in the browser to test their solutions.
   - Input and output are displayed within the platform to provide immediate feedback.
   - Allows users to solve problems and check their code functionality interactively in real time.
  
![image](https://github.com/user-attachments/assets/57258f89-fc88-4f25-8d40-2bd1ea762af2)

2. **Future Enhancements:**
   - View problems with a detailed description.
   - Solve challenges and submit solutions (test case feature planned for future).
   - Add automated test case evaluation.
   - Track user progress and display leaderboards.

---

## Installation
### Prerequisites
- Python 3.10.6
- Django 5.1.5
- PostgreSQL 17.2

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Technical-D/CodePlayground.git
   cd CodePlayground
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations to set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser for the admin panel:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the platform in your browser:
   - Admin panel: `http://127.0.0.1:8000/admin/`
   - Platform home: `http://127.0.0.1:8000/`

---

## Future Enhancements
1. **Test Case Execution:**
   - Add a mechanism to evaluate user submissions against predefined test cases.

2. **User Progress Tracking:**
   - Track which problems users have solved.

3. **Leaderboard:**
   - Display top performers based on scores.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contact
For queries or suggestions, contact:
- Email: dheerajgupta1902@gmail.com
- GitHub: https://github.com/Technical-D

