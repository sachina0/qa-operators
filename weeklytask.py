#1.Create a class named User.
class User:
   def __init__(self, name, email): 
      self.name = name
      self.email = email   

   def display_user(self):
      print("Name:", self.name)
      print("Email:", self.email)   

# Create object and call method
user1 = User("maya", "maya@gmail.com")
user1.display_user()



class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login_check(self):
        if self.username == "qa_user" and self.password == "qa123":
            print("Login Passed")
        else:
            print("Login Failed")


# Valid credentials
login1 = Login("qa_user", "qa123")
login1.login_check()

# Invalid credentials
login2 = Login("qa_user", "wrongpass")
login2.login_check()
