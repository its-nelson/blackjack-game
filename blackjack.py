import random
from blackjack_logo import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def blackjack():
    def hit():
        """Returns a random card from the deck."""
        card_dealt = random.choice(cards)
        return card_dealt

    def make_ace_1(list_of_cards):
        """Makes ace a 1 when the player's and computer's total is over 21."""
        if list_of_cards[-1] == 11 and sum(list_of_cards) > 21:
            list_of_cards[-1] = 1

    player_cards = [hit(), hit()]
    make_ace_1(player_cards)

    computer_cards = [hit(), hit()]
    make_ace_1(computer_cards)

    def display_scores():
        """Displays the player's current score and the computer's first card."""
        print(f"Your cards: {player_cards}, current score: {sum(player_cards)}\nComputer's first card: {computer_cards[0]}\n")

    def display_final_hand():
        """Display's both the player's and computer's final hand."""
        print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}\nComputer's final hand: {computer_cards}, final score: {sum(computer_cards)}")

    def draw_card(list_of_cards):
        """The player or computer draws a card."""
        for card in range(0, 1):
            list_of_cards.append(hit())

    def computer_has_blackjack():
        """Checks if the computer has Blackjack."""
        if 11 in computer_cards and 10 in computer_cards:
            return True
        return None

    decision = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if decision == "y":
        print("\n" * 22)
        print(logo)
        display_scores()
        #Check if player has Blackjack (Ace + 10)
        if 11 in player_cards and 10 in player_cards and not computer_has_blackjack():
            display_final_hand()
            # If player gets Blackjack, they win (unless the computer also has Blackjack)
            print("Win with a Blackjack 🤑\n")
        else:
            another_card = True
            while another_card:
                option = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if option == "y":
                    draw_card(player_cards)
                    # If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
                    make_ace_1(player_cards)
                    display_scores()
                    #Game ends immediately when user score goes over 21.
                    if sum(player_cards) > 21:
                        another_card = False
                        display_final_hand()
                        #Player loses because their final hand was over 21.
                        print("You went over. You lose 😓\n")
                elif option == "n":
                    another_card = False
                    display_scores()
                    #Check if computer has Blackjack (Ace + 10)
                    if computer_has_blackjack():
                        display_final_hand()
                        # If computer gets Blackjack, the player loses even if they also have Blackjack.
                        print("Lose, opponent has Blackjack 😔\n")
                    else:
                        while sum(computer_cards) < 17:
                            draw_card(computer_cards)
                            #If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
                            make_ace_1(computer_cards)
                        display_final_hand()
                        #Computer loses because its final hand was over 21.
                        if sum(computer_cards) > 21:
                            print("Opponent went over. You win 😆\n")
                        #Computer beats player by a final hand that is less than 21
                        elif sum(computer_cards) <= 21 and sum(computer_cards) > sum(player_cards):
                            print("You lose 😣\n")
                        #Player beats computer by a final hand that is less than 21.
                        elif sum(player_cards) <= 21 and sum(player_cards) > sum(computer_cards):
                            print("You win 😂\n")
                        #Player's final hand is equal to the computer's final hand.
                        elif sum(player_cards) == sum(computer_cards):
                            print("Draw 🤝\n")
        blackjack()
    elif decision == "n":
        print("Exited game.")
blackjack()
