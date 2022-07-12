from marshmallow import Schema, fields


class EmployeeSchema(Schema):
    id = fields.Integer(required=True)
    surname = fields.String(required=True)
    name = fields.String(required=True)
    patronymic = fields.String(required=True)
    age = fields.Integer(required=True)
    address = fields.String(required=True)
    group = fields.Integer(required=True)


class GroupSchema(Schema):
    id = fields.Integer(required=True)
    group_name = fields.String(required=True)
    employee = fields.Nested(EmployeeSchema, many=True, dump_only=True)


class InterviewSchema(Schema):
    id = fields.Integer(required=True)
    interview_name = fields.String(required=True)


class ParticipantGroupSchema(Schema):
    id = fields.Integer(required=True)
    interview_name = fields.String(required=True)
    groups = fields.Nested(GroupSchema, many=True, dump_only=True)
