from Authentication import Authentication
from Projects import Project
import sys, os
def welcomeScreen():
    while True:
        print("1-Register")
        print("2-Login")
        try:
            userInput = int(input("Please Choose From List Above: "))
        except Exception as e:
            print(e)
        else:
            if userInput == 1:
                if Authentication.register():
                    print("You can login now")
            elif userInput == 2:
                user = Authentication.login()
                if user:
                    user_id = user[0]
                    print("Logged In")
                    Project.projectScreen(user_id)
                else:
                    print("user is not exists.")


welcomeScreen()