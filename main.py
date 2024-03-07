from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/submit', methods=["POST"])
def submit():
    name = request.form.get("name")
    reason = request.args.get("reason")
    amount = request.args.get("amount")
    email = request.args.get("email")

    print("The person's name was... " + name)
    return ""

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')