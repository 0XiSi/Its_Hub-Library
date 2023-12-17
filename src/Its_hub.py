"""
MIT License

Copyright (c) 2023 uǝ⊥ʞı⊥

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Its_Hub library.
This is a library with Other Libraries! (;
U Can Use This Library For Use Few Other Library. 4 Example:
Faker
CV2
Tkinter
TKHTMLVIEW
...
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
My name is Farbod Parkhooi(Or you can call me Tik Ten)
This is my Github link: https://www.github.com/tik-ten/Its_Hub
Thanks for use.
"""
def Return_error(error, exit_code, line): 
    print(f"""
_____________________________________________________________________________________
We have an error!                                                                   |
                                                                                    |
I think error it's:                                                                 |
{error}                                                                |
                                                                                    |
I think it's in line {line} of Its_Hub Library.                                         |
Now i quit with exit code: {exit_code}                                                        |
From Its_Hub library.                                                               |
____________________________________________________________________________________|
""")
    quit(exit_code)
class Its_Hub():
    print("YOU USING ***Its_Hub*** LIBRARY FOR DO SOMETHING IN THIS CODE.")
    def Faker(target):
        try: from faker import Faker
        except ImportError: Return_error("import error. \nYou most install Faker library with: \npip3 install Faker", 0, 55)
        faker = Faker()
        try:
            if target == "first_name": return faker.first_name()
            elif target == "last_name": return faker.last_name()
            elif target == "name": return faker.name()
            elif target == "phone_number": return faker.phone_number()
            elif target == "address": return faker.address()
            elif target == "profile": return faker.profile()
            elif target == "job": return faker.job()
            elif target == "company": return faker.company()
            elif target == "website": return faker.website()
            elif target == "blood_group": return faker.blood_group()
        except AttributeError: Return_error("Attribute error. Your faker library has a problem.", 0, "58 -> 67")
    class Fake_profile():
        def __init__(self, Gender="M", Company=None, blood_group=None, website=None, username=None, name=None, sex=None, address=None, Job=None, mail=None):
            self.gender = Gender
            self.company = Company
            self.bg = blood_group
            self.website = website
            self.username = username
            self.name = name
            self.sex = sex
            self.address = address
            self.job = Job
            self.mail = mail
        def Create_profile(self):
            from faker import Faker
            faker = Faker()
            profile = faker.profile(sex=f"{self.gender}")
            del profile["ssn"]
            del profile["residence"]
            del profile["current_location"]
            del profile["birthdate"]
            if self.job != None: profile["job"] = self.job
            elif self.company != None: profile["company"] = self.company
            elif self.bg != None: profile["blood_group"] = self.bg
            elif self.website != None: profile["website"] = self.website
            elif self.username != None: profile["username"] = self.username
            elif self.name != None: profile["name"] = self.name
            elif self.sex != None: profile["sex"] = self.sex
            elif self.address != None: profile["address"] = self.address
            elif self.mail != None: profile["mail"] = self.mail
            result = list(profile.values())
            if self.website == None: result[3] = result[3][0]
            return result
        def Create_result(self, result):
            from tkinter import Tk, Frame, Label 
            from tkhtmlview import HTMLLabel
            root = Tk()
            label = HTMLLabel(root, html=f"""
____________________________________________
<br /> Created by <b>Tik Ten</b>
<br />Github: <b>Github.com/tik-ten</b> 
<h3> Information: </h3>
Job: <b>{result[0]}</b> <br />
Company: <b>{result[1]}</b> <br />
Blood group: <b>{result[2]}</b> <br />
Website: <b>{result[3]}</b> <br />
Username: <b>{result[4]}</b> <br />
Name: <b>{result[5]}</b> <br />
Sex: <b>{result[6]}</b> <br />
Address: <b>{result[7]}</b> <br />
Mail: <b>{result[8]}</b> <br /> 
____________________________________________
""")
            label.pack(pady=20, padx=20)
            root.resizable(False, False)
            root.geometry("400x500")
            root.title("Your fake profile is ready!")
            root.mainloop()
    class Mini():
        def Plus(number, plus):
            try: return number + int(plus)
            except: Return_error("Value error. Plus isn't int!", 0, 129)
        def Count(start_number, range_num):
            try: 
                start_number = int(start_number)
                range_num = int(range_num)
            except ValueError: Return_error("Value error. Start_number or range_num isn't int!", 0, 134)
            for i in range(range_num):
                start_number = start_number + 1
            return start_number
