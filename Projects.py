import sqlite3
import re
import sys, os

class Project:
    @classmethod
    def projectScreen(cls,user_id):
        os.system('clear')

        while True:
            print("1-Create Project")
            try:
                userInput = int(input("Please Choose From List Above: "))
            except Exception as e:
                print(e)
            else:
                if userInput == 1:
                    if cls.createProject(user_id):
                        print(f"Project [{title}] is created successfully.")


    @classmethod
    def createProject(cls , user_id):
        try:
            conn = sqlite3.connect('crowd_funding.db')
        except Exception as ex:
            print(ex)
        else:
            while True:
                title = input("Please Enter Project Title: ")
                if bool(re.fullmatch("^[a-zA-Z]+[a-zA-Z0-9]*$", title)):
                    break
                else:
                    print("Project Title Format is incorrect")

            while True:
                details = input("Please Enter Project Details: ")
                if bool(re.fullmatch("^[a-zA-Z]+[a-zA-Z0-9]*$", details)):
                    break
                else:
                    print("Project Details Format is incorrect")

            while True:
                total_target = input("Please Enter Project Details: ")
                if total_target.isnumeric():
                    break
                else:
                    print("Project Total Target Format is incorrect")

            while True:
                start_date = input("Please Enter Project Start Date: ")
                if bool(re.fullmatch("^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$" , start_date)):
                    break
                else:
                    print("Project Start Format is incorrect")

            while True:
                end_date = input("Please Enter Project End Date: ")
                if bool(re.fullmatch("^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$" , end_date)):
                    break
                else:
                    print("Project End Format is incorrect")

            conn.execute(f"INSERT INTO projects (user_id,title,details,total_target,start_date,end_date) \
                    VALUES ({user_id}, '{title}' , '{details}', {total_target} , '{start_date}' , '{end_date}')")
            conn.commit()
            conn.close()
            return True



