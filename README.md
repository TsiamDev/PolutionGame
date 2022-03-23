# PolutionGame

This is a simple simulation of the polution game - a classroom game depicting the effects of polutant emissions and various polices enacted to mitigate them.

In this instance, there are four factories in four adjacent regions. Each factory, at each round, receives subsidies, produces profit and emits polutants to its' region's atmosphere.

The simulation continues as long as there is at least one ecosystem alive. All the possible combinations of the factories' policies are tested.

Below are presented the results of the simulations

For three factories.

![3](https://user-images.githubusercontent.com/56920806/159654804-c4a84295-2458-46e9-a845-9d9fe69d40c1.png)
![4](https://user-images.githubusercontent.com/56920806/159654813-f8d5e98c-3549-44b7-ab23-d44c4f69a521.png)

For four factories

![1](https://user-images.githubusercontent.com/56920806/159648098-1fb31868-0078-4222-bb6f-c1ed34a83c9b.png)
![2](https://user-images.githubusercontent.com/56920806/159648148-8a139d9a-a6e7-447b-a4fa-8b39824fd76a.png)

Each factory is assumed to be rational and selfish, and has the choicce of either enacting policies to mitigate its' emissions (with a cost of 3) or to be apathetic (with a cost of 1 and also a penalty of 1 to every other factory). 

Below is depicted the normal form of the game (payoff matrices):

For four factories:
(It is a bit difficult to draw the normal form for four factories but I attempt it below)

![5](https://user-images.githubusercontent.com/56920806/159699887-37eba4d7-6cb2-41f2-8c72-40556a7084e5.png)

For three factories

![6](https://user-images.githubusercontent.com/56920806/159699918-cac41afd-27b6-4731-9613-f415e569321c.png)

I know from:
https://eclass.upatras.gr/modules/document/file.php/CEID1154/02-Lecture-Intro_Games_Strategies_Solutions.pdf
(It is in greek - apologies if I find an english source I will cite it here)
that a dominant strategy solution (if exists) is unique for the game. Also, I know that the dominant strategy solution minimizes the cost, so in the case of the n factories, they all remain passive.



