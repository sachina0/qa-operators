class Login:
      def __init__(self, username, password):
         self.__username = username
         self.__password = password

      def get_username(self):
          return self.__username
      
      def set_password(self,new_pass):
         self.__password = new_pass
         return self.__password
user = Login("dfdf","dsds")
print(user.get_username())
print(user.set_password)