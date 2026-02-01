from flask import Flask

app = Flask(__name__)

INSTRUCTOR_NAME = "Chandan Varma"

@app.route("/instructor")
def instructor():
    return f"Instructor: {INSTRUCTOR_NAME}"

if __name__ == "__main__":
    # Listen on all interfaces so other VMs can call it
    app.run(host="0.0.0.0", port=8000, debug=True)