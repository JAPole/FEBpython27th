ISBN = input ("Please enter 12 digits of ISBN :  ")
sum1 = 0
sum2 = 0

for ISBNodd in range(1,12,2):

    sumodd = int(ISBN[ISBNodd]) * 3
    total1 = total1       + sumodd  

