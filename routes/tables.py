from flask import Blueprint, jsonify, request
import pandas as pd
import datetime
from shikshavalley.modules.student_portal.libs.lib_student_details import StudentDetail
from shikshavalley.modules.student_portal.libs.lib_student_fees import StudentFeesDetail
tables = Blueprint('tables', __name__, url_prefix='/tables')

student_detail_obj = StudentDetail()
fees_obj = StudentFeesDetail()

@tables.route("/student_table", methods=['GET'])
def student_table_content():
    df = fees_obj.get_students_balance()
    #Get Student details
    # student_data = student_detail_obj.get_all_students_details()
    # df = pd.DataFrame(student_data)

    #Get class details for mapping class id to class name
    class_data = student_detail_obj.get_all_class_details()
    df_class = pd.DataFrame(class_data)
    df['class_name'] = df['class_id'].map(df_class.set_index('id')['class_name'])
    df = df[['admission_id', 'student_name', 'father_name', 'father_mobile_number', 'class_name','balance']]
    return jsonify({'data': df.to_dict(orient="records")})

@tables.route("/update_student_details", methods=['POST'])
def update_student_details():

    data = request.form.to_dict()
    admission_id = data['user_application_id']
    annual_charges = data['user_annual_charges']
    monthly_fees = data['user_monthly_fees']
    sports_charges = data['user_sports_charges']
    summer_charges = data['user_summer_charges']
    winter_charges = data['user_winter_charges']
    book_charges = data['user_book_charges']
    resp = student_detail_obj.update_student_details(admission_id,annual_charges,
                                                              monthly_fees,sports_charges,summer_charges,
                                                              winter_charges,book_charges)
    return jsonify({'data': "success"})


@tables.route("/fees_table", methods=['GET','POST'])
def fees_table_content():

    #Get fees submitted by students details
    if request.method == 'POST':
        data = request.form.to_dict()
        start_date = data['start_date']
        end_date = data['end_date']
        # fees_data = fees_obj.get_all_fees_details()
        fees_data = fees_obj.get_all_fees_details_by_daterange(convert(start_date),convert(end_date))
        fees_details = []
        for x in fees_data:
            fees_dict = x[0].as_dict()
            fees_dict.update({'student_name': x[1], 'class_id': x[2]})
            fees_details.append(fees_dict)
        df = pd.DataFrame(fees_details)

    # Get class details for mapping class id to class name
    class_data = student_detail_obj.get_all_class_details()
    df_class = pd.DataFrame(class_data)
    df['class_name'] = df['class_id'].map(df_class.set_index('id')['class_name'])
    df.drop(['id','is_active', 'description', 'updated_date', 'class_id'], axis=1, inplace=True)
    df = df[['admission_id', 'student_name', 'class_name', 'amount', 'date']]
    df = df.sort_values(by='date', ascending=False)

    return jsonify({'data': df.to_dict(orient="records")})

# Function to convert string to datetime
def convert(date_time):
    format = '%Y-%m-%d'  # The format
    datetime_str = datetime.datetime.strptime(date_time, format)
    return datetime_str

@tables.route("/delete_fees_details", methods=['POST'])
def delete_fees_details():

    data = request.form.to_dict()
    fees_id = data['rowid']
    resp = fees_obj.delete_fees_details(fees_id)
    return jsonify({'data': "success"})

@tables.route("/inactive_student_details", methods=['POST'])
def inactive_fees_details():

    data = request.form.to_dict()
    application_id = data['user_application_id']
    resp = student_detail_obj.inactive_student_details_by_id(application_id)
    return jsonify({'data': "success"})
