#Prompt the user enter their full name (first and last) and save that to a variable called "name"
name = input("Please enter your first and last name: ")

#Some users have a surname (for example Junior, Senior, II, III, etc.) that they forgot to enter
#Use compound assignment and input to ask the user for a surname and attach it to the end of the
#name variable so it correctly holds their first, last and surname.
name += " " + input("Please enter a surname: ")

#Report back to the user how many characters are in their full name using length and print.
print("You have", len(name), "characters in your name.")

#As a terrible attempt at a multifactor authentication, a program asks for the 5th character of
#the person's name (could even be a space). Report to the user which character is the 5th in their
#name.
#String indexing
print("The fifth character of your name is", name[4]) #Remember 0-indexing!

#It also asks for the last character in the person's name. Report to the user which is their last.
#String indexing
print("The last character of your name is", name[-1]) #Could also use name[len(name) - 1]

#A stock username asks that it starts with the first four letters of their name. Report to the user
#what the first three characters of their name are.
#String slicing without start, with end
print("The first four characters of your name are", name[:4]) #Stops before character in 4th slot!

#The person wants to know what their name would look like if it was shorter. They decide the easiest
#way to do this is to take off characters at the beginning and end of their name. Report to the user
#what their name would be without the first 3 characters and without the last 2 characters.
#String slicing with start and end
print("Your shortened name would be", name[3:-2]) #Starts at index 3 (4th)

#Another terrible authentication asks for the last 4 characters of the user's name. Report to the user
#what the last four characters of their name is.
#String slicing with start, without end
print("The last four characters of your name are", name[-4:])