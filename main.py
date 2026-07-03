

import random
secret_number =random.randint(1,100)
attempt = 0
print ("you have only 7 chances")
while True:
    guessnum = int (input (" guess a number: "))
    attempt += 1
    if guessnum < secret_number:
        print("bigger number please")
    elif guessnum > secret_number:
         print("say smaller number please")
    else :
        print ("you winn")
        break
    if attempt >= 7:
        print ("you loose your chances")
        break