import json
from flask import Flask, request, render_template
data = json.load(open('data.json'))

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    word = request.form['word']
    def translate(w):
        w = w.lower()
        if w in data:
            return data[w]
        return "Wrong data"
    output = translate(word)
    return render_template('result.html',output=output)



if __name__ == '__main__':
    app.run(debug=True)