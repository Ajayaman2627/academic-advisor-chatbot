CREATE DATABASE IF NOT EXISTS academic_db;
USE academic_db;

CREATE TABLE courses (
    course_id   VARCHAR(20) PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    credits     INT NOT NULL,
    department  VARCHAR(50) NOT NULL
);

CREATE TABLE prerequisites (
    course_id   VARCHAR(20),
    prereq_id   VARCHAR(20),
    PRIMARY KEY (course_id, prereq_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (prereq_id) REFERENCES courses(course_id)
);

CREATE TABLE schedule (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id   VARCHAR(20) NOT NULL,
    semester    VARCHAR(20) NOT NULL,
    days        VARCHAR(50) NOT NULL,
    time_slot   VARCHAR(50) NOT NULL,
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

CREATE TABLE policies (
    policy_id   INT AUTO_INCREMENT PRIMARY KEY,
    category    VARCHAR(50) NOT NULL,
    description TEXT NOT NULL
);

-- Seed data
INSERT INTO courses VALUES
('CS 2010', 'Programming Fundamentals', 3, 'Computer Science'),
('CS 3000', 'Data Structures', 3, 'Computer Science'),
('CS 3100', 'Algorithms', 3, 'Computer Science'),
('CS 4500', 'Database Systems', 3, 'Computer Science'),
('CS 5550', 'Software Engineering', 3, 'Computer Science'),
('CS 5700', 'Machine Learning', 3, 'Computer Science'),
('CS 6550', 'Big Data Analytics', 3, 'Computer Science'),
('MATH 2200', 'Discrete Mathematics', 3, 'Mathematics'),
('MATH 2600', 'Probability and Statistics', 3, 'Mathematics');

INSERT INTO prerequisites VALUES
('CS 3000', 'CS 2010'),
('CS 3100', 'CS 3000'),
('CS 4500', 'CS 3000'),
('CS 5700', 'CS 3000'),
('CS 5700', 'MATH 2600'),
('CS 6550', 'CS 4500'),
('CS 5550', 'CS 3000');

INSERT INTO schedule VALUES
(NULL, 'CS 2010', 'Fall 2026', 'Mon/Wed', '9:00 AM - 10:15 AM'),
(NULL, 'CS 3000', 'Fall 2026', 'Tue/Thu', '10:00 AM - 11:15 AM'),
(NULL, 'CS 3000', 'Spring 2027', 'Mon/Wed', '1:00 PM - 2:15 PM'),
(NULL, 'CS 3100', 'Spring 2027', 'Tue/Thu', '2:30 PM - 3:45 PM'),
(NULL, 'CS 4500', 'Fall 2026', 'Mon/Wed', '3:00 PM - 4:15 PM'),
(NULL, 'CS 5700', 'Spring 2027', 'Mon/Wed', '3:00 PM - 4:15 PM'),
(NULL, 'CS 5700', 'Fall 2026', 'Tue/Thu', '10:00 AM - 11:15 AM'),
(NULL, 'CS 6550', 'Fall 2026', 'Tue/Thu', '5:00 PM - 6:15 PM'),
(NULL, 'CS 5550', 'Spring 2027', 'Mon/Wed', '10:00 AM - 11:15 AM');

INSERT INTO policies VALUES
(NULL, 'drop', 'Students may drop a course without a W grade during the first two weeks of the semester.'),
(NULL, 'add', 'Courses may be added during the first week of instruction with instructor approval.'),
(NULL, 'withdraw', 'Withdrawal with a W is permitted between weeks 3 and 10. After week 10, withdrawal requires dean approval.'),
(NULL, 'gpa', 'Students must maintain a cumulative GPA of 3.0 or higher to remain in good academic standing in the graduate program.'),
(NULL, 'probation', 'Students whose GPA falls below 3.0 are placed on academic probation and must raise their GPA within two semesters.'),
(NULL, 'graduation', 'A minimum of 30 graduate-level credits with a 3.0 GPA is required for graduation. Students must also complete a capstone project or thesis.');
