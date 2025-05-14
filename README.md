# Blackjack Game

Hello, and welcome to my text-based version of the game of Blackjack, aka 21. If you are not familiar with it, the goal of the game is for the player to add up their cards to the largest number without going over 21.

## Basic Rules

All of the cards from two to ten count as their face value. The Jack, King, and Queen each count as ten. Now, an ace is a special card because, by default, it counts as 11. However, if an ace is drawn and the player's or dealer's cards add up to more than 21, the ace counts as 1.

## How it works

In this version of the game, the player will be playing against the computer, which will be the dealer. The computer will deal two cards to the player and to itself. The computer's first card is revealed, but its second is concealed. The player can see their cards and their current score. If the player is dealt two cards that add up to 21 (ace + 10), the player immediately wins with Blackjack. If not, the player has to decide whether to get another card or to pass. If the player's cards add up to more than 21, they lose immediately. When the player decides not to get another card, the dealer will check to see if its two cards add up to 21 (ace + 10). If so, the player loses because the computer has Blackjack. If not, the computer will keep drawing cards unless its score goes over 16. Afterward, the player's and computer's final hand will be revealed. If the computer's score goes over 21, the player wins. If the computer has a final hand that is greater than the player's final hand and is less than 21, the player loses. But if the player has a final hand that is greater than the computer's final hand and is less than 21, the player wins. If the player's final hand is equal to the computer's final hand, it's a draw. I have included the project's flow chart as a PDF document, so feel free to take a look.

## Considerations

For the deck of cards, I used a list containing 13 numbers just to keep things simple. It includes the number 11 that represents an ace, numbers 2 through 10 representing the face value of the cards in a deck, and three more 10s, each representing a Jack, a Queen, and a King. This means that the number 10 is four times more likely to be drawn compared to other cards. Take note that once a card is drawn, it is not removed from the deck. This means that each card in the deck has an equal chance of occurring. Also, there is no Joker as part of the cards in the deck.

## How to play
Just run the code and enjoy the game.
