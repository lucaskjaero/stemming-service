from flask import Flask, request
from flask_restful import Resource, Api

from chinese.Segmenter import segment_chinese
from english.Segmenter import segment_english

app = Flask(__name__)
api = Api(app)

class DocumentHandler(Resource):
    def post(self, language):
        # Default responses
        words = []
        message = ""
        status = "OK"

        request_json = request.get_json()
        text = request_json['text']

        if language == "chinese":
            words = segment_chinese(text)
        elif language == "english":
            words = segment_english(text)
        else:
            status = "ERROR"
            message = "Language %s has not been implemented yet." % language

        return {"status": status, "message": message, "words": words}

api.add_resource(DocumentHandler, '/v1/<string:language>/document')

if __name__ == '__main__':
    app.run(debug=True)
