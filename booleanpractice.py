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


#Collect answers to four different statements using variables ans1, ans2, ans3, and ans4:


#Once you've collected answers, write four different compound statements (different combinations
#of and/or, and st1/st2/st3/st4) and their calculated boolean values (similar to lines 12 and 13)


#Write two different 'not' statements with their calculated boolean values (like line 14)