source = ("Enter the name of source file: ")
output = ("Enter the output file name: ")

with open(source , "w") as f:
  text = input("Enter the text: ")
  f.write(text)

with open(source , "r") as f1:
  data = f1.read()

  new_data = ""

for ch in data:
  if  ch == ".":
    new_data += ","
  elif ch.islower():
    new_data += ch.upper()
  elif ch.isupper():
    new_data += ch.lower()
  else:
    new_data += ch

  with open(output , "w") as f2:
    f2.write(new_data)

with open(output , "r") as f3:
  print("The data is output file is : " ,f3.read())
