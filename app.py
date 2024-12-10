from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == '__main__':
  try:
    app.run(debug=True)
    print("Flask app started")
  except Exception as e:
    print(f"An error occurred: {e}")