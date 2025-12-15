class Laptop:
   def laptop_on(self):
      print("lapt on")

      l = Laptop
      l.laptop_on


      #inheritence
      class User:
         def login(self):
            print("user login")

      class Admin(User):
         def delete_user(self):
            print ("user delete")

a = Admin()
a.login
a.delete_user