import random


def sum_cards(count, card):
    if card == 'V' \
            or card == 'D' \
            or card == 'K' \
            or card == 'D':
        card_value = 10
    elif card == 'A':
        card_value = 11
    else:
        card_value = card
    return count + card_value


def start_game():
    current_key = input('Blackjack.\nEnter any key to start.\nPress \'C\' to exit.\n')

    if current_key != 'c' and current_key != 'C':

        session_player_wins = 0
        session_croupier_wins = 0

        while True:

            croupier_cards = ''
            player_cards = ''
            croupier_count = 0
            player_count = 0

            print('I`ll take first\n')
            cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'V', 'D', 'K', 'A'] * 4

            while True:
                current_key = input('Do you want another card? y/n\n')
                if current_key == 'y':

                    random.shuffle(cards)
                    player_card = cards.pop()
                    random.shuffle(cards)
                    croupier_card = cards.pop()

                    if player_cards == '':
                        player_cards = str(player_card)
                        print('Your card is %s' % player_cards)
                    else:
                        player_cards = player_cards + ' ' + str(player_card)
                        print('Your cards are %s' % player_cards)

                    if croupier_cards == '':
                        croupier_cards = str(croupier_card)
                    else:
                        croupier_cards = croupier_cards + ' ' + str(croupier_card)

                    player_count = sum_cards(player_count, player_card)
                    croupier_count = sum_cards(croupier_count, croupier_card)

                    if player_count >= 21 or croupier_count >= 21:
                        break
                else:
                    break

            print('\nMy cards are   %s (%d)' % (croupier_cards, croupier_count))
            print('Your cards are %s (%d)\n' % (player_cards, player_count))

            # print('My count is   %d' % croupier_count)
            # print('Your count is %d\n' % player_count)

            if player_count == croupier_count:
                if croupier_count > 21:
                    print('I took first. You win!')
                    session_player_wins += 1
                else:
                    print('No winner.\nThank you for playing.')
            else:
                player_win = False
                if player_count == 21:
                    player_win = True
                # elif croupier_count == 21:
                #    print('You lose!' % croupier_count)
                elif croupier_count > 21:
                    player_win = True
                elif player_count > 21:
                    player_win = False
                elif player_count > croupier_count:
                    player_win = True
                # elif player_count < croupier_count:
                if player_win:
                    print('You win!')
                    session_player_wins += 1
                else:
                    print('You lose!')
                    session_croupier_wins += 1

            print('Count of this session is %d:%d (You:Me)' %(session_player_wins, session_croupier_wins))
            current_key = input('Do you want to play again? y/n\n')
            if current_key != 'y':
                break


start_game()
