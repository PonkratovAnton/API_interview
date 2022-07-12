from faker import Faker
from database import create_db, session
from models import Employee, Group, Interview


def create_database(load_fake_data: bool = True):
    create_db()
    if load_fake_data:
        _load_fake_data(session())


def _load_fake_data(session: session):
    interview_names = ['Геология', 'Геофизика', 'Элетродинамика','Бухгалтерский учёт', 'Физическая култура']
    group1 = Group(group_name='1-ГИК-7')
    group2 = Group(group_name='1-ТВИН-9')
    session.add(group1)
    session.add(group2)

    for key, it in enumerate(interview_names):
        interview = Interview(interview_name=it)
        interview.groups.append(group1)
        if key % 2 == 0:
            interview.groups.append(group2)
        session.add(interview)
    faker = Faker('ru_RU')
    group_list = [group1, group2]
    session.commit()

    for _ in range(50):
        full_name = faker.name().split(' ')
        age = faker.random.randint(16, 25)
        address = faker.address()
        group = faker.random.choice(group_list)
        employee = Employee(full_name, age, address, group.id)
        session.add(employee)
    session.commit()
    session.close()
