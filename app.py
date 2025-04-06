from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Face2Face Form Intelligence Engine'

if __name__ == '__main__':
    app.run()
