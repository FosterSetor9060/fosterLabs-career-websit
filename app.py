from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Welcome to fosterLabs Careers Website!"


if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)