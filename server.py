from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/crossy_road')
def serve_html():
    return render_template('crossy_road.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
