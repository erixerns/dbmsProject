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

  # Add expiry to medicine
  conn.execute('''CREATE TABLE MEDICINES
          (M_ID VARCHAR(20) PRIMARY KEY NOT NULL,
    NAME VARCHAR(20) NOT NULL,
          QUANTITY INT NOT NULL,
          PRICE INT NOT NULL);''')

  # Duration should be in seperate table named PatienWards
  conn.execute('''CREATE TABLE WARDS
          (W_ID VARCHAR(20) PRIMARY KEY NOT NULL,
          W_TYPE VARCHAR(30) NOT NULL,
          DURATION INT NOT NULL);''')

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

def insertpat(pid,pname,paddr,psex,pdet):
    conn.execute("INSERT INTO DOCTOR VALUES (?,?,?,?,? )",(pid,pname,paddr,psex,pdet))

def insertmed(mid,mqty,mprice):
    conn.execute("INSERT INTO DOCTOR VALUES (?,?,?)",(mid,mqty,mprice))

def insertward(wid,wtype,wdur):
    conn.execute("INSERT INTO DOCTOR VALUES (?,?,?)",(wid,wtype,wdur))

def insertemp(eid,ename,eaddr,esex,edet):
    conn.execute("INSERT INTO DOCTOR VALUES (?,?,?,?,?)",(eid,ename,eaddr,esex,edet))

def insertrec(rid,app,pat,doc):
    conn.execute("INSERT INTO DOCTOR VALUES (?,?,?,?)",(rid,app,pat,doc))


def select_task_by_docid(docid, conn=conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Doctor WHERE docid=?", (docid,))
    rows = cur.fetchall()
    return rows


def select_task_by_pid(pid, conn=conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Patient WHERE pid=?", (pid,))
    rows = cur.fetchall()
    return rows

def select_task_by_mid(mid, conn=conn):

    cur = conn.cursor()
    cur.execute("SELECT * FROM Medicines WHERE mid=?", (mid,))

    rows = cur.fetchall()


    return rows

def select_task_by_priority(conn, wid):

    cur = conn.cursor()
    cur.execute("SELECT * FROM Wards WHERE wid=?", (wid,))
    rows = cur.fetchall()
    return rows

def select_task_by_eid(conn, eid):

    cur = conn.cursor()
    cur.execute("SELECT * FROM Employee WHERE eid=?", (eid,))

    rows = cur.fetchall()
    return rows

def select_task_by_rid(conn, rid):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Record WHERE rid=?", (rid,))
    rows = cur.fetchall()
    return rows
