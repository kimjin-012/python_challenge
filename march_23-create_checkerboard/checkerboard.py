# Checkerboard creation

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/<hori>/<vert>/<startc>/<endc>')
def boxes(hori, vert, startc, endc):
    return render_template("index.html", num_times = int(hori), num_ver = int(vert), start_color = startc, end_color = endc)

if __name__=="__main__":
    app.run(debug = True)