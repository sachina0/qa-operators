test_results =input("Enter test results (passed/failed/): ")
if test_results == "passed":
    print("All tests passed successfully.")
elif test_results == "failed":
    print("Some tests have failed. Please review the results.")
else:
   print("Test results are inconclusive. Further investigation is needed.")


   tests =["logon", "signup", "logout"]
   for test in tests:
       print("Running test case:", test)


      #try1
test_results={
            "login": "passed",
            "signup": "failed",
            "logout": "passed"      
      }
# for test in test_results:
#    print(test)
#try2
# for test, result in test_results.values():
#     print(result)

    #try3
for test, result in test_results.items():
    print(test,":", result)