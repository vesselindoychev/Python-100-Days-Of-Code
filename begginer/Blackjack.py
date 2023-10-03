import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 'K', 'J', 'Q', 10]

card_points = {
    'K': 10,
    'J': 10,
    'Q': 10,
}


def deal_cards_for_computer(cards):
    score = sum(cards)
    while True:
        if score < 17:
            current_card = draw_random_cards(1)
            cards.append(current_card[0])
            score = calculate_score(cards)
        else:
            return cards


def draw_random_cards(times):
    result = []
    for i in range(times):
        random_card = random.choice(cards)
        if type(random_card) == str:
            result.append(card_points[random_card])
        else:
            result.append(random_card)
    return result


def calculate_score(cards):
    score = sum(cards)
    if score == 21:
        return 0

    if score > 21:
        if cards[-1] == 11:
            cards.remove(11)
            cards.append(1)
            score = sum(cards)
        return score

    return score


def has_blackjack(score):
    if score == 0:
        return True


def is_score_over_21(score):
    if score > 21:
        return True


def check_score(player_score, computer_score):
    if player_score == computer_score:
        return 'It\'s a draw'
    if player_score == 0:
        return 'Win with a Blackjack'
    if computer_score == 0:
        return 'Lose, opponent has Blackjack'
    if player_score > 21:
        return 'You went over. You lose.'
    if computer_score > 21:
        return 'Opponent went over. You win.'
    if player_score > computer_score:
        return 'You win.'
    if computer_score > player_score:
        return 'You lose.'


flag = False
while True:
    starting_confirmation = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if flag:
        break
    if starting_confirmation == 'y':
        """
        clear console output
        print(logo)
        """
        player_cards = draw_random_cards(2)
        computer_cards = draw_random_cards(2)
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {player_cards}, current score: {player_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if player_score == 0 or computer_score == 0:
            print(f"    Your final hand: {player_cards}, final score: {player_score}")
            print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
            print(check_score(player_score, computer_score))
            continue

        while True:
            get_another_card_conf = input("Type 'y' to get another card, type 'n' to pass: ")
            if get_another_card_conf == 'y':
                current_card = draw_random_cards(1)
                player_cards.append(current_card[0])
                player_score = calculate_score(player_cards)
                print(f"    Your cards: {player_cards}, current score: {player_score}")
                print(f"    Computer's first card: {computer_cards[0]}")
                if is_score_over_21(player_score):
                    print(check_score(player_score, computer_score))
                    break
            else:
                computer_cards = deal_cards_for_computer(computer_cards)
                player_score = calculate_score(player_cards)
                computer_score = calculate_score(computer_cards)
                print(f"    Your final hand: {player_cards}, final score: {player_score}")
                print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
                print(check_score(player_score, computer_score))
                # flag = True
                break

    else:
        break
