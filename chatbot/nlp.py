import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    nltk.download("punkt_tab", quiet=True)

try:
    stopwords.words("english")
except LookupError:
    nltk.download("stopwords", quiet=True)

STOP_WORDS = set(stopwords.words("english"))

def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    tokens = word_tokenize(text)
    return [t for t in tokens if t not in STOP_WORDS]

def classify_intent(tokens):
    prereq_keywords = {"prerequisite", "prerequisites", "require", "required", "requirement", "needed", "need", "before", "prereq"}
    schedule_keywords = {"schedule", "time", "when", "class", "classes", "offered", "section", "days", "hours", "semester"}
    policy_keywords = {"policy", "policies", "rule", "rules", "department", "deadline", "drop", "add", "withdraw", "gpa", "probation"}
    course_keywords = {"course", "credits", "credit", "description", "about", "what"}

    token_set = set(tokens)

    if token_set & prereq_keywords:
        return "prerequisites"
    elif token_set & schedule_keywords:
        return "scheduling"
    elif token_set & policy_keywords:
        return "policy"
    elif token_set & course_keywords:
        return "course_info"
    else:
        return "general"

def extract_course_id(tokens):
    for i, token in enumerate(tokens):
        if token in ("cs", "cse", "math", "eng") and i + 1 < len(tokens):
            next_token = tokens[i + 1]
            if next_token.isdigit():
                return f"{token.upper()} {next_token}"
    for token in tokens:
        if any(c.isdigit() for c in token) and len(token) >= 4:
            return token.upper()
    return None
