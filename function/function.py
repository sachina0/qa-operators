def greet_user():
   print("Hello, QA team")

greet_user()


def test_login(username):
   print("Testing login for:", username)
test_login("sachina")

#funtion with return value
def verify_status(code):
   if code == 200:
       return "Success"
   else:
       return "Failure"
result = verify_status(200)
print(result)


def check_credentials(user, password):
   if user == "admin" and password == "admin123":
      print("Access Granted")
   else:
      print("Access Denied") 
check_credentials("admin", "admin123")

def sum_numbers(a, b):
   return a + b
total = sum_numbers(5, 10)
print("Sum is:", total)

#funtion greeting with name input
def greet_with_name(name):
   print("Hello, " + name + "! Welcome aboard.")
greet_with_name(input("Enter you name: "))

#function age minor check
def is_minor(age):
   if age < 18:
       return "Minor"
   else:
       return "Adult"
minor_status = is_minor(int(input("Enter your age: "))) 
print("Minor or adult:", minor_status)


#lenght of name
def name_length(name):
   return len(name)
length = name_length(input("Enter you name: "))
print("Length of name is:", length)


#function to check even or odd
def check_even_odd(number):
   if number % 2 == 0:
       return "Even"
   else:
       return "Odd"
result = check_even_odd(int(input("Enter number to check even or odd: "))) 
print("The number is:", result)

#verify staus code
def verify_status_code(status_code):
   if status_code == 200:
       return "pass"
   else:
       return "fail"
results = verify_status_code(int(input("Enter status code: ")))
print("Status code verification:", results)