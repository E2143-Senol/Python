if input("Do you have a severe chronic disease? yes or no") == "yes":
    chronic = True
else:
    chronic = False

if input("Is your immune system too weak? yes or no") == "yes":
    immune = True
else:
    immune = False

risk = age or chronic or immune

if risk == True:
    print("You are in risky group")
else:
    print("You are not in risky group")