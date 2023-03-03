from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
     "id" : 1,
        "title" : "Bus. Analyst",
        "location" : "Charlotte, NC"
    },
      {
        "id" : 2,
        "title" : "Manager",
        "company" : "EY",
        "location" : "Chicago"
    },
      {
        "id" : 3,
        "title" : "Specialist",
        "company" : "McKinsey & Company",
        "location" : "Charlotte"
    },
      {
        "id" : 4,
        "title" : "Operations Manager",
        "company" : "Shopify",
        "location" : "Charlotte"
    }
]

@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5001, debug=True)
