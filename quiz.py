# on itialise le nombre de chance
nb_de_chances = 3

# on liste nos questions
questions=[
    ["Combien de fois la France a gagné la coupe du monde ? ", "2"],
    ["Quand a été fondé Apple ? ", "1976"],
    ["Qui a fondé SpaceX ? ", "elon musk"]
    ]

print("Voici notre quiz, tu as trois chances !")
q=0
perdu=False

while q < 3: # on boucle pour répondre à nos 3 questions
    question= input(questions[q][0]) # on récupère la question dans la liste questions
    while question != questions[q][1]: # on récupère la réponse dans la liste questions
        nb_de_chances -= 1 # on retire une chance suite à une mauvaise réponse
        print("Dommage ! Il te reste {} chances".format(nb_de_chances))
        if nb_de_chances == 0: # si plus aucune chance c'est perdu et on arrête le quiz
            print("Oh non ! Tu as perdu le jeu...")
            perdu=True
            break
        question = input(questions[q][0])

    if perdu: break # si perdu on arrête le quiz
    
    q += 1 # on passe à la question suivante

if nb_de_chances > 0 and perdu==False:
    print("Bravo ! Tu as gagné le quiz !")