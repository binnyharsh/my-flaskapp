from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

### Define pages on website
### add route to tell flask from where to fetch the page
@app.route("/")
def home():
    return render_template("index.html", content="Testing")



if __name__ == "__main__":
    app.run(debug=True)
