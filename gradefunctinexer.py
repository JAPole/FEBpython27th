student_name = input ("please input student name: ")

hwork = int (input("input homework mark: "))
asses = int (input("input assesment mark: "))
final = int (input("input finalexam mark here: "))


def grade(hwork_mark, asses_mark, final_mark):
    answer = ((hwork_mark + asses_mark + final_mark) / 175)*100
    return answer

finalgrade = grade(hwork, asses, final) 

if finalgrade>= 70:
    print("yay you got a 1st")
elif finalgrade >= 60:
    print("2:1")
elif finalgrade >= 50:
    print("2:2")
elif finalgrade >= 40:
    print("pass")
else:
    print ("fail")
