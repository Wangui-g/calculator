# get user inputs
value1 = float(input("Enter value 1:"))  # convert to float for decimal support
value2 = float(input ("Enter value 2:"))

def get_operator():
 valid_operators = {'+', '-', '*', '/'}

 while True:
    operator = input("Enter an operator (+,-,*,/): ").strip()
    if operator in valid_operators:
        return operator
    else:
        print("Invalid operator! Please enter one of +, -, /, *. ")

# Function to get a valid operator
operator = get_operator()

#perform calculation
if operator == '+':
   result = value1 + value2
elif operator == '-':
   result = value1 - value2
elif operator == '*':
   result = value1 * value2
elif operator == '/':
   #handle division by zero error
   if value2 == 0: 
      result = "Error"
   else:
     result = value1 / value2

 #print result
print(f"Result: {value1} {operator} {value2} = {result}")
  
  



