questions_bp = Blueprint("questions", __name__)
api = Api(questions_bp)


class QuestionResource(Resource):

    def get(self, question_code=None):
        # ...

    def post(self):
        # ...
    
api.add_resource(
    QuestionResource, 
    "/questions",
    "/questions/<string:question_code>"
)
