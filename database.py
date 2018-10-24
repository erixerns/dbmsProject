import sqlite3

conn = sqlite3.connect('hospital.db', check_same_thread=False)

def createTable():
  conn.execute('''CREATE TABLE DOCTOR
          (DOCTORID VARCHAR(20) PRIMARY KEY NOT NULL,
          DOCTORNAME VARCHAR(30) NOT NULL,
          SPECIALIZATION VARCHAR(20) NOT NULL,
          DOCTORTYPE VARCHAR (20) NOT NULL);''')

  conn.execute('''CREATE TABLE PATIENT
          (P_ID VARCHAR(20) PRIMARY KEY NOT NULL,
          P_NAME VARCHAR(30) NOT NULL,
          P_ADDRESS VARCHAR(20) NOT NULL,
          P_SEX VARCHAR (20) NOT NULL,
          P_DETAILS VARCHAR (50));''')

  conn.execute('''CREATE TABLE MEDICINES
          (M_ID VARCHAR(20) PRIMARY KEY NOT NULL,
    NAME VARCHAR(20) NOT NULL,
          QUANTITY INT NOT NULL,
          PRICE INT NOT NULL
    EXPIRY DATE NOT NULL);''')

  conn.execute('''CREATE TABLE WARDS
          (W_ID VARCHAR(20) PRIMARY KEY NOT NULL,
          W_TYPE VARCHAR(30) NOT NULL);''')

  conn.execute('''CREATE TABLE PATIENTWARDS
          (W_ID VARCHAR(20),
          P_ID VARCHAR(20),
          DURATION INT NOT NULL,
    FOREIGN KEY (W_ID) REFERENCES WARDS(W_ID),
    FOREIGN KEY (P_ID) REFERENCES PATIENT(P_ID));''')

  conn.execute('''CREATE TABLE EMPLOYEE
          (E_ID VARCHAR(20) PRIMARY KEY NOT NULL,
          E_NAME VARCHAR(30) NOT NULL,
          E_ADDRESS VARCHAR(20) NOT NULL,
          E_SEX VARCHAR (20) NOT NULL,
          E_DETAILS VARCHAR (50));''')

  conn.execute('''CREATE TABLE RECORD
          (R_ID VARCHAR(20) PRIMARY KEY NOT NULL,
          APPOINTED VARCHAR(30) NOT NULL,
          PATIENT VARCHAR(20) NOT NULL,
          DOCTOR VARCHAR (20) NOT NULL,
          FOREIGN KEY (PATIENT) REFERENCES PATIENT(P_ID),
          FOREIGN KEY (DOCTOR) REFERENCES DOCTOR(DOCTORID));''')


def insertdoc(docid,dname,dspl,dtype):
    conn.execute("INSERT INTO DOCTOR VALUES (?,?,?,? )",(docid,dname,dspl,dtype))
    conn.commit()

def insertpat(pid,pname,paddr,psex,pdet):
    conn.execute("INSERT INTO PATIENT VALUES (?,?,?,?,? )",(pid,pname,paddr,psex,pdet))
    conn.commit()
def insertmed(mid,mqty,mprice,expiry):
    conn.execute("INSERT INTO MEDICINES VALUES (?,?,?,?)",(mid,mqty,mprice,expiry))
    conn.commit()
def insertward(wid,wtype):
    conn.execute("INSERT INTO WARDS VALUES (?,?)",(wid,wtype))
    conn.commit()
def insertpatward(pwid,ppid,pwdur):
    conn.execute("INSERT INTO PATIENTWARDS VALUES (?,?,?)",(pwid,ppid,pwdur))
    conn.commit()
def insertemp(eid,ename,eaddr,esex,edet):
    conn.execute("INSERT INTO EMPLOYEE VALUES (?,?,?,?,?)",(eid,ename,eaddr,esex,edet))
    conn.commit()
def insertrec(rid,app,pat,doc):
    conn.execute("INSERT INTO RECORD VALUES (?,?,?,?)",(rid,app,pat,doc))
    conn.commit()

def select_task_by_docid(docid, conn=conn):
  cur = conn.cursor()
  cur.execute("SELECT * FROM Doctor WHERE doctorid=?", (docid,))
  rows = cur.fetchall()
  return rows
 

def select_task_by_pid(p_id, conn=conn):
  cur = conn.cursor()
  cur.execute("SELECT * FROM Patient WHERE p_id=?", (p_id,))
  rows = cur.fetchall()
  return rows
 
def select_task_by_mid(m_id, conn=conn):
  cur = conn.cursor()
  cur.execute("SELECT * FROM Medicines WHERE m_id=?", (m_id,))
  rows = cur.fetchall()
  return rows
 
def select_task_by_priority(w_id, conn=conn):
  cur = conn.cursor()
  cur.execute("SELECT * FROM Wards WHERE w_id=?", (w_id,))
  rows = cur.fetchall()
  return rows 

def select_task_by_eid(e_id, conn=conn):
  cur = conn.cursor()
  cur.execute("SELECT * FROM Employee WHERE e_id=?", (e_id,))
  rows = cur.fetchall()
  return rows

def select_task_by_rid(r_id, conn=conn):
  cur = conn.cursor()
  cur.execute("SELECT * FROM Record WHERE r_id=?", (r_id,))
  rows = cur.fetchall()
  return rows

  
def select_all_doctors(conn=conn):
  cur = conn.cursor()
  cur.execute("SELECT * FROM DOCTOR")

  rows = cur.fetchall()

  return rows

def select_all_patient(conn=conn):
    
  cur = conn.cursor()
  cur.execute("SELECT * FROM Patient")

  rows = cur.fetchall()

  return rows

def select_all_medicines(conn=conn):
    
  cur = conn.cursor()
  cur.execute("SELECT * FROM Medicines")

  rows = cur.fetchall()

  return rows

def select_all_wards(conn=conn):
    
  cur = conn.cursor()
  cur.execute("SELECT * FROM Wards")

  rows = cur.fetchall()

  return rows

def select_all_employee(conn=conn):
    
  cur = conn.cursor()
  cur.execute("SELECT * FROM Employee")

  rows = cur.fetchall()

  return rows

def select_all_record(conn=conn):
    
  cur = conn.cursor()
  cur.execute("SELECT * FROM Record")

  rows = cur.fetchall()

  return rows

