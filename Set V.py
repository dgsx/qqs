import csv
def create_csv():
  f=open("emp.csv",'w',newline='')
  wo=csv.writer(f)
  n=int(input("How many records?:"))
  for i in range(n):
    empno=int(input("Enter employee number:"))
    ename=input("Enter Ename:")
    salary=float(input("Enter Salary:"))
    wo.writerow([empno,ename,salary])
  print("Record file created Successfully.")
  f.close()

def display_record():
  f=open("emp.csv",'r')
  ro=csv.reader(f)
  for i in ro:
    if float(i[2])>=5000 and float(i[2])<=15000:
      print(i)
  f.close()
#create_csv()
display_record()
