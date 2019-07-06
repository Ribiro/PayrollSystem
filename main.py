from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from config import Development, Production
from resources.employees import Employees
import pygal

app = Flask(__name__)
app.config.from_object(Development)
# app.config.from_object(Production)


# create an instance of SQLAlchemy
db = SQLAlchemy(app)

from models.Employees import EmployeesModel
from models.Payrolls import PayrollsModel


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def home():
    employees = EmployeesModel.fetch_all_records()

    # calculate no of employees
    male = 0
    female = 0
    na = 0

    # using list comprehension and count method modify this for loop
    for emp in employees:
        if emp.gender == 'male':
            male += 1
        elif emp.gender == 'female':
            female += 1
        else:
            na += 1
    print(male)
    print(female)
    print(na)

    # create a pie chart
    pie_chart = pygal.Pie()
    pie_chart.title = 'Male vs Female Employees'
    pie_chart.add('Male Employees', male)
    pie_chart.add('Female Employees', female)
    pie_chart.add('Not Applicable', na)
    graph = pie_chart.render_data_uri()
    print(graph)
    return render_template('index.html', wafanyikazi=employees, graph=graph)


@app.route('/payrolls/<int:id>')
def payrolls(id):
    employee = EmployeesModel.fetch_by_id(id)
    return render_template('payroll.html', title='payrolls', mfanyikazi=employee)


@app.route('/delete/<int:id>')
def delete_employee(id):
    EmployeesModel.delete_by_id(id)
    return redirect(url_for('home'))


@app.route('/editemployee/<int:id>', methods=['POST'])
def edit_employee(id):
    name = request.form['name']
    gender = request.form['gender']
    email = request.form['email']
    kra_pin = request.form['kra']
    basic_salary = request.form['basic']
    benefits = request.form['benefits']

    current_user = EmployeesModel.fetch_by_id(id)
    # use and to capture this error
    if EmployeesModel.check_kra_pin(kra_pin) and kra_pin != current_user.kra_pin or \
            EmployeesModel.check_email(email) and email != current_user.email:
        flash("Kra/email already exists")
        return redirect(url_for('home'))

    EmployeesModel.update_by_id(id=id, name=name, gender=gender, email=email, kra_pin=kra_pin, basic_salary=basic_salary, benefits=benefits)
    return redirect(url_for('home'))


@app.route('/newemployee', methods=['POST'])
def create_new_employee():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        email = request.form['email']
        kra_pin = request.form['kra']
        basic_salary = request.form['basic']
        benefits = request.form['benefits']

        if EmployeesModel.check_kra_pin(kra_pin) or EmployeesModel.check_email(email):
            flash("Email/Kra already exists")
            return redirect(url_for('home'))

        emp = EmployeesModel(name=name, gender=gender, email=email, kra_pin=kra_pin, basic_salary=basic_salary, benefits=benefits)
        emp.insert_record()

        return redirect(url_for('home'))

# generate payroll for specific employee
@app.route('/generate/<int:uid>', methods=['POST'])
def generate_payroll(uid):
    month = request.form['month']
    year = request.form['year']
    overtime = request.form['overtime']

    month = month + str(year)
    employee = EmployeesModel.fetch_by_id(uid)

    basic = employee.basic_salary
    benefits = employee.benefits

    mfanyikazi = Employees(basic, benefits)

    gross = mfanyikazi.get_gross_salary()
    nssf = mfanyikazi.get_nssf()
    nhif = mfanyikazi.get_nhif()
    net = mfanyikazi.get_net_salary() + float(overtime)
    payee = mfanyikazi.get_payee()
    personal_relief = mfanyikazi.personal_relief
    sacco_contribution = 0
    pension = 0
    emp_id = uid

    pay = PayrollsModel(month=month, gross_salary=gross, payee=payee, nhif=nhif, nssf=nssf,
                        personal_relief=personal_relief, sacco_contribution=sacco_contribution, pension=pension,
                        net_salary=net, employee_id=emp_id)

    # create a bar chart
    line_chart = pygal.Bar()
    line_chart.title = 'Payroll Summary in %'
    line_chart.x_labels = map(str, range(2019))
    line_chart.add('Month', [month])
    line_chart.add('Gross salary', [gross])
    line_chart.add('PAYE', [payee])
    line_chart.add('NHIF', [nhif])
    line_chart.add('NSSF', [nssf])
    line_chart.add('Relief', [personal_relief])
    line_chart.add('Net Salary', [net])
    bar = line_chart.render_data_uri()
    print(bar)

    try:
        pay.insert_records()
        return redirect(url_for('payrolls', id=uid))

    except:
        flash("Error in saving to the database")
        return redirect(url_for('payrolls', id=uid))


if __name__ == '__main__':
    app.run()
