
                                     #12Python quiz game

questions =["you killed John ____ dog",  # some simple question on the screen
           "an apple a day keeps ______ away",
           "king of all fruit is ___",
           "meow says a ____"]

options =(("a. man","b. wick", "c. sena", "d. kumar"), #answers for the above question # each q has 4 option to select from
          ("a. Doctor","b. dentist", "c. therapist", "d. rockstar"),
          ("a. fruit","b. apple", "c. mango", "d. orange"),
           ("a. human","b. dog", "c. lion", "d. cat"))

answers = ["b", "a", "c", "d"]          # the correct answer from the options of each q
guesses = []                            # to stores  the answers given by user
player_score = 0                        # to calculate the score
question_num =0  #order number

for question in questions:              # using for loop to get all the questions in te questions-list till none left
    print("!!!!!!!!!!!!!!!!!!!!!")
    print(question)                        #prints each question then below nested loop workss
    for option in options[question_num]:   #argument is passed as to get the index of question from the list of questions
        print(option)                          #then the all the option for the index of option is printed

    guess = input("Enter (a, b, c, d): ").lower()               # it stores the values in the quesses list and .lower to prevent any uppercase
    guesses.append(guess)
    if guess == answers[question_num]:                             #so if the value stored in guesses at index of vriable- question_num are same
        player_score += 1                                              #then 1 point or simply no. is added to the player_score variable
        print("__Correct!__")
    else:
        print("__incorrect__")                                         #else an message is printed with the correct answer:
        print(f"correct answer is {answers[question_num]}")                    # by checking the index value of the answer at variable question_num
    question_num += 1                                                   # and a num is added in the variable questio_num so to increse every other funct using it as index finder
print("---______Result______---")
                                                    # the result page or side
print("answers: ",end=" ")
for answer in answers:                             # printing all the values in the asnswers list mentioned at the start
    print(answer, end=" ")                          # using for loop here as to not get the decoration around as seen in list the string signs " " or the list brackets [ ]
                                                    # in short avoiding symbols
print()
print("guesses: ",end=" ")
for guess in guesses:                               # same as above--answers
    print(guess, end=" ")                             # nd one more thing to get in order on by one using end=" " to get the spaccing right

print()
                                                            #ssome calculation for getiing a score
player_score =int( player_score / (len(questions)) * 100)   # just getting total points in the player_score variabe and rewiting/re--storring the same in the same variable
print(f"your player_score is {player_score}%")

                                    #commenting is time consuming
