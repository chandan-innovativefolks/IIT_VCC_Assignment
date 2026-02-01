# course_name_with_instructor.py
from flask import Flask
import urllib.request
import urllib.error

# 👇 Change this to the IP of the INSTRUCTOR VM
INSTRUCTOR_VM_IP = "192.168.1.24"
INSTRUCTOR_ENDPOINT = f"http://{INSTRUCTOR_VM_IP}:8000/instructor"

app = Flask(__name__)

COURSE_NAME = "Virtualization and Cloud Computing"

@app.route("/instructor_info")
def instructor_info():
    course_text = f"Course: {COURSE_NAME}"
    instructor_text = fetch_instructor_text()
    return f"{course_text} | {instructor_text}"

def fetch_instructor_text() -> str:
    try:
        with urllib.request.urlopen(INSTRUCTOR_ENDPOINT, timeout=3) as resp:
            text = resp.read().decode("utf-8").strip()
            return text if text else "Instructor: Not Available"
    except (urllib.error.URLError, TimeoutError, ValueError):
        return "Instructor: Not Available"

if __name__ == "__main__":
    # Listen on all interfaces so other machines can access it
    app.run(host="0.0.0.0", port=9000, debug=True)
