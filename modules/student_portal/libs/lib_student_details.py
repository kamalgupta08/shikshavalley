from shikshavalley.models import StudentDetails, db, ClassTypes
import pandas as pd
from shikshavalley.common.response_helper import ResponseHelper
from dateutil.parser import parse
from .lib_student_fees import StudentFeesDetail
from sqlalchemy import and_

class StudentDetail(ResponseHelper):
    """
    Record Student Details in db

    """
    def __init__(self):
        self.date_format = '%Y-%m-%d'


    def get_student_details_by_id(self, admission_id: int):
        """
        Get student present in the system by provided id
        :return:
        """
        result = db.session.query(StudentDetails).filter(
            and_(
                StudentDetails.is_active,
                StudentDetails.admission_id == admission_id
            )
        ).first()
        return result

    def get_all_students_details(self):
        """
        Get all students present in the system
        :return:
        """
        result = db.session.query(StudentDetails).filter(
                StudentDetails.is_active
        ).all()
        all_student_details = [student_detail.as_dict() for student_detail in result]
        return all_student_details

    def get_student_details(self, admission_id: int):
        """
        Get student details
        :param admission_id:
        :return:
        """
        student_detail = self.get_student_details_by_id(admission_id)
        if not student_detail:
            return None
        student_detail = student_detail.as_dict()
        student_detail['class_name']=self.get_class_name_by_id(student_detail.pop('class_id'))
        student_fees_detail = StudentFeesDetail().get_student_fees_details(admission_id)
        if student_fees_detail is None:
            student_detail['total_amount'] = 0
            student_detail['total_paid_amount'] = 0
            student_detail['monthly_fees_details'] = []
            student_detail['balance'] = 0
        student_detail.update(student_fees_detail)
        return student_detail

    def get_student_details_by_class_name(self, full_name, father_name, class_name):
        """
        Get student details
        :param full_name
        :param father_name
        :param class_name
        :return:
        """
        class_id = self.get_class_id_by_name(class_name)
        if not class_id:
            return None

        if father_name:
            student_detail = db.session.query(StudentDetails).filter(
                and_(
                    StudentDetails.is_active,
                    StudentDetails.student_name == full_name,
                    StudentDetails.father_name == father_name,
                    StudentDetails.class_id == class_id
                )
            ).first()
        else:
            student_detail = db.session.query(StudentDetails).filter(
                and_(
                    StudentDetails.is_active,
                    StudentDetails.student_name == full_name,
                    StudentDetails.class_id == class_id
                )
            ).first()

        if not student_detail:
            return None
        student_detail = student_detail.as_dict()
        student_detail['class_name']=class_name
        student_fees_detail = StudentFeesDetail().get_student_fees_details(student_detail['admission_id'])
        if student_fees_detail is None:
            student_detail['total_amount'] = 0
            student_detail['total_paid_amount'] = 0
            student_detail['monthly_fees_details'] = []
            student_detail['balance'] = 0
        student_detail.update(student_fees_detail)
        return student_detail

    def inactive_student_details_by_id(self, admission_id: int):
        """
        Inactive student present in the system by provided id
        :return:
        """
        result = db.session.query(StudentDetails).filter(
                StudentDetails.admission_id == admission_id
            ).update({"is_active":False})
        db.session.commit()
        return result

    def create_student(self, student_frame: pd.DataFrame):
        """
        Add a student to the system
        :return:
        """
        student_frame['birthday'] = student_frame['birthday'].map(lambda x: parse(x, dayfirst=True).strftime(self.date_format))
        student_frame['registration_date'] = student_frame['registration_date'].map\
            (lambda x: parse(x, dayfirst=True).strftime(self.date_format))
        try:
            student_data_request_obj = student_frame.to_dict(orient="records")[0]
            class_name = student_data_request_obj.pop('class')
            class_id = self.get_class_id_by_name(class_name)
            if class_id:
                student_data_request_obj['class_id']=class_id
            else:
                return self.get_error_response(message="No class found")
            result = StudentDetails.new(**student_data_request_obj)
            db.session.commit()
        except Exception as e:
            return self.get_error_response(message=str(e))
        return self.get_success_response(message="Student inserted into DB")

    def get_class_name_by_id(self,class_id):
        """
        Get Class Name by Id
        :param class_id:
        :return:
        """
        result = db.session.query(ClassTypes).filter(
                ClassTypes.id == class_id
        ).first()
        if result:
            return result.class_name
        return None

    def get_class_id_by_name(self,class_name):
        """
        Get Class Name by Id
        :param class_id:
        :return:
        """
        result = db.session.query(ClassTypes).filter(
                ClassTypes.class_name == class_name
        ).first()
        if result:
            return result.id
        return None

    def get_all_class_details(self):
        """
        Get all students present in the system
        :return:
         """
        result = db.session.query(ClassTypes).filter(
            ClassTypes.is_active
        ).all()
        classes_details = [class_detail.as_dict() for class_detail in result]
        return classes_details

    def update_student_details(self,admission_id,annual_charges,
                                                              monthly_fees,sports_charges,summer_charges,
                                                              winter_charges,book_charges):
        """
        Update student present in the system
        :return:
        """
        result = db.session.query(StudentDetails).filter(
                StudentDetails.admission_id ==admission_id
        ).update({"annual_charges":annual_charges,
                "per_month_fees":monthly_fees,"sports_dress":sports_charges,
                "summer_dress": summer_charges,
                "winter_dress":winter_charges,"books_charges":book_charges})
        db.session.commit()
        return result
