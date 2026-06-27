"""Initialize the SQLite database with sample academic data."""
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "academic.db")

def setup():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("DROP TABLE IF EXISTS prerequisites")
    c.execute("DROP TABLE IF EXISTS schedule")
    c.execute("DROP TABLE IF EXISTS policies")
    c.execute("DROP TABLE IF EXISTS courses")

    c.execute("""CREATE TABLE courses (
        course_id   TEXT PRIMARY KEY,
        course_name TEXT NOT NULL,
        credits     INTEGER NOT NULL,
        department  TEXT NOT NULL
    )""")

    c.execute("""CREATE TABLE prerequisites (
        course_id TEXT,
        prereq_id TEXT,
        PRIMARY KEY (course_id, prereq_id),
        FOREIGN KEY (course_id) REFERENCES courses(course_id),
        FOREIGN KEY (prereq_id) REFERENCES courses(course_id)
    )""")

    c.execute("""CREATE TABLE schedule (
        schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_id   TEXT NOT NULL,
        semester    TEXT NOT NULL,
        days        TEXT NOT NULL,
        time_slot   TEXT NOT NULL,
        FOREIGN KEY (course_id) REFERENCES courses(course_id)
    )""")

    c.execute("""CREATE TABLE policies (
        policy_id   INTEGER PRIMARY KEY AUTOINCREMENT,
        category    TEXT NOT NULL,
        description TEXT NOT NULL
    )""")

    courses = [
        ("CS 2010", "Programming Fundamentals", 3, "Computer Science"),
        ("CS 3000", "Data Structures", 3, "Computer Science"),
        ("CS 3100", "Algorithms", 3, "Computer Science"),
        ("CS 4500", "Database Systems", 3, "Computer Science"),
        ("CS 5550", "Software Engineering", 3, "Computer Science"),
        ("CS 5700", "Machine Learning", 3, "Computer Science"),
        ("CS 6550", "Big Data Analytics", 3, "Computer Science"),
        ("MATH 2200", "Discrete Mathematics", 3, "Mathematics"),
        ("MATH 2600", "Probability and Statistics", 3, "Mathematics"),
    ]
    c.executemany("INSERT INTO courses VALUES (?,?,?,?)", courses)

    prereqs = [
        ("CS 3000", "CS 2010"), ("CS 3100", "CS 3000"), ("CS 4500", "CS 3000"),
        ("CS 5700", "CS 3000"), ("CS 5700", "MATH 2600"), ("CS 6550", "CS 4500"),
        ("CS 5550", "CS 3000"),
    ]
    c.executemany("INSERT INTO prerequisites VALUES (?,?)", prereqs)

    schedules = [
        ("CS 2010", "Fall 2026", "Mon/Wed", "9:00 AM - 10:15 AM"),
        ("CS 3000", "Fall 2026", "Tue/Thu", "10:00 AM - 11:15 AM"),
        ("CS 3000", "Spring 2027", "Mon/Wed", "1:00 PM - 2:15 PM"),
        ("CS 3100", "Spring 2027", "Tue/Thu", "2:30 PM - 3:45 PM"),
        ("CS 4500", "Fall 2026", "Mon/Wed", "3:00 PM - 4:15 PM"),
        ("CS 5700", "Spring 2027", "Mon/Wed", "3:00 PM - 4:15 PM"),
        ("CS 5700", "Fall 2026", "Tue/Thu", "10:00 AM - 11:15 AM"),
        ("CS 6550", "Fall 2026", "Tue/Thu", "5:00 PM - 6:15 PM"),
        ("CS 5550", "Spring 2027", "Mon/Wed", "10:00 AM - 11:15 AM"),
    ]
    c.executemany("INSERT INTO schedule VALUES (NULL,?,?,?,?)", schedules)

    policies = [
        ("drop", "Students may drop a course without a W grade during the first two weeks of the semester."),
        ("add", "Courses may be added during the first week of instruction with instructor approval."),
        ("withdraw", "Withdrawal with a W is permitted between weeks 3 and 10. After week 10, withdrawal requires dean approval."),
        ("gpa", "Students must maintain a cumulative GPA of 3.0 or higher to remain in good academic standing in the graduate program."),
        ("probation", "Students whose GPA falls below 3.0 are placed on academic probation and must raise their GPA within two semesters."),
        ("graduation", "A minimum of 30 graduate-level credits with a 3.0 GPA is required for graduation. Students must also complete a capstone project or thesis."),
    ]
    c.executemany("INSERT INTO policies VALUES (NULL,?,?)", policies)

    conn.commit()
    conn.close()
    print(f"Database created at {DB_PATH}")

if __name__ == "__main__":
    setup()
