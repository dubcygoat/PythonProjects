import random

#Assign a variable name with a value
name = "Emmanuel"

#Assign a variable questions with a value
questions = "Yes" or "No"

#Assign a variable answer with an empty value
answer = ""

#Assign a variable random_number with a value
random_number = random.randint(1,9)
print(random_number)


#Control Flow Implementation
if random_number == 1:
  answer = "Yes-definitely"
elif random_number == 2:
  answer = "it is decidely so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Without a doubt"
elif random_number == 5:
  answer = "Reply hazy, try again"
elif random_number == 6:
  answer = "Ask again later"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer ="outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer ="Error"

#Here is the the output

print(name,"asks:",questions)
print("Magic 8-Ball's answer:", answer)
