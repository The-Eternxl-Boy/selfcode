# age = int(input("enter age to check: "))
# if age >= 18:
#     print("your are elegible to vote")
# else:
#     print("please wait for "+ str(18-age) +" years to vote")

class AgeCheck(object):
    def __init__(self, age) -> None:
        self.age = age
    def __repr__(self) -> str:
        return "age: " + str(self.age)
    def check_adult(self):
        return True if self.age > 18 else False
    
print(True if AgeCheck(int(input("enter age: "))).check_adult() else False)