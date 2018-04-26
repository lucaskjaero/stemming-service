from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/v1/document/<language>', methods=['GET', 'POST'])
def process_document(language):
    return "Processing document in " + language
