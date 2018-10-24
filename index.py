from flask import Flask, render_template, request
from database import *

app = Flask(__name__)
try:
  createTable()
except sqlite3.OperationalError:
  print("Table already exists!")

@app.route("/")
def renderHome():
  return render_template("home.html")

@app.route("/admin")
def renderAdmin():
  doctorDetails = select_all_doctors()
  print(doctorDetails)
  return render_template("admin.html", doctorDetails=doctorDetails)

@app.route("/create/<table>", methods=['POST'])
def create(table):
  print("Create: ", table)
  if table == 'doctor':
    doctorID = request.form['form-id-doctor']
    doctorPass = request.form['form-password-doctor']
    doctorName = request.form['form-name-doctor']
    doctorSpecialization = request.form['form-specialization-doctor']
    doctorType = request.form['form-type-doctor']
    if(doctorID=='' or doctorName=='' or doctorPass=='' or doctorSpecialization=='' or doctorType==''):
      return "Error: Fields cannot be empty"
    
    insertdoc(doctorID, doctorName, doctorSpecialization, doctorType)
    print(select_task_by_docid(doctorID))

  elif table == 'patient':
    patientID = request.form['form-id-patient']
    patientPassord = request.form['form-password-patient']
    patientName = request.form['form-name-patient']
    patientSex = request.form['form-sex-patient']
    patientAddress = request.form['form-address-patient']

    insertpat(patientID, patientName, patientAddress, patientSex, '')
  elif table=='ward':
    wardID = request.form['form-id-ward']
    wardType = request.form['form-type-ward']
  else:
    return "Error: Uknown Table!"
  return table

if __name__ == "__main__":
  app.run(port=80, debug=True)