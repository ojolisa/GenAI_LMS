from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv
from models import db, Week, Lecture, Assignment, Question, ProgAssg
from yt_summary import get_transcript

app = Flask(__name__)
CORS(app)

load_dotenv()

# Configure generative AI
genai.configure(api_key=os.getenv('API_KEY'))

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/info', methods=['GET'])
def get_weeks():
    weeks = Week.query.all()
    return jsonify([week.serialize() for week in weeks])


@app.route('/helper', methods=['POST'])
def handle_query():
    data = request.get_json()
    query = data.get('query')
    week_id = data.get('weekId')

    week = Week.query.get(week_id)
    if week is None:
        return jsonify({'message': 'Week not found'}), 404

    lecture_names = [lecture.name for lecture in week.lectures]

    system_instruction = f"Give answers in markdown. You only know information about {', '.join(
        lecture_names)} in python. For anything else, refuse to answer. Do not spoonfeed the entire answer. Give small code snippets for examples. Try to encourage personal research for better learning."
    print(system_instruction)
    model = genai.GenerativeModel(
        'gemini-1.5-flash', system_instruction=system_instruction
    )

    response = model.generate_content(query)
    print(response.text)

    return jsonify(response.text)


@app.route('/summary/<lectureId>', methods=['GET'])
def get_summary(lectureId):
    lecture = Lecture.query.get(lectureId)
    if lecture is None:
        return jsonify({'message': 'Lecture not found'}), 404

    url = lecture.video
    transcript = get_transcript(url)

    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(
        transcript+"\n Write a summary of this transcript.Give the answer in markdown.")

    return jsonify(response.text)


@app.route('/week', methods=['POST'])
def create_week():
    data = request.get_json()
    new_week = Week(name=data['weekName'])
    db.session.add(new_week)
    db.session.commit()
    return jsonify(new_week.serialize()), 201


@app.route('/week/<int:id>', methods=['PUT'])
def update_week(id):
    data = request.get_json()
    week = Week.query.get(id)
    if week is None:
        return jsonify({'message': 'Week not found'}), 404
    week.name = data['weekName']
    db.session.commit()
    return jsonify(week.serialize())


@app.route('/week/<int:id>', methods=['DELETE'])
def delete_week(id):
    week = Week.query.get(id)
    if week is None:
        return jsonify({'message': 'Week not found'}), 404
    db.session.delete(week)
    db.session.commit()
    return jsonify({'message': 'Week deleted'})


@app.route('/lecture', methods=['POST'])
def create_lecture():
    data = request.get_json()
    new_lecture = Lecture(
        name=data['name'], video=data['video'], week_id=data['weekId'])
    db.session.add(new_lecture)
    db.session.commit()
    return jsonify(new_lecture.serialize()), 201


@app.route('/lecture/<int:id>', methods=['PUT'])
def update_lecture(id):
    data = request.get_json()
    lecture = Lecture.query.get(id)
    if lecture is None:
        return jsonify({'message': 'Lecture not found'}), 404
    if data['name'] != "":
        lecture.name = data['name']
    if data['video'] != "":
        lecture.video = data['video']
    if data['weekId'] != "":
        lecture.week_id = data['weekId']
    db.session.commit()
    return jsonify(lecture.serialize())


@app.route('/lecture/<int:id>', methods=['DELETE'])
def delete_lecture(id):
    lecture = Lecture.query.get(id)
    if lecture is None:
        return jsonify({'message': 'Lecture not found'}), 404
    db.session.delete(lecture)
    db.session.commit()
    return jsonify({'message': 'Lecture deleted'})


@app.route('/assignment', methods=['POST'])
def create_assignment():
    data = request.get_json()
    new_assignment = Assignment(name=data['name'], week_id=data['weekId'])
    db.session.add(new_assignment)
    db.session.commit()
    return jsonify(new_assignment.serialize()), 201


@app.route('/assignment/<int:id>', methods=['PUT'])
def update_assignment(id):
    data = request.get_json()
    assignment = Assignment.query.get(id)
    if assignment is None:
        return jsonify({'message': 'Assignment not found'}), 404
    if data['name'] != "":
        assignment.name = data['name']
    if data['weekId'] != "":
        assignment.week_id = data['weekId']
    db.session.commit()
    return jsonify(assignment.serialize())


@app.route('/assignment/<int:id>', methods=['DELETE'])
def delete_assignment(id):
    assignment = Assignment.query.get(id)
    if assignment is None:
        return jsonify({'message': 'Assignment not found'}), 404
    db.session.delete(assignment)
    db.session.commit()
    return jsonify({'message': 'Assignment deleted'})


@app.route('/question', methods=['POST'])
def create_question():
    data = request.get_json()
    new_question = Question(
        question=data['question'],
        options=data['options'],
        correctOption=data['correctOption'],
        assignmentId=data['assignmentId']
    )
    db.session.add(new_question)
    db.session.commit()
    return jsonify(new_question.serialize()), 201


@app.route('/question/<int:id>', methods=['PUT'])
def update_question(id):
    data = request.get_json()
    question = Question.query.get(id)
    if question is None:
        return jsonify({'message': 'Question not found'}), 404
    if data['question'] != "":
        question.question = data['question']
    if data['options'] != "":
        question.options = data['options']
    if data['correctOption'] != "":
        question.correctOption = data['correctOption']
    if data['assignmentId'] != "":
        question.assignmentId = data['assignmentId']
    db.session.commit()
    return jsonify(question.serialize())


@app.route('/question/<int:id>', methods=['DELETE'])
def delete_question(id):
    question = Question.query.get(id)
    if question is None:
        return jsonify({'message': 'Question not found'}), 404
    db.session.delete(question)
    db.session.commit()
    return jsonify({'message': 'Question deleted'})


@app.route('/progassg', methods=['GET'])
def get_progassg():
    progassgs = ProgAssg.query.all()
    return jsonify([{
        'id': progassg.id,
        'name': progassg.name,
        'question': progassg.question,
        'week_id': progassg.week_id
    } for progassg in progassgs])


@app.route('/progassg', methods=['POST'])
def create_progassg():
    data = request.get_json()
    new_progassg = ProgAssg(
        name=data['name'],
        question=data['question'],
        week_id=data['weekId']
    )
    db.session.add(new_progassg)
    db.session.commit()
    return jsonify({'message': 'Programming Assignment creaed'}), 201


@app.route('/progassg/<int:id>', methods=['PUT'])
def update_progassg(id):
    data = request.get_json()
    progassg = ProgAssg.query.get(id)
    if progassg is None:
        return jsonify({'message': 'Programming Assignment not found'}), 404
    if data['name'] != "":
        progassg.name = data['name']
    if data['question'] != "":
        progassg.question = data['question']
    if data['weekId'] != "":
        progassg.week_id = data['weekId']
    db.session.commit()
    return jsonify({'message': 'Programming Assignment updated'}), 201


@app.route('/progassg/<int:id>', methods=['DELETE'])
def delete_progassg(id):
    progassg = ProgAssg.query.get(id)
    if progassg is None:
        return jsonify({'message': 'Programming Assignment not found'}), 404
    db.session.delete(progassg)
    db.session.commit()
    return jsonify({'message': 'Programming Assignment deleted'})


@app.route('/progassg_suggestions', methods=['POST'])
def progassg():
    data = request.get_json()  # Get the JSON data from the request
    question = data.get('question')  # Extract the question from the data
    code = data.get('code')  # Extract the code from the data

    system_instructions = "Write a brief report on the code provided. Explain how the code could be improved. Give the answer in markdown."

    model = genai.GenerativeModel(
        'gemini-1.5-flash', system_instruction=system_instructions
    )

    response = model.generate_content(question + "\n\n" + code)

    return jsonify(response.text)  # Return a JSON response


@app.route('/submit_assg', methods=['POST'])
def submit_answers():
    if request.method == 'POST':
        submitted_answers = request.json
        score = 0
        assg = 0
        results = "Question ID\tCorrect Option\tSelected Option\n"

        for question_id, selected_option in submitted_answers.items():
            # Fetch the correct option for the question from the database
            question = Question.query.get(question_id)
            results += f"{question.question}\t{question.correctOption}\t{selected_option}\n"
            if question and question.correctOption == selected_option:
                score += 1
            assg = question.assignmentId

        total_questions = len(
            Question.query.filter_by(assignmentId=assg).all())

        system_instructions = "Given is a tab seperated string having the question, correct option and the selected option. Explain how the answers is correct or incorrect. Give the answer in markdown."

        model = genai.GenerativeModel(
            'gemini-1.5-flash', system_instruction=system_instructions
        )

        message = model.generate_content(results)

        return jsonify({
            "message": message.text,
            "status": "success",
            "score": (score/total_questions) * 100,
        }), 200


if __name__ == '__main__':
    app.run(debug=True)
