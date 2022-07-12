from sqlalchemy import Column, Integer, String, Table, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    patronymic = Column(String)
    age = Column(Integer)
    address = Column(String)
    group = Column(Integer, ForeignKey('groups.id'))

    # Конструктор для автозаполнения БД
    # def __init__(self, full_name: list[str], age: int, address: str, id_group: int):
    #     self.surname = full_name[0]
    #     self.name = full_name[1]
    #     self.patronymic = full_name[2]
    #     self.age = age
    #     self.address = address
    #     self.group = id_group


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    group_name = Column(String)
    employee = relationship('Employee', backref='groups', lazy=True)


participantGroup_table = Table('participant_group', Base.metadata,
    Column('group_id', Integer, ForeignKey('groups.id')),
    Column('interview_id', Integer, ForeignKey('interviews.id')))


class Interview(Base):
    __tablename__ = 'interviews'
    id = Column(Integer, primary_key=True)
    interview_name = Column(String)
    groups = relationship('Group', secondary=participantGroup_table, backref='group_interview')
