biology = float (input("input biology mark: "))
chemistry = float (input("input chemistry mark: "))
pyhsics = float (input("input pyhsics mark here: "))

automaticfail = float ((biology <= 40) or (chemistry <= 40) or (physics <= 40))

average = float (biology + chemistry + pyhsics)/3

elif grade >= 70:
    print("yay you got a 1st")
elif grade >= 60:
    print("2:1")
elif grade >= 50:
    print("2:2")
elif grade >= 40:
    print("pass")
else:
    print ("fail")