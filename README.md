Expense Tracker

A simple Expense Tracker web application built with Python, Flask, and SQLite, allowing users to manage their personal expenses with ease.

Features

Add Expenses: Add new expenses with description, amount, category, and date.

Edit Expenses: Update expense details after creation.

Delete Expenses: Remove unwanted expenses with confirmation.

Expense Table: View all expenses in a clean, sortable table.

Total Calculation: Automatically calculates the total of all expenses.

Input Validation: Ensures amount is positive and all fields are required.

Flash Messages: Provides user feedback on errors and successful operations.

Responsive UI: Clean and modern interface with CSS styling.

Technologies Used

Backend: Python, Flask

Database: SQLite

Frontend: HTML, CSS, Jinja2 Templates

Other: Flash messages for user feedback

Installation

Clone the repository:

git clone <your-repo-url>
cd expense-tracker


Create a virtual environment and activate it:

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate


Install dependencies:

pip install flask


Run the app:

python app.py


Open your browser and go to:

http://127.0.0.1:5000/

Usage

Navigate to Add Expense to record a new expense.

Go to Edit Expense to modify existing entries.

Use Delete Expense to remove expenses.

Check the total of all expenses at the top of the homepage.

Future Improvements

Add user authentication for multiple users.

Include charts/graphs for visual analysis of expenses.

Add categories filters or search functionality.

Deploy the app online (Heroku, Render, etc.) for live access.

License

This project is open source and available under the MIT License.
