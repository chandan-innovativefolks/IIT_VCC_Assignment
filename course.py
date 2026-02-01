from flask import Flask

app = Flask(__name__)

AUTHOR_NAME = "The Great Chandan Varma"

@app.route("/author")
def author():
    return f"By: {AUTHOR_NAME}"

if __name__ == "__main__":
    # Port should match what the calling service expects
    app.run(host="0.0.0.0", port=8000)