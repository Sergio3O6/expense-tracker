from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "supersecretkey"

#Creates database if one does not exists
def init_db():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  description TEXT,
                  amount REAL,
                  category TEXT,
                  date TEXT)''')
    conn.commit()
    conn.close()

# Helper to get expenses and total
def get_expenses():
    conn = sqlite3.connect('expenses.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM expenses")
    expenses = c.fetchall()
    total = sum([expense['amount'] for expense in expenses])
    conn.close()
    return expenses, total

#Homepage for all the expenses to be shown
@app.route('/')
def index():
    expenses, total = get_expenses()
    return render_template('index.html', expenses=expenses, total=total)

#Adds new expense to table
@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        description = request.form['description']
        amount = float(request.form['amount'])
        category = request.form['category']
        date = request.form['date']
        if amount <= 0:
            flash("Amount must be greater than 0")
            return redirect(url_for("add_expense"))

        conn = sqlite3.connect('expenses.db')
        c = conn.cursor()
        c.execute("INSERT INTO expenses (description, amount, category, date) VALUES (?, ?, ?, ?)",
                  (description, amount, category, date))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_expense.html')

#Deletes an expense
@app.route('/delete/<int:expense_id>')
def del_expense(expense_id):
        conn = sqlite3.connect('expenses.db')
        c = conn.cursor()
        c.execute("DELETE FROM expenses WHERE id =?", (expense_id,))
        conn.commit()
        conn.close()
        return redirect(url_for('delete_page'))

#Page to show all expenses with a delete button
@app.route('/delete_page')
def delete_page():
    expenses, total = get_expenses()
    return render_template('delete_expense.html', expenses=expenses, total=total)

#Page to show all expenses with an edit button
@app.route('/edit_page')
def edit_page():
    expenses, total = get_expenses()
    return render_template('edit_page.html', expenses=expenses, total=total)

#Edit a single expense
@app.route('/edit/<int:expense_id>', methods=["GET", "POST"])
def edit_expense(expense_id):
    conn = sqlite3.connect('expenses.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    if request.method == "POST":
        description = request.form["description"]
        amount = float(request.form["amount"])
        category = request.form["category"]
        date = request.form["date"]
        if amount <= 0:
            flash("Amount must be greater than 0")
            return redirect(url_for("add_expense", expense_id=expense_id))

        c.execute('''
            UPDATE expenses
            SET description=?, amount=?, category=?, date=?
            WHERE id=?
        ''', (description, amount, category, date, expense_id))
        conn.commit()
        conn.close()
        return redirect(url_for("edit_page"))
    
    c.execute("SELECT * FROM expenses WHERE id=?", (expense_id,))
    expense = c.fetchone()
    if not expense:
        flash("Expense not found.")
        return redirect(url_for("edit_page"))
    conn.close()
    return render_template("edit_single.html", expense=expense)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
