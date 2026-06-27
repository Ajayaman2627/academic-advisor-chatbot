# Academic Advisor Chatbot

> An AI-powered chatbot that automates student queries on course prerequisites, scheduling, and department policies using NLP-based intent classification and a database-backed knowledge system.

---

## Overview

This project builds a functional academic advisor assistant designed to reduce manual advisor workload by automatically answering common student questions. The system uses NLP text preprocessing and pattern-based intent classification to match user queries to structured academic data stored in a relational database.

---

## Features

- Natural language query understanding using NLP preprocessing
- Intent classification to categorize student queries (prerequisites, scheduling, policies, etc.)
- Database-backed response generation using structured academic records
- Context-aware response generation for multi-type queries
- Scalable query-handling architecture for high-volume student interactions

---

## System Architecture

```
User Input (Text Query)
        │
        ▼
   NLP Preprocessing
   (Tokenization → Stop-Word Removal → Normalization)
        │
        ▼
   Intent Classifier
   (Pattern Matching / ML Classification)
        │
        ▼
   Database Query Layer (SQL)
        │
        ▼
   Response Generator
        │
        ▼
   Chatbot Response
```

---

## NLP Pipeline

```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    return [t for t in tokens if t not in stop_words]

def classify_intent(tokens):
    if any(w in tokens for w in ['prerequisite', 'require', 'needed']):
        return 'prerequisites'
    elif any(w in tokens for w in ['schedule', 'time', 'when', 'class']):
        return 'scheduling'
    elif any(w in tokens for w in ['policy', 'rule', 'department', 'requirement']):
        return 'policy'
    else:
        return 'general'
```

---

## Database Schema

```sql
CREATE TABLE Courses (
    course_id   VARCHAR(20) PRIMARY KEY,
    course_name VARCHAR(100),
    credits     INT,
    department  VARCHAR(50)
);

CREATE TABLE Prerequisites (
    course_id   VARCHAR(20),
    prereq_id   VARCHAR(20),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id),
    FOREIGN KEY (prereq_id) REFERENCES Courses(course_id)
);

CREATE TABLE Schedule (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id   VARCHAR(20),
    semester    VARCHAR(20),
    days        VARCHAR(50),
    time_slot   VARCHAR(50),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

CREATE TABLE Policies (
    policy_id   INT AUTO_INCREMENT PRIMARY KEY,
    category    VARCHAR(50),
    description TEXT
);
```

---

## Sample Interaction

```
Student: What are the prerequisites for CS 5700?
Bot:     CS 5700 (Machine Learning) requires:
         - CS 3000: Data Structures
         - MATH 2600: Probability and Statistics
         Would you like to see the schedule for CS 5700?

Student: Yes, when is it offered?
Bot:     CS 5700 is offered:
         - Spring 2026: Mon/Wed 3:00 PM – 4:15 PM
         - Fall 2026: Tue/Thu 10:00 AM – 11:15 AM
```

---

## Setup

### Prerequisites
- Python 3.8+
- MySQL 8.x

### Install Dependencies

```bash
pip install -r requirements.txt
```

`requirements.txt`:
```
nltk==3.8.1
flask==3.0.0
mysql-connector-python==8.3.0
python-dotenv==1.0.0
```

### Run

1. Clone the repository
2. Import `schema/academic_db.sql` into MySQL
3. Create a `.env` file:
   ```
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=your_password
   DB_NAME=academic_db
   ```
4. Download NLTK data:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```
5. Run the application:
   ```bash
   python app.py
   ```

---

## Project Structure

```
academic-advisor-chatbot/
├── app.py               # Flask app and routes
├── chatbot/
│   ├── nlp.py           # Preprocessing and intent classification
│   ├── db_handler.py    # SQL query layer
│   └── response.py      # Response generation
├── schema/
│   └── academic_db.sql
├── requirements.txt
└── README.md
```

---

## Tech Stack

- **Language:** Python
- **NLP:** NLTK (tokenization, stop-word removal)
- **Backend:** Flask
- **Database:** MySQL
- **Version Control:** Git, GitHub

---

## Author

**Ajayaman Kantumuchu**
MS in Computer Science, CSUSB | ajayamankantumuchu@gmail.com
[LinkedIn](https://linkedin.com/in/YOUR_USERNAME) | [GitHub](https://github.com/Ajayaman2627)
