from flask import Flask, request
from flask_restful import Resource, Api

from chinese.Segmenter import segment_chinese
from english.Segmenter import segment_english
#from spanish.Segmenter import segment_spanish

app = Flask(__name__)
api = Api(app)


class DocumentHandler(Resource):
    def post(self, language):
        # Default responses
        words = []
        message = ""
        status = "OK"
        response_code = 200

        request_json = request.get_json()
        text = request_json['text']

        try:
            if language == "chinese":
                words = segment_chinese(text)
            elif language == "english":
                words = segment_english(text)
            #elif language == "spanish":
                #words = segment_spanish(text)
            else:
                status = "ERROR"
                message = "Language %s has not been implemented yet." % language
                response_code = 400
        except:
            status = "ERROR"
            message = "An error occurred"
            response_code = 500

        return {"status": status, "message": message, "words": words}, response_code

api.add_resource(DocumentHandler, '/v1/<string:language>/document')

if __name__ == '__main__':
    app.run(debug=True)
