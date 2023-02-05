from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from .common.dateutils import get_current_utc_time
from shikshavalley.common.basemodel import BaseModel
from .extensions import db

class User(UserMixin, BaseModel):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(100))
    admin = db.Column(db.Boolean)
    teacher = db.Column(db.Boolean)
    student = db.Column(db.Boolean)

    @property
    def unhashed_password(self):
        raise AttributeError('Cannot view unhashed password!')

    @unhashed_password.setter
    def unhashed_password(self, unhashed_password):
        self.password = generate_password_hash(unhashed_password)

class ClassTypes(BaseModel):
    __tablename__ = 'classes'
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    created_date = db.Column(db.TIMESTAMP, default=get_current_utc_time(), nullable=False)
    updated_date = db.Column(db.TIMESTAMP, default=get_current_utc_time(), onupdate=get_current_utc_time(),nullable=False)


class StudentDetails(BaseModel):
    __tablename__ = 'students'
    admission_id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(255), nullable=False)
    father_name = db.Column(db.String(255), nullable=True)
    father_mobile_number = db.Column(db.String(255), nullable=True)
    mother_name = db.Column(db.String(255), nullable=True)
    mother_mobile_number = db.Column(db.String(255), nullable=True)
    class_id = db.Column(db.Integer, db.ForeignKey(ClassTypes.id), nullable=False)
    annual_charges = db.Column(db.Integer, nullable=False)
    registration_date = db.Column(db.TIMESTAMP, nullable=False)
    per_month_fees = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String, nullable=True)
    state = db.Column(db.String, nullable=True)
    zip = db.Column(db.String, nullable=True)
    gender = db.Column(db.String, nullable=False)
    birthday = db.Column(db.Date, nullable=True)
    books_charges = db.Column(db.Integer, nullable=True)
    sports_dress = db.Column(db.Integer, nullable=True)
    summer_dress = db.Column(db.Integer, nullable=True)
    winter_dress = db.Column(db.Integer, nullable=True)
    updated_date = db.Column(db.TIMESTAMP, default=get_current_utc_time(), onupdate=get_current_utc_time(),
                             nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)

class StudentFeesDetails(BaseModel):
    __tablename__ = 'students_fees'
    id = db.Column(db.Integer, primary_key=True)
    admission_id = db.Column(db.Integer, db.ForeignKey("students.admission_id"), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    date = db.Column(db.Date, default=get_current_utc_time(), nullable=False)
    updated_date = db.Column(db.TIMESTAMP, default=get_current_utc_time(), onupdate=get_current_utc_time(),nullable=False)