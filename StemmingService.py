from flask import Flask, request
from flask_restful import Resource, Api

from chinese.Segmenter import words_in_text

app = Flask(__name__)
api = Api(app)

class DocumentHandler(Resource):
    def post(self, language):
        if (language == "chinese"):
            text = request.form['text']
            words = list(words_in_text(text))

        return {"words": words, "language": language}

api.add_resource(DocumentHandler, '/v1/document/<string:language>')

if __name__ == '__main__':
    app.run(debug=True)
