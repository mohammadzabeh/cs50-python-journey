# ask user their name.
name = input("what's your name? ")
# capitalize user's name
# title= capializes every word
name = name.title().strip().split(" ")
first, last = name
# say hello to user
print("hello", first)
age = input("how old are you? ")
# remove whitespace from str
age = age.strip()
print("good,", age, "is fine")
job = input("what do you do? ")
job = job.strip()
print("what a great job. " + job + "!")
reason = input("why are you here? ")
reason = reason.strip()
print("well, that's a good one, ", end="")
print(reason, "is great", sep="-")
print("!!!")
happen = input("what the heck is happenning!!!? ")
happen = happen.strip()
print(f"wow that is not good: {happen}")









