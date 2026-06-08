import requests
URL=r'http://lms.devilhai.info/'

def create_students(i):
    data={
        "stu_name":f"vishal_{i}",
        "stu_age":"2001-01-01",
        "stu_phone":f"7814598290{i}",
        "stu_email":f"vv21{i}@gmail.com",
        "stu_password":f"vishal123{i}",
        "stu_address":"Aao haveli pe"

    }
    r=requests.post(f"{URL}/student/student-register",data=data,timeout=10)
    print(r.status_code)
for i in range(1,10):
#print(f"{URL}/student/student-register")
    create_students(i)
    print(i)


