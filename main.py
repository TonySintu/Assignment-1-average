y = 0 # Declares varialbe equal to 0
mylist = [] # Declares a list with no elements

print("This program will take the first six numbers you will input and find the average") # Explains what the program does

while True: # Loops forever since boolean 'True' remains unchanged
  try: # Catches + handles exceptions
    mylist.append(int(input("Please enter a number: "))) # Declares y equal to the number the user inputs added to the previous inputted number
    p = input("Type 'done' to get the average: ")
    if p == 'done': 
      break # If the condition is satisfied (when user types 'done') break the loop
  except Exception as e: # Declares variable e as the exception 
    print(e) # Prints out the exception 

y = sum(mylist)/len(mylist)# Divides y by the amount of numbers the user inputted in order to find the average
print("%.2f" %y) # Console prints the average