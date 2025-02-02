import mysql.connector as sqltor
while True:
    password=open('pass.txt',"r")
    got_pass=password.readline()
    print(got_pass)
    password_w=open('pass.txt',"w")
    # got_pass=password.readline()
    # print(got_pass)

    password_w.write(got_pass)
    got_pass=password.readline()
    print(got_pass)

    try:
        my=sqltor.connect(host='localhost',
            user='root',password=got_pass,
            database='dairy_management')
        break
    except:
        if got_pass=="":
            got_pass=input("""Password not provided
Enter password:-""")
            password_w.write(got_pass)
        else:
            got_pass=input("""Password  provided is not correct
Enter correct password:-""")
            password_w.write(got_pass)
password.close()
