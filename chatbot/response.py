from chatbot.nlp import extract_course_id
from chatbot.db_handler import get_prerequisites, get_schedule, get_policies, get_course_info, get_all_courses

def generate_response(intent, original_message, tokens):
    course_id = extract_course_id(tokens)

    if intent == "prerequisites":
        if not course_id:
            return "Which course are you asking about? Please include the course ID (e.g., CS 5700)."
        prereqs = get_prerequisites(course_id)
        if prereqs:
            prereq_list = ", ".join(f"{pid} ({pname})" for pid, pname in prereqs)
            return f"Prerequisites for {course_id}: {prereq_list}"
        course = get_course_info(course_id)
        if course:
            return f"{course_id} ({course[1]}) has no listed prerequisites."
        return f"I couldn't find course {course_id} in our database."

    elif intent == "scheduling":
        if not course_id:
            return "Which course schedule are you looking for? Please include the course ID (e.g., CS 5700)."
        schedule = get_schedule(course_id)
        if schedule:
            lines = [f"  - {sem}: {days} {time}" for sem, days, time in schedule]
            return f"Schedule for {course_id}:\n" + "\n".join(lines)
        course = get_course_info(course_id)
        if course:
            return f"No schedule found for {course_id} ({course[1]}) at this time."
        return f"I couldn't find course {course_id} in our database."

    elif intent == "course_info":
        if not course_id:
            courses = get_all_courses()
            if courses:
                course_list = ", ".join(f"{cid}" for cid, _, _, _ in courses[:10])
                return f"Here are some available courses: {course_list}. Ask about a specific course for details."
            return "Please specify a course ID (e.g., CS 5700)."
        course = get_course_info(course_id)
        if course:
            return f"{course[0]} - {course[1]} | {course[2]} credits | Department: {course[3]}"
        return f"I couldn't find course {course_id} in our database."

    elif intent == "policy":
        policy_keywords = [t for t in tokens if t in ("drop", "add", "withdraw", "gpa", "probation", "deadline", "graduation")]
        category = policy_keywords[0] if policy_keywords else None
        policies = get_policies(category)
        if policies:
            lines = [f"  - {cat}: {desc}" for cat, desc in policies]
            return "Relevant policies:\n" + "\n".join(lines)
        return "I couldn't find specific policies for that topic. Try asking about: drop/add, withdrawal, GPA, or graduation requirements."

    else:
        return ("I'm your Academic Advisor Chatbot! I can help with:\n"
                "  - Course prerequisites (e.g., 'What are the prerequisites for CS 5700?')\n"
                "  - Class schedules (e.g., 'When is CS 5700 offered?')\n"
                "  - Department policies (e.g., 'What is the drop policy?')\n"
                "  - Course information (e.g., 'Tell me about CS 5700')")
