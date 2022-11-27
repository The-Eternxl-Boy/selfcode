my_str = input("enter a word")
my_str = my_str.casefold()
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
   print(my_str,"is a palindrome.")
else:
   print(my_str,"is not a palindrome.")