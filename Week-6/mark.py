file=open("marks.data","w")
n=int(input("enter a number of students: "))

for i in range(n):
    roll_no=input("enter a roll_no: ")
    name=input("enter a name: ")
    marks=input("enter a marks: ")
    
    file.write(roll_no+" "+name+" "+marks +"" +"\n")
file.close()
print("student details written successfully")
