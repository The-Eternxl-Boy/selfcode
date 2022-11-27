# import telnetlib


# num=int(input("enter number"))

# if num==1:
#     print("one")

# elif num==2:
#     print("two")

# elif num==3:
#     print("three")

# else:
#     print("out of range")           

# 1 - 100 => one - one hundred

n = int(input("n: "))

tens = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety","hundred"]
ones = ["one","two","three","four","five","six","seven","eight","nine","ten"]
teens = ["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]

name = None

if n >= 1 and n <= 10:
    name = ones[n]
elif n >= 11 and n <= 19:
    name = teens[n - 11]
elif n >= 20 and n <= 100:
    t = (n / 10) - 2
    o = (n % 10) - 1
    name = tens[int(t)] + " " + ones[int(o)]
else:
    name = "invalid number"

print(name.strip())