#Declaring variables of different data types
integer_var = 10 #int
float_var = 3.14 #float
string_var = ''Hello'' #string

#Outputting the values of each variable
print (''Integer:'', integer_var)
print (''Float:'', float_var)
print (''String:'', string_var)



#Taking two numbers as input from the user
num1 = float (input(''Enter the first number:''))
num2 = float (input(''Enter the second number:''))

#Calculating sum, difference, product and quotient
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2 if num2 !=0 else ''Undefined (division by zero)''

#Outputting the results
print (''Sum:'', sum_result)
print (Difference:'', difference)
print (Product:'', product)
print (''Quotient:'', quotient)



#Taking a number as input from the user
num = float (input(''Enter the number:''))

#Checking if the number is positive, negative, or zero
if num > 0:
    print (''The number is positive.'')
elif num < 0:
    print (''The number is negative.'')
else:
    print (''The number is zero.'')
    
    
    
#Taking x and y as input from the user
x = float(input(''Enter value for x:''))
y = float(input(''Enter value for y:''))

#Calculating each expression
expression1 = 4 * x * (y+3) + 15 * y
expression2 = (5 * y ** 2 - 144 * x + 2) / (x + y) ** 2
expression3 = (2 + x - 2 * x * y) / (y  / (x + y))

#Outputting the results
print (''Result of expression 1:'', expression1)
print (''Result of expression 2:'', expression2)
print (''Result of expression 3:'', expression3)



#Taking a grade as input from the user 
grade = int (input(''Enter a grade (1-10):''))

#Determining the letter grade based on the input 
if grade > = 9 and grade < = 10:
    letter_grade ='A'
elif grade > = 7 and grade < = 8:
    letter_grade = 'B'
elif grade > = 5 and grade < = 6:
    letter_grade = 'C'
elif grade > = 3 and grade < = 4:
    letter_grade = 'D'
elif grade > = 1 and grade < = 2:
    letter_grade = 'E'
elif grade == 0:
    letter_grade = 'F'
else:
    leter_grade = ''Invalid grade''
    
#Outputting the letter grade
print (''Letter grade:'', letter_grade)