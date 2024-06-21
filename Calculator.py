print("\n")

print("\t    ======Let's Calculate Values======")

print("\n")

print("\t======ENTER NUMBERS FOR CALCULATION======")

print("\n\n")

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

print("\n\n")

tuple = ("⁠✿ Enter \"+\" for Addition" , "⁠✿ Enter \"-\" for Subtraction" ,"⁠✿ Enter \"*\" for Multiplication" , "⁠✿ Enter \"/\" for Division" , "⁠✿ Enter \"**\" for Power" )

for x in tuple:
    print(x)

print("\n\n")

operator = input("Enter operator : ")

print("\n\n")

match operator :
    case "+" :
        print("Addition of " , num1 , " + " , num2 , " is : " , (num1+num2))

    case "-" :
        print("Subtraction of " , num1 , " - " , num2 , " is : " , (num1-num2))

    case "*" :
        print("Multiplication of " , num1 , " * " , num2 , " is : " , (num1*num2))

    case "/" :
        print("Division of " , num1 , " / " , num2 , " is : " , (num1/num2))

    case "**" :
        print("Power of " , num1 , " ** " , num2 , " is : " , (num1**num2))

    case _ :
        print("Enter valid number")

print("\n\n")



