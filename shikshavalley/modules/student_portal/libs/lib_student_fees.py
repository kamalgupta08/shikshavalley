from shikshavalley.models import StudentFeesDetails, db, StudentDetails
import pandas as pd
from shikshavalley.common.response_helper import ResponseHelper
from datetime import date
import numpy as np

class StudentFeesDetail(ResponseHelper):
    """
    Record and Fetch Student Fees Details in db

    """
    def __init__(self):
        self.total_amount = 0
        self.total_paid_amount = 0
        from .lib_student_details import StudentDetail
        self.student_details = StudentDetail()

    def get_student_fees_by_id(self, admission_id: int):
        result = db.session.query(StudentFeesDetails) \
            .filter(StudentFeesDetails.admission_id == admission_id) \
            .all()
        return result

    def get_all_students_fees_details(self):
        result = db.session \
            .query(StudentFeesDetails) \
            .all()
        return result

    def get_all_fees_details(self):
        result = db.session \
            .query(StudentFeesDetails,StudentDetails.student_name,StudentDetails.father_name,
                   StudentDetails.class_id) \
            .join(StudentDetails).filter(StudentDetails.is_active).all()
        return result

    def get_all_fees_details_by_daterange(self, start_date, end_date):
        result = db.session \
            .query(StudentFeesDetails,StudentDetails.student_name,
                   StudentDetails.class_id) \
            .join(StudentDetails) \
            .filter(StudentFeesDetails.date>= start_date,StudentFeesDetails.date<= end_date) \
            .all()
        return result

    def insert_student_fees(self, admission_id: int, fees_details:list):
        """
        Insert student fees details to the system
        :param fees_details: list of dict
        :return:
        """
        try:
            fees_detail = {k.lower(): v for k, v in fees_details.items() if k!='Status'}
            fees_detail['amount']=int(float(fees_detail['amount']))
            fees_detail['admission_id']=admission_id
            result = StudentFeesDetails.new(**fees_detail)
            db.session.commit()
        except Exception as e:
            return self.get_error_response(message=str(e))
        return self.get_success_response(message="Student fees inserted into DB")

    def get_student_fees_details(self, admission_id: int):
        """
        This function will help in calculating student fees
        :return:
        """

        #Check Student details in students table
        student_detail = self.student_details.get_student_details_by_id(admission_id)
        if not student_detail:
            return None
        registration_date = student_detail.registration_date
        monthly_fees = student_detail.per_month_fees
        annual_charges = student_detail.annual_charges
        books_charges = student_detail.books_charges
        sports_dress = student_detail.sports_dress
        summer_dress = student_detail.summer_dress
        winter_dress = student_detail.winter_dress

        # Total Amount - Registration Date Month * Current Date Month

        current_date = date.today()
        num_months = (current_date.year - registration_date.year) * 12 \
                     + (current_date.month - registration_date.month)

        self.total_amount = (num_months+1)*monthly_fees + annual_charges + books_charges + sports_dress \
                            + summer_dress + winter_dress

        #Get Monthly Fees Details

        monthly_fees_result = self.get_student_fees_by_id(admission_id)
        monthly_fees_details = [fees_detail.as_dict() for fees_detail in monthly_fees_result]
        df = pd.DataFrame(monthly_fees_details)
        balance = self.total_amount
        if not df.empty:
            self.total_paid_amount = df['amount'].sum()
            balance = self.total_amount - self.total_paid_amount
        return {"total_amount": self.total_amount,
                "total_paid_amount": self.total_paid_amount,
                "monthly_fees_details": monthly_fees_details,
                "balance": balance
                }

    def get_students_balance(self):
        """
        This function will help in calculating students balance
        :return:
        """

        #Check Student details in students table
        students_details_frame = self.student_details.get_all_students_details()
        df = pd.DataFrame(students_details_frame)
        if df.empty:
            return None
        current_date = date.today()
        df['registration_date'] = pd.to_datetime(df['registration_date']).apply(lambda x: x.date())
        df['num_months'] = df['registration_date'].map(lambda x: (current_date.year - x.year) * 12 \
                     + (current_date.month - x.month) + 1)
        df['total_amount'] = df['num_months']*df['per_month_fees'] + df['annual_charges']+df['books_charges']+ \
                             df['sports_dress'] + df['summer_dress'] + df['winter_dress']
        students_fees_details_frame = self.get_all_students_fees_details()
        monthly_fees_details = [fees_detail.as_dict() for fees_detail in students_fees_details_frame]
        df_fees = pd.DataFrame(monthly_fees_details)
        df2 = df_fees.groupby('admission_id', as_index=False)['amount'].sum()
        df_left_merge = pd.merge(df, df2, how='left')
        df_left_merge['amount'] = df_left_merge['amount'].replace(np.nan, 0)
        df_left_merge['balance'] = df_left_merge['total_amount'] - df_left_merge['amount']
        return df_left_merge

    def delete_fees_details(self,fees_id):
        """
        Delete fees detail in the system
        :return:
        """
        result = db.session.query(StudentFeesDetails).filter(
                StudentFeesDetails.id ==fees_id

        ).delete()
        db.session.commit()
        return result


