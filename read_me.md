# **Expense Management System**

📘 ABOUT
---------
This is a simple Expense Tracking System built using Python, FastAPI, and MySQL. 
It allows users to add, view, update, and delete their daily expenses, and also 
analyze spending patterns using simple data visualization.This web app is designed to **track your daily expenses** efficiently.  
It helps you gain **better insights** into where your money is being spent,  
so you can make **smarter financial decisions**, improve **budget management**,  
and increase your **savings** over time.

💡 **Try it now and take control of your finances!**

🧩 FEATURES
------------
- Add new expenses with date, category, and amount
- Update or delete existing expense entries
- View total and category-wise expenses
- Monthly analytics (e.g., spending by month)
- REST API built using FastAPI
- Data stored in MySQL database
- Optional frontend using Streamlit for easy visualization

🗂️ PROJECT STRUCTURE
---------------------
project_expense_tracking-system/
│
├── frontend/                                  # User Interface built with Streamlit
│   ├── add_update_ui.py                       # UI for adding and updating expenses
│   ├── analytics_by_category.py               # Displays analytics grouped by category
│   ├── analytics_by_month.py                  # Displays analytics grouped by month
│   └── app.py                                 # Main entry point for the Streamlit frontend
│
├── backend/                                   # Core backend with FastAPI and MySQL
│   ├── db_helper.py                           # Handles database connections and CRUD operations
│   ├── logging_setup.py                       # Logging configuration and handlers
│   ├── paths.py                               # Centralized file and directory paths
│   └── server.py                              # FastAPI main server file (defines API endpoints)
│
├── test/                                      # Unit and integration tests
│   ├── test_backend/                          # Tests for backend components
│   │   └── test_db_helper.py                  # Tests database helper functions
│   └── test_frontend/                         # Tests for frontend UI and data flow
│
├── requirements.txt                           # List of required Python packages
└── README.txt                                 # Project documentation (this file)

🧱 REQUIREMENTS
---------------
- Python 3.9 or above
- MySQL Server installed and running
- FastAPI
- Uvicorn
- mysql-connector-python
- pandas
- streamlit
- pytest (for running tests)
- logging (standard library)
- 
📦 INSTALLATION
----------------
1. Clone or download this repository.
2. Create a virtual environment:
   python -m venv venv
   venv\Scripts\activate     (on Windows)
   source venv/bin/activate    (on macOS/Linux)

3. Install dependencies:
   pip install -r requirements.txt

4. Set up MySQL database:
   - Open MySQL and run:
     CREATE DATABASE expense_db;
     USE expense_db;

   - Create the table:
     CREATE TABLE expenses (
         id INT AUTO_INCREMENT PRIMARY KEY,
         date DATE,
         category VARCHAR(50),
         amount DECIMAL(10,2),
         description TEXT
     );

⚙️ RUNNING THE APP
-------------------
1. Start the FastAPI backend:
   uvicorn backend.main:app --reload
   (API available at: http://127.0.0.1:8000)

2. (Optional) Start the Streamlit frontend:
   streamlit run frontend/app.py
   (Dashboard opens in browser)

🧾 API ENDPOINTS
-----------------
- GET /expenses/ → Fetch all expenses
- POST /expenses/ → Add a new expense
- PUT /expenses/{id} → Update an expense
- DELETE /expenses/{id} → Delete an expense
- GET /analytics_by_month/ → View monthly analytics
