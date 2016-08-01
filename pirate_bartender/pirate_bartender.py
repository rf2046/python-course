import random # I imported this function to choose ingredients.

# pirate_bartender

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

answers = {} # A dictionary to hold answers, True or False, to questions.

for key in questions:

    print(key, "-", questions[key])
    input_key = input("yes (y) or no (n): ")
    
    if input_key == "y" or input_key == "yes":
        answers[key] = True

    #elif input_key == "yes":
    #    answers[key] = True

    # Here, if I chose "y" or "yes", answers[key] would be set "True"     
        
    else:
        answers[key] = False

    # Here, if I chose "No," answers[key] would be set "False."
    # To exclude the parameters set False, I made this loop.

# print("These are the values to confirm that users said yes.")
# for key in answers: # I made this second loop to confirm the values.
#    if answers[key] == True:
#        print(questions[key], ":", answers[key])



print("The ingredients you need are the following!")

for key in answers:
    if answers[key] == True:
        test = random.randint(0, 2)
        # print ('this shows the result of random.randint(0,2)')
        results = ingredients[key][test]

        print (results)











