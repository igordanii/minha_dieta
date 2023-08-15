from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def load_index():
   if request.method == "POST":
       return render_template("successful-submission.html")
   else:
      return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001")