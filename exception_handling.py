#exception handling in python is error handling in javascript
#uses try-except i.e. try-catch
#methods used are: try, except, finally. else is only used to execute code only if no exceptions occur.

try:
  result = 10 / 0
except ZeroDivisionError as e:
  print(f"Error: {e}")
else:
  print("No errors occured!")
finally:
  print("Execution complete.")
#Output:
#Error: division by zero
#Execution complete.