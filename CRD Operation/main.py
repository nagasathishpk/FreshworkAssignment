import json
import threading
import time
def home(no):
    peoples={
        "people 0":{"name":"Nagasathish",
        "age":21,
        "dept":"ECE"},
        "people 1":{"name":"Ragul",
        "age":21,
        "dept":"ECE"}
    }
    obj = json.dumps(peoples) 
    with open("data.json","w") as f:
        f.write(obj)
    with open("data.json","r") as read:
        data = json.load(read)
    while(1):
        time.sleep(3)
        command = int(input('USER {}--> Enter 1 For Read or 2 For Update or 3 For Delete or 4 For exit  :\n'.format(no)))
        if(command==1):
            print("USER{} data--> {}\n".format(no,data))
            time.sleep(1)
        elif(command==2):
            C=0
            for _ in data:
                C=C+1
            name,age,dept=input("USER {}->Enter Name,Age,Dept: ".format(no)).split(",")
            data["people {}".format(C)]={
                "name":"{}".format(name),
                "age":int(age),
                "dept":"{}".format(dept)
            }
            app=json.dumps(data)
            with open("data.json","w") as read:    
                read.write(app)
        elif(command==3):
            C=0
            d=0
            for _ in data:
                C=C+1
            if(C>0):
                d=C-1
            delete=int(input("From User{}--> Enter number from 0-{} to Delete : ".format(no,d)))
            for i in range (delete,d):
                j=i+1
                data["people {}".format(i)]=data["people {}".format(j)]
            del data["people {}".format(d)]
            app=json.dumps(data)
            with open("data.json","w") as read:    
                read.write(app)
        elif(command==4):
            print("USER {} exited from DataBase".format(no))
            break
        
threads=[]
N=int(input("Enter No.of USERS : "))
for i in range(N):
    t=threading.Thread(target=home,args=[i])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()