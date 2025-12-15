class Chrome:
   def run_test(self):
      print("test chrome")

class Brave:
      def run_test(self):
          print("tect brave")
      
for browser in (Chrome(),Brave()):
   browser.run_test