class Student:
   def __init__(self,username,address ):
       self.username = username
       self.address = address

   def greet_user(self):
       print("Hello, " + self.username + "! Welcome to the class.")  

   def address_info(self):
       print("Address:", self.address) 

raminfo = Student("Ramin","Kathmandu")
raminfo.greet_user()