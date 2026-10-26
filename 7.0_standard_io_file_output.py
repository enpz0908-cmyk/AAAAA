"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In: a date, expense category, amount, and payment method for one purchase.
# 2. Process: trim text, require non-empty category and payment method, and accept only
#    a real date in YYYY-MM-DD form and a positive numeric amount. Invalid input is
#    rejected and requested again.
# 3. Out: expenses.csv with columns date, category, amount, payment_method.
# 4. I chose these columns to track personal spending. With two hundred rows I could
#    sort or filter by date and category, total spending by category, and compare months.

import csv
from datetime import datetime
from pathlib import Path

OUTPUT_FILE = Path(__file__).with_name("expenses.csv")


def ask_for_date():
    while True:
        value = input("Date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("Please enter a real date in YYYY-MM-DD format.")


def ask_for_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This value cannot be empty.")


def ask_for_amount():
    while True:
        value = input("Amount: ").strip()
        try:
            amount = float(value)
            if amount > 0:
                return f"{amount:.2f}"
        except ValueError:
            pass
        print("Please enter an amount greater than zero.")


def main():
    entry = {
        "date": ask_for_date(),
        "category": ask_for_text("Category: "),
        "amount": ask_for_amount(),
        "payment_method": ask_for_text("Payment method: "),
    }
    file_exists = OUTPUT_FILE.exists() and OUTPUT_FILE.stat().st_size > 0
    with OUTPUT_FILE.open("a", newline="", encoding="utf-8") as output_file:
        writer = csv.DictWriter(
            output_file,
            fieldnames=["date", "category", "amount", "payment_method"],
        )
        if not file_exists:
            writer.writeheader()
        writer.writerow(entry)
    print(f"Saved one expense to {OUTPUT_FILE.name}.")


if __name__ == "__main__":
    main()
