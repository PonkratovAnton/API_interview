from database import session
from models import Employee, Group, Interview
from config import Config
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec import APISpec
from flask_apispec.extension import FlaskApiSpec
import create_database as db_creator
from schemas import EmployeeSchema, GroupSchema, InterviewSchema, ParticipantGroupSchema
from flask_apispec import use_kwargs, marshal_with
from flask import Flask


app = Flask(__name__)
app.config.from_object(Config)

docs = FlaskApiSpec()
docs.init_app(app)
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='API_interview',
        version='v1',
        openapi_version='2.0',
        plugins=[MarshmallowPlugin()],
    ),
    'APISPEC_SWAGGER_URL': '/swagger/'
})

# ----------------------------------------------------------------------------------------------
#                                   API - Employee
# ----------------------------------------------------------------------------------------------


@app.route('/employees', methods=['GET'])
@marshal_with(EmployeeSchema(many=True))
def get_employee():
    employees = Employee.query.all()
    return employees


@app.route('/employees', methods=['POST'])
@use_kwargs(EmployeeSchema)
@marshal_with(EmployeeSchema)
def post_employee(**kwargs):
    new_one = Employee(**kwargs)
    session.add(new_one)
    session.commit()
    return new_one


@app.route('/employees/<int:id>', methods=['PUT'])
@use_kwargs(EmployeeSchema)
@marshal_with(EmployeeSchema)
def put_employee(id, **kwargs):
    item = Employee.query.filter(Employee.id == id).first()
    if not item:
        return {'message': 'No tutorials with this id'}, 400
    for key, value in kwargs.items():
        setattr(item, key, value)
    session.commit()
    return item


@app.route('/employees/<int:id>', methods=['DELETE'])
@marshal_with(EmployeeSchema)
def delete_employee(id):
    item = Employee.query.filter(Employee.id == id).first()
    if not item:
        return {'message': 'No tutorials with this id'}, 400
    session.delete(item)
    session.commit()
    return item


# ----------------------------------------------------------------------------------------------
#                                   API - Group
# ----------------------------------------------------------------------------------------------


@app.route('/groups', methods=['GET'])
@marshal_with(GroupSchema(many=True))
def get_group():
    groups = Group.query.all()
    return groups


@app.route('/groups', methods=['POST'])
@use_kwargs(GroupSchema)
@marshal_with(GroupSchema)
def post_group(**kwargs):
    new_one = Group(**kwargs)
    session.add(new_one)
    session.commit()
    return new_one


@app.route('/groups/<int:id>', methods=['PUT'])
@use_kwargs(GroupSchema)
@marshal_with(GroupSchema)
def put_group(id, **kwargs):
    item = Group.query.filter(Group.id == id).first()
    if not item:
        return {'message': 'No tutorials with this id'}, 400
    for key, value in kwargs.items():
        setattr(item, key, value)
    session.commit()
    return item


@app.route('/groups/<int:id>', methods=['DELETE'])
@marshal_with(GroupSchema)
def delete_group(id):
    item = Group.query.filter(Group.id == id).first()
    if not item:
        return {'message': 'No tutorials with this id'}, 400
    session.delete(item)
    session.commit()
    return item


# ----------------------------------------------------------------------------------------------
#                                   API - Interview
# ----------------------------------------------------------------------------------------------


@app.route('/interviews', methods=['GET'])
@marshal_with(InterviewSchema(many=True))
def get_interview():
    interviews = Interview.query.all()
    return interviews


@app.route('/interviews', methods=['POST'])
@use_kwargs(InterviewSchema)
@marshal_with(InterviewSchema)
def post_interview(**kwargs):
    new_one = Interview(**kwargs)
    session.add(new_one)
    session.commit()
    return new_one


@app.route('/interviews/<int:id>', methods=['PUT'])
@use_kwargs(InterviewSchema)
@marshal_with(InterviewSchema)
def put_interview(id, **kwargs):
    item = Interview.query.filter(Interview.id == id).first()
    if not item:
        return {'message': 'No tutorials with this id'}, 400
    for key, value in kwargs.items():
        setattr(item, key, value)
    session.commit()
    return item


@app.route('/interviews/<int:id>', methods=['DELETE'])
@marshal_with(InterviewSchema)
def delete_interview(id):
    item = Interview.query.filter(Interview.id == id).first()
    if not item:
        return {'message': 'No tutorials with this id'}, 400
    session.delete(item)
    session.commit()
    return '', 400


# ----------------------------------------------------------------------------------------------
#                                   API - ParticipantGroup
# ----------------------------------------------------------------------------------------------


@app.route('/participantGroups', methods=['GET'])
@marshal_with(ParticipantGroupSchema(many=True))
def get_association():
    associations = Interview.query.all()
    return associations


@app.route('/participantGroups', methods=['POST'])
@use_kwargs(ParticipantGroupSchema)
@marshal_with(ParticipantGroupSchema)
def post_association(**kwargs):
    new_one = Interview(**kwargs)
    session.add(new_one)
    session.commit()
    return new_one


@app.route('/participantGroups/<int:id>', methods=['PUT'])
@use_kwargs(ParticipantGroupSchema)
@marshal_with(ParticipantGroupSchema)
def put_association(id, **kwargs):
    item = Interview.query.filter(Interview.id == id).first()
    if not item:
        return {'message': 'No tutorials with this id'}, 400
    for key, value in kwargs.items():
        setattr(item, key, value)
    session.commit()
    return item


@app.route('/participantGroups/<int:id>', methods=['DELETE'])
@marshal_with(ParticipantGroupSchema)
def delete_association(id):
    item = Interview.query.filter(Interview.id == id).first()
    if not item:
        return {'message': 'No tutorials with this id'}, 400
    session.delete(item)
    session.commit()
    return item


docs.register(get_employee)
docs.register(post_employee)
docs.register(put_employee)
docs.register(delete_employee)
docs.register(get_group)
docs.register(post_group)
docs.register(put_group)
docs.register(delete_group)
docs.register(get_interview)
docs.register(post_interview)
docs.register(put_interview)
docs.register(delete_employee)
docs.register(get_association)
docs.register(post_association)
docs.register(put_association)
docs.register(delete_association)


if __name__ == '__main__':
    # db_creator.create_database() - Создание БД
    app.run(debug=True)




