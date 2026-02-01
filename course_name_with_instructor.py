from flask import Flask
import urllib.request
import urllib.error

INSTRUCTOR_API_BASE = "http://127.0.0.1:8000"
INSTRUCTOR_ENDPOINT = f"{INSTRUCTOR_API_BASE}/instructor"

app = Flask(__name__)

COURSE_NAME = "Virtualization and Cloud Computing"

@app.route("/instructor_info")
def course_info():
    course_text = f"Course: {COURSE_NAME}"
    instructor_text = fetch_instructor_text()
    return f"{course_text} | {instructor_text}"

def fetch_instructor_text() -> str:
    try:
        with urllib.request.urlopen(INSTRUCTOR_ENDPOINT, timeout=2) as resp:
            text = resp.read().decode("utf-8").strip()
            return text if text else "Instructor: Not Available"
    except (urllib.error.URLError, TimeoutError, ValueError):
        return "Instructor: Not Available"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
