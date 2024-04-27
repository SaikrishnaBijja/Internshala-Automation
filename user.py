def read_data():
    email=input("Enter your E-mail Id: ")
    password=input("Enter your Password: ")
    intrests=[]

    print("Enter any five intrests (like python,java)")
    for x in range(1,6):
        intrests.append(input(f"{x}: "))

    with open('data.txt', 'w') as enter:
        enter.write(email+"\n")
        enter.write(password+"\n")
        for intrest in intrests:
            enter.write(intrest+"\n")

def get_data():
    with open("data.txt", 'r') as get:
        info=get.readlines()
        info=[x.replace("\n", '') for x in info]
        email=info[0]
        password=info[1]
        intrest=info[2:]
        return email, password, intrest

    


    

