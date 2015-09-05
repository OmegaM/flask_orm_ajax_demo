#!coding:utf-8

from flask import Flask, jsonify, render_template
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:wxhwbx6666@localhost/sqlalchemy_test_db'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
db = SQLAlchemy(app)


class Parent(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True)
    children = db.relationship("Child", backref="parent")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Name is %r" % self.name


class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "name is %r" % self.name


tags = db.Table('tags',
                db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
                db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
                )


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    course = db.relationship('Course', secondary=tags)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "name : %r" % self.name

    def to_json(self):

        return {
            'id': self.id,
            'name': self.name,
            'courses': [{"name": c.name} for c in self.course]
        }


class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    # student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "name : %r" % self.name


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/get_student_json')
def get_student_json():
    sList = db.session.query(Student).all()
    return jsonify({"students": [s1.to_json() for s1 in sList]})

if __name__ == '__main__':
    if db:
        # p1 = db.session.query(Parent).get(1)
        # print p1
        # db.session.query(Child).filter(Child.id == 2).update({Child.name: 'child2'})
        # db.session.query(Child).filter(Child.id == 3).update({Child.name: 'child3'})
        # c4 = db.session.query(Child).filter(Child.id == 4).first()
        # db.session.delete(c4)
        # childrens = db.session.query(Parent).filter(Parent.name == 'parent1').first().children
        # for ch in childrens:
        #     print ch.id
        #     print ch.name
        # db.session.commit()
        # db.create_all()
        # s1 = Student('student1')
        # s2 = Student('student2')
        # c1 = Course('course1')
        # c2 = Course('course2')
        # c3 = Course('course3')
        # s1.course = [c1, c2, c3]
        # s2.course = [c1, c2]
        # db.session.add(s1)
        # db.session.add(s2)
        # db.session.commit()
        # s1_courses = Student.query.get(1).course
        # s1_courses = db.session.query(Student).filter(Student.name == 'student1').first().course
        # for s1c in s1_courses:
        #     print s1c.name, s1c.id
        # paginate = Student.query.paginate(1, 2, False)
        # print paginate.items

        # s1 = db.session.query(Student).filter(Student.name == 'student1').first()
        # print s1.course
        # print json.dumps(s1.to_json())
        app.run(debug=True, port=9099)
