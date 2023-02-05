from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from shikshavalley.modules.student_portal.libs.lib_student_details import StudentDetail
from shikshavalley.modules.student_portal.libs.lib_student_fees import StudentFeesDetail
import pandas as pd
import json

admin = Blueprint('admin', __name__)
student_obj = StudentDetail()


@admin.route('/search', methods=['GET', 'POST'])
@login_required
def search():

    if not current_user.admin:
        return redirect(url_for('main.index'))
    filter_class_parameter = ""
    full_name = ""
    father_name = ""
    if request.method == 'GET':
        filter_class_parameter = request.args.get("class")
        full_name = request.args.get("name")
        father_name = request.args.get("father_name")
    if request.method == 'POST':
        filter_class_parameter = request.form['class-choice']
        full_name = request.form['search_input']
    if filter_class_parameter and full_name:
        resp = student_obj.get_student_details_by_class_name(full_name, father_name, filter_class_parameter)
        if resp is None:
            flash("Kindly Enter a valid full name and class")
        else:
            resp=[resp]
            return render_template('studentprofile.html', data=resp)

    return render_template('search.html')

@admin.route('/applicationform', methods=['GET', 'POST'])
@login_required
def applicationform():
    if not current_user.admin:
        return redirect(url_for('main.index'))
    if request.method == 'POST':
        df = pd.DataFrame([request.form.to_dict()])
        resp = student_obj.create_student(df)
        if not resp['status']:
            flash("Student not created")
        else:
            return redirect(f"/search?name={df['student_name'][0]}&class={df['class'][0]}&father_name={df['father_name'][0]}")
    return render_template('applicationform.html')

@admin.route('/fees', methods=['GET','POST'])
@login_required
def studentfees():
    if not current_user.admin:
        return redirect(url_for('main.index'))
    if request.method == 'POST':
        fees_details = request.form.to_dict()
        if not 'request_form_data' in fees_details.keys():
            resp = student_obj.get_student_details_by_class_name(fees_details['search_input'],"",
                                                                 fees_details['class-choice'])
            resp = [resp]
            return render_template('studentprofile.html', data=resp)
        fees_details = json.loads(fees_details['request_form_data'])
        if not fees_details:
            flash("Kindly input fees of student")
        if fees_details['date'] == "" or fees_details['amount'] == "":
            return render_template('search.html')
        application_id = request.form['application_id']
        res = StudentFeesDetail().insert_student_fees(admission_id=application_id,
                                              fees_details=fees_details)
        if res['status']:
            resp = student_obj.get_student_details(application_id)
            if resp is None:
                flash("Kindly Enter a valid Admission Id")
            else:
                resp=[resp]
                return render_template('studentprofile.html', data=resp)

    application_id = request.args.get('application_id')
    resp = student_obj.get_student_details_by_id(application_id)
    if resp is None:
        return render_template('search.html')
    student_name = resp.student_name
    return render_template('fees.html', data={'student_name':student_name,'id':application_id})

@admin.route("/student_table")
@login_required
def student_table():
    if not current_user.admin:
        return redirect(url_for('main.index'))
    return render_template("student_table.html")

@admin.route("/fees_table")
@login_required
def fees_table():
    if not current_user.admin:
        return redirect(url_for('main.index'))
    return render_template("fees_table.html")
