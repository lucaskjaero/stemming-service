from flask import Flask
from flask_restful import Resource, Api

from chinese.Segmenter import words_in_text

app = Flask(__name__)
api = Api(app)

class DocumentHandler(Resource):
    def post(self, language):
        if (language == "chinese"):
            words = words_in_text("Text")

        return {"message": "Parsing not supported yet", "language": language}

api.add_resource(DocumentHandler, '/v1/document/<string:language>')

if __name__ == '__main__':
    app.run(debug=True)
