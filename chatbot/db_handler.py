import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "academic.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def get_prerequisites(course_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c2.course_id, c2.course_name
        FROM prerequisites p
        JOIN courses c2 ON p.prereq_id = c2.course_id
        WHERE UPPER(REPLACE(p.course_id, ' ', '')) = UPPER(REPLACE(?, ' ', ''))
    """, (course_id,))
    results = cursor.fetchall()
    conn.close()
    return results

def get_schedule(course_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT semester, days, time_slot
        FROM schedule
        WHERE UPPER(REPLACE(course_id, ' ', '')) = UPPER(REPLACE(?, ' ', ''))
    """, (course_id,))
    results = cursor.fetchall()
    conn.close()
    return results

def get_policies(category=None):
    conn = get_connection()
    cursor = conn.cursor()
    if category:
        cursor.execute("SELECT category, description FROM policies WHERE LOWER(category) LIKE ?", (f"%{category.lower()}%",))
    else:
        cursor.execute("SELECT category, description FROM policies")
    results = cursor.fetchall()
    conn.close()
    return results

def get_course_info(course_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT course_id, course_name, credits, department
        FROM courses
        WHERE UPPER(REPLACE(course_id, ' ', '')) = UPPER(REPLACE(?, ' ', ''))
    """, (course_id,))
    result = cursor.fetchone()
    conn.close()
    return result

def get_all_courses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT course_id, course_name, credits, department FROM courses ORDER BY course_id")
    results = cursor.fetchall()
    conn.close()
    return results
