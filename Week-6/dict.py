d={
    "unzila":"7654321287",
     "neha":"2345654678",
     "priya":"2343546787"
}
name=input("enter a name: ");
phone=d.get(name)
if name:
    print("phone number are: ",phone)
else:
    print("not found")