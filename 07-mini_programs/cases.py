# Match–Case 
# It is used to compare a value against multiple patterns and execute the matching block of code, similar to a switch-case statement in other programming languages.

# Example 1
x= int(input("enter any number : "))

match x:
    case 0:
        print("value of x is 0")
    case 1:
        print("value of x is 1")
    case 2:
        print("value of x is 2")
    case 3:
        print("value of x is 3")
    case _ :
        print("invalid")

# Example 2

day = int(input("enter the day(1-7) : "))

match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thrusday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case _:
        print("invalid day")
