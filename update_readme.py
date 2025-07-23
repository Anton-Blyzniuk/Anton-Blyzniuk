import re
from datetime import date, datetime

README_FILE = "README.md"
BIRTH_DATE = date(2005, 12, 12)
START_DATE = date(2022, 12, 12)

PATTERN = r"I’m \d+ years old, and I’ve been programming for over \d+ years"

def calculate_years_since(since_date: date) -> int:
    today = date.today()
    years = today.year - since_date.year
    # Check if birthday/anniversary has occurred yet this year
    if (today.month, today.day) < (since_date.month, since_date.day):
        years -= 1
    return years

def generate_updated_line(age: int, experience: int) -> str:
    return f"I’m {age} years old, and I’ve been programming for over {experience} years"

def update_readme():
    age = calculate_years_since(BIRTH_DATE)
    experience = calculate_years_since(START_DATE)

    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    new_line = generate_updated_line(age, experience)
    updated_content = re.sub(PATTERN, new_line, content)

    if content != updated_content:
        with open(README_FILE, "w", encoding="utf-8") as f:
            f.write(updated_content)
        print("✅ README.md updated.")
    else:
        print("ℹ️ No changes needed — already up to date.")

if __name__ == "__main__":
    update_readme()