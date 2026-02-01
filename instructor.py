from flask import Flask

app = Flask(__name__)

INSTRUCTOR_NAME = "Chandan Varma"

@app.route("/instructor")
def instructor():
    return f"Instructor: {INSTRUCTOR_NAME}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
