#Concrete statements are either True or False for a person, making them ideal for working with booleans.
#Use print and input statements to have the user answer True or False to statements you provide.
#Using their responses, utilize 'and' and 'or' to make compound statements and
#determine if they are True or False. Use 'not' to discuss the negation of statements
#Here is an example:
st1 = "I am a teacher"
st2 = "I am a high school student"
print(st1)
ans1 = bool(input("Was this statement True or False for you: "))
print(st2)
ans2 = bool(input("Was this statement True or False for you: "))
print(st1, "and", st2, "is", ans1 and ans2)
print(st1, "or", st2, "is", ans1 or ans2)
print("The negation of", st1, "is", not ans1)

#Write 4 statements as strings and save them using variables st1, st2, st3, and st4:
st1 = "I like math"
st2 = "I like video games"
st3 = "I am a child"
st4 = "I am 25 years old"

#Collect answers to four different statements using variables ans1, ans2, ans3, and ans4:
print(st1)
ans1 = bool(input("Was this statement True or False for you: "))
print(st2)
ans2 = bool(input("Was this statement True or False for you: "))
print(st3)
ans3 = bool(input("Was this statement True or False for you: "))
print(st4)
ans4 = bool(input("Was this statement True or False for you: "))

#Once you've collected answers, write four different compound statements (different combinations
#of and/or, and st1/st2/st3/st4) and their calculated boolean values (similar to lines 12 and 13)
print(st1, "and", st2, "is", ans1 and ans2)
print(st2, "and", st3, "is", ans2 and ans3)
print(st3, "or", st4, "is", ans3 or ans4)
print(st4, "or", st1, "is", ans4 or ans1)

#Write two different 'not' statements with their calculated boolean values (like line 14)
print("The negation of", st1, "is", not ans1)
print("The negation of", st3, "is", not ans3)