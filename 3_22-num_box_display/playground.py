# Playground, chaning the number of boxes as the url changes
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play/<times>/<color>')
def boxes(times, color):
    return render_template("index.html", num_times = int(times), changecolor = color)

if __name__=="__main__":
    app.run(debug = True)