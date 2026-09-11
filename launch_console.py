name = input('Input username.')
print(f"Welcome to {name}'s Launch Console!")

running = True
while running:
  print('1. About Me')
  print('2. My Goals')
  print('3. Exit')
  choice = input('Input 1-3.')
  if choice == "1":
    print("I'm a student attending the async Elite 101 term for Code2College.")
  elif choice == "2":
    print("I want to build my resume by shipping real projects in my current and future terms at C2C.")
  elif choice == "3":
    print("Goodbye.")
    running = False
  else:
    print("Choose a number from 1, 2, and 3.")

  
