from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Renders templates/index.html

if __name__ == '__main__':
    # Listen on all interfaces so the container’s port is accessible externally
    app.run(host='0.0.0.0', port=5000)
