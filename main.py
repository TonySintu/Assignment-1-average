print("This program will take the first six numbers you will input and find the average") # Explains what the program does
y = 0 # Declares that y is equal to 0
x = 0 # Declares that x is equal to 0

while True: # Loops forever since boolean 'True' remains unchanged
  try: # Catches + handles exceptions
    y = y + (int(input("Please enter a number: "))) # Declares y equal to the number the user inputs added to the previous inputted number
    p = input("Type 'done' to get the average: ")
    x += 1 # Increases the counter by 1
    if p == 'done': 
      break # If the condition is satisfied (when user types 'done') break the loop
  except Exception as e: # Declares variable e as the exception 
    print(e) # Prints out the exception 
    x -= 1
y = y / x # Divides y by the amount of numbers the user inputted in order to find the average
print("%.2f" %x) # Console prints the average