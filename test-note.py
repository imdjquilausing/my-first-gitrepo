sss = []

print("Catch and eat any of these fruits: ('Apple', 'orange','mango','Guave')")
x = int(input("Enter how many fruits you would like to eat :"))

print("Choose a fruit catch. Press A, O, M or G")

for i in range(x):
  fruit = input(f"Fruit {i + 1} of {x} :" )  
  if fruit == 'A' or fruit == 'a':
    sss.append("Apple")
  elif fruit == 'O' or fruit == 'o':
    sss.append("orange")
  elif fruit == 'M' or fruit == 'm':
    sss.append("Mango")
  elif fruit == 'G' or fruit == 'g':
    sss.append("Guava")
  else: 
    print("Invalid input")  

print("Your basket now has:" ,sss)

for i in range(x):
  eat = input("Press e to eat the fruit: ")
  sss.pop()

  if not sss:
    print("Stack is empty")  
  else:
    print("Fruit(s) in the basket" , sss)        
