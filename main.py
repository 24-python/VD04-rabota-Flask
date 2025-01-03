from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def film():
    html = render_template('index.html')
    return html

@app.route('/actor/')
def actor():
    html = render_template('actor.html')
    return html

if __name__ == '__main__':
    app.run()