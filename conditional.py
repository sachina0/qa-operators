test_results =input("Enter test results (passed/failed/): ")
if test_results == "passed":
    print("All tests passed successfully.")
elif test_results == "failed":
    print("Some tests have failed. Please review the results.")
else:
   print("Test results are inconclusive. Further investigation is needed.")