biology = float (input("input biology mark: "))
chemistry = float (input("input chemistry mark: "))
pyhsics = float (input("input pyhsics mark here: "))

automaticfail = float ((biology <= 40) or (chemistry <= 40) or (physics <= 40))

print automaticfail 
  