from flask import Flask, render_template, request, redirect, url_for
from incomming_process import icopro

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    answer = None
    question = None

    if request.method == 'POST':
        question = request.form['question']
        answer = icopro(question)

    return render_template('index.html', question=question, answer=answer)

@app.route("/ask-again")
def ask_again():
    return redirect(url_for('hello_world'))

if __name__ == "__main__":
    app.run(debug=True)
