from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Week(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    lectures = db.relationship('Lecture', backref='week', lazy=True)
    assignments = db.relationship('Assignment', backref='week', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'lectures': [lecture.serialize() for lecture in self.lectures],
            'assignments': [assignment.serialize() for assignment in self.assignments]
        }


class Lecture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    video = db.Column(db.String(500), nullable=False)
    week_id = db.Column(db.Integer, db.ForeignKey('week.id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'video': self.video,
            'week_id': self.week_id
        }


class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    week_id = db.Column(db.Integer, db.ForeignKey('week.id'), nullable=False)
    questions = db.relationship('Question', backref='assignment', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'week_id': self.week_id,
            'questions': [question.serialize() for question in self.questions]
        }


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(500), nullable=False)
    options = db.Column(db.PickleType, nullable=False)
    correctOption = db.Column(db.String(100), nullable=False)
    assignmentId = db.Column(db.Integer, db.ForeignKey(
        'assignment.id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'question': self.question,
            'options': self.options,
            'correctOption': self.correctOption,
            'assignmentId': self.assignmentId
        }


class ProgAssg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    question = db.Column(db.String(500), nullable=False)
    week_id = db.Column(db.Integer, nullable=False)
