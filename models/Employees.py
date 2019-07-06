from main import db
from datetime import datetime
from models.Payrolls import PayrollsModel


class EmployeesModel(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(50), unique=True)
    kra_pin = db.Column(db.String(50), unique=True)
    hire_date = db.Column(db.DateTime, default=datetime.now())
    basic_salary = db.Column(db.Float, default=0)
    benefits = db.Column(db.Float, default=0)
    # create a pseudo column
    payrolls = db.relationship(PayrollsModel, backref='employee')

    # create
    def insert_record(self):
        db.session.add(self)  # basically adding and checking the specified constraints
        db.session.commit()  # saving into the database

    # check email
    @classmethod
    def check_email(cls, email):
        record = cls.query.filter_by(email=email).first()
        return record

    # check kra
    @classmethod
    def check_kra_pin(cls, kra_pin):
        record = cls.query.filter_by(kra_pin=kra_pin).first()
        return record

    # read
    @classmethod
    def fetch_all_records(cls):
        return cls.query.all()

    #  read by id
    @classmethod
    def fetch_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    # delete
    @classmethod
    def delete_by_id(cls, id):
        record = cls.query.filter_by(id=id)
        record.delete()
        db.session.commit()
        return True

    # update
    @classmethod
    def update_by_id(cls, id, name=None, gender=None, email=None, kra_pin=None, basic_salary=None, benefits=None):
        record = cls.query.filter_by(id=id).first()
        if name:
            record.name = name
        if gender:
            record.gender = gender
        if email:
            record.email = email
        if kra_pin:
            record.kra_pin = kra_pin
        if basic_salary:
            record.basic_salary = basic_salary
        if benefits:
            record.benefits = benefits

        db.session.commit()
        return True



# look on pygal and flask migrate