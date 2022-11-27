from statistics import mean
# sub1 = int(input("Enter marks of the first subject: "))
# sub2 = int(input("Enter marks of the second subject: "))
# sub3 = int(input("Enter marks of the third subject: "))
# sub4 = int(input("Enter marks of the fourth subject: "))
# sub5 = int(input("Enter marks of the fifth subject: "))
# avg=(sub1+sub2+sub3+sub4+sub4)/5
# if avg>=90.0:
#     print("Grade: A")
# elif avg>=80.0 and avg<90.0:
#     print("Grade: B")
# elif avg>=70.0 and avg<80.0:
#     print("Grade: C")
# elif avg>=60.0 and avg<70.0:
#     print("Grade: D")
# else:
#     print("Grade: F")

average = mean([int(input("Enter Marks of Subject [" + str(i + 1) + "]: "), 10) for i in range(5)])
grade = None
if average >= 90.0:
    grade = "A"
elif average >= 80.0:
    grade = "B"
elif average >= 70.0:
    grade = "C"
elif average >= 60.0:
    grade = "D"
else:
    grade = "F"

print(grade)