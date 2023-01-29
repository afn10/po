import getpass

CorrectUsername = "critikal"
CorrectPassword = "a" 

loop = 'true'
while (loop == 'true'):

    username = raw_input("masukan username kamu: ")

    if (username == CorrectUsername):
        loop1 = 'true'
        while (loop1 == 'true'):
            password = getpass.getpass("password kamu: ")
            if (password == CorrectPassword):
                print "Login berhasil! " + username
                loop = 'false'
                loop1 = 'false'
            else:
                print "Password salah!"

    else:
        print "Username salah!"
