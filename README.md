
**PRODIGY_FS_01:** Flask User Authentication System

This is a simple and secure user authentication application built using Flask and SQLite. The project demonstrates user registration, login, logout, password hashing, session handling, and protected dashboard access.

**Table of Contents**  
1. Tech Stack  
2. Project Structure  
3. Installation  
4. Usage  

**1. Tech Stack**  
- Frontend: HTML  
- Backend: Flask (Python)  
- Database: SQLite  
- Security: Werkzeug password hashing, Flask sessions  

**2. Project Structure**

project-root  
├── app.py  
├── config.py  
├── instance  
│   └── mydatabase.db (created after first run)  
├── templates  
│   ├── login.html  
│   ├── register.html  
│   └── dashboard.html  
└── README.md  

**3. Installation**

1. Clone the repository:

   git clone https://github.com/Roopashree-3/PRODIGY_FS_01.git
   cd flask-auth-app

2. Create a virtual environment and activate it:

   python -m venv venv  
   venv\Scripts\activate  (on Windows)  
   source venv/bin/activate (on Mac/Linux)

3. Install required packages:

   pip install flask flask_sqlalchemy werkzeug

4. Make sure the `instance` folder exists:

   If not, create it manually to avoid SQLite errors.

5. Run the application:

   python app.py

6. Open your browser and go to:

   http://localhost:5000

**4. Usage**

- Register: Create a new user account with username, email, and password  
- Login: Enter your credentials to access the dashboard  
- Dashboard: Accessible only after login  
- Logout: Clear session and return to login page

**Contributing**  
You are welcome to fork this repository, make improvements, and submit pull requests. Contributions are appreciated!
