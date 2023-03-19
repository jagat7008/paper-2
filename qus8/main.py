#8. Take the input marks from user using input() function and find out the grade of the students. Note the grading will be in this manner – (100 – 91) – A1, (90-81) – A2, (80-71) – B1, (70-61) – B2, (60- 51) – C1 (50-40) – C2 and less than 40 students will ‘Fail’. Also make sure user should input the marks in the range 0<=marks<=100, if user will input some other marks in should print invalid marks
n=int(input("enter student marks:"))
if n>=91 and n<=100:
    print("Your Grade is A1")
elif n>=81 and n<90:
    print("Your Grade is A2")
elif n>=71 and n<80:
    print("Your Grade is B1")
elif n>=61 and n<70:
    print("Your Grade is B2")
elif n>=51 and n<60:
    print("Your Grade is C1")
elif n>=40 and n<50:
    print("Your Grade is C2")
elif n<40:
    print("fail")
else:
     print("Invalid mark")
