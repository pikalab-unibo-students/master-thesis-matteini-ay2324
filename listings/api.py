questions_bp = Blueprint("questions", __name__)
api = Api(questions_bp)


class QuestionResource(Resource):

    def get(self, question_code=None):
        if question_code:
            graph_question_id: EntityId = GraphQuestionFactory.id_of(code=question_code)
            question: Optional[GraphQuestion] = question_service.get_question_by_id(
                graph_question_id
            )
            if question:
                return serialize(question), StatusCode.OK
            else:
                return "Question not found", StatusCode.NOT_FOUND
        else:
            all_questions: List = question_service.get_all_questions()
            all_questions.sort(key=lambda q: q.id)
            return [serialize(question) for question in all_questions], StatusCode.OK

    def post(self):
        new_question: GraphQuestion = deserialize(request.get_json(), GraphQuestion)
        try:
            question_service.add_question(new_question)
        except ConflictError as e:
            return e.message, e.status_code
        return serialize(new_question.id), StatusCode.CREATED

    ...
    
api.add_resource(QuestionResource, "/questions", "/questions/<string:question_code>")