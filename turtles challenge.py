import turtle
from turtle import *
import random

# Initialisation du jeu
ts = turtle.getscreen()
ts.clear()
ts.bgpic("champcourse2.gif")

ts.title("Bienvenue à la course des tortues !")
ts.setup(width=1400, height=800, startx=0, starty=0)



# Déclarez les 5 tortues et positionnez-les sur leurs hexagones respectifs
Michelangelo = Turtle()
Leonardo = Turtle()
Raphael = Turtle()
Splinter = Turtle()
Donatello = Turtle()

Michelangelo.color("Orange")
Michelangelo.shape('turtle')
Leonardo.color("Deep Sky Blue")
Leonardo.shape('turtle')
Raphael.color("Red")
Raphael.shape('turtle')
Splinter.color("Dark Slate Grey")
Splinter.shape('turtle')
Donatello.color("Purple")
Donatello.shape('turtle')

Michelangelo.up()
Leonardo.up()
Raphael.up()
Splinter.up()
Donatello.up()

Michelangelo.goto(-650, 330)
Leonardo.goto(-650, 165)
Raphael.goto(-650, 0)
Splinter.goto(-650, -150)
Donatello.goto(-650, -310)

Michelangelo.down()
Leonardo.down()
Raphael.down()
Splinter.down()


# Demander de saisir dans la console les prédictions des joeurus 1 et 2 dans le format 1,2,3
predicition = input("Quelles sont vos prédictions ? (ex: 1,2,3,4,5) : ")
predicition = predicition.replace(" ", "").replace(",", "")
listPrediction = list(predicition)

print(listPrediction)

# A l'aide d'une boucle while, faire courir les tortues en tirant un nombre entre 0 et 5 qui représente le nombre de pixels du déplacement vers la droite
while Michelangelo.pos() != "(650, 330)":
    Michelangelo.forward(random.randint(1, 5))


# Comparer les résultats de la course avec les pronostics des joueurs 
# et afficher le résultat de la course
# et le joueur gagnant avec la tortue arbitre et l'instruction turtle.Write à la position 0,0
# A IMPLEMENTER



turtle_arbitre = turtle.Turtle()
turtle_arbitre.goto(0,0)
turtle_arbitre.color("Black")
turtle_arbitre.write("Le joueur 1 à gagné", move=True, align="left", font=("Arial", 16, "normal"))



turtle.mainloop()



