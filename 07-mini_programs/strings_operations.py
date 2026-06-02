str1 = str(input("Enter the string 1: "))
str2 = str(input("Enter the string 2: "))
sub_str = str(input("Enter the substring: "))

print("Length of string 1 : ", len(str1))
print("Length of string 2 : ", len(str2))

if str1 == str1[::-1]:
  print("String 1 is palindrome")
else:
  print ("String 1 is not Palindrome")

if str2 == str2[::-1]:
  print("String 2 is palindrome")
else:
  print ("String 2 is not Palindrome")

if sub_str in str1 :
  print ("Substring is present in string 1")
else:
  print ("Substring is not present in string 1")

if sub_str in str2 :
  print ("Substring is present in string 2")
else:
  print ("Substring is not present in string 2")

if str1 == str2:
  print("String 1 and String 2 are same")
else:
  print("String 1 and String 2 are not same")
