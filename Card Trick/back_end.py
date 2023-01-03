def lists_formation(complete_list):
    row_A = []
    row_B = []
    row_C = []

    partial_list = complete_list

    for i in range(0, 21, 3):
        row_A.append(partial_list[i])
    for j in range(1, 21, 3):
        row_B.append(partial_list[j])
    for k in range(2, 21, 3):
        row_C.append(partial_list[k])

    return row_A, row_B, row_C


def positioning(row_A, row_B, row_C, correct_column):
    choice = correct_column
    deck_of_cards = []

    if choice == "A":
        for i in row_B:
            deck_of_cards.append(i)
        for j in row_A:
            deck_of_cards.append(j)
        for k in row_C:
            deck_of_cards.append(k)
    if choice == "B":
        for i in row_A:
            deck_of_cards.append(i)
        for j in row_B:
            deck_of_cards.append(j)
        for k in row_C:
            deck_of_cards.append(k)
    if choice == "C":
        for i in row_B:
            deck_of_cards.append(i)
        for j in row_C:
            deck_of_cards.append(j)
        for k in row_A:
            deck_of_cards.append(k)

    return deck_of_cards


def colors():
    return {"white": (255, 255, 255),
            "dark_orange": (201, 90, 10),
            "light_orange": (245, 127, 10),
            "dark_purple": (110, 60, 128),
            "light_purple": (145, 17, 171),
            }


def cards():
    return {'JH': 'jack_of_hearts2.png',
            'QD': 'queen_of_diamonds2.png',
            '3C': '3_of_clubs.png',
            '6C': '6_of_clubs.png',
            '9H': '9_of_hearts.png',
            '7H': '7_of_hearts.png',
            '8H': '8_of_hearts.png',
            '3D': '3_of_diamonds.png',
            '5C': '5_of_clubs.png',
            '8D': '8_of_diamonds.png',
            'AD': 'ace_of_diamonds.png',
            'AC': 'ace_of_clubs.png',
            '5D': '5_of_diamonds.png',
            '10H': '10_of_hearts.png',
            '3H': '3_of_hearts.png',
            '9C': '9_of_clubs.png',
            '9S': '9_of_spades.png',
            '4H': '4_of_hearts.png',
            '9D': '9_of_diamonds.png',
            'JS': 'jack_of_spades2.png',
            '4D': '4_of_diamonds.png',
            '7S': '7_of_spades.png',
            '8C': '8_of_clubs.png',
            '10D': '10_of_diamonds.png',
            '4S': '4_of_spades.png',
            '10C': '10_of_clubs.png',
            'AH': 'ace_of_hearts.png',
            '2H': '2_of_hearts.png',
            '10S': '10_of_spades.png',
            '3S': '3_of_spades.png',
            '5H': '5_of_hearts.png',
            'JD': 'jack_of_diamonds2.png',
            '6D': '6_of_diamonds.png',
            'KH': 'king_of_hearts2.png',
            '7D': '7_of_diamonds.png',
            '6H': '6_of_hearts.png',
            'JC': 'jack_of_clubs2.png',
            '2C': '2_of_clubs.png',
            '8S': '8_of_spades.png',
            'AS': 'ace_of_spades.png',
            'KD': 'king_of_diamonds2.png',
            '5S': '5_of_spades.png',
            'QC': 'queen_of_clubs2.png',
            '6S': '6_of_spades.png',
            'KC': 'king_of_clubs2.png',
            '4C': '4_of_clubs.png',
            'KS': 'king_of_spades2.png',
            'QS': 'queen_of_spades2.png',
            '7C': '7_of_clubs.png',
            '2S': '2_of_spades.png',
            'QH': 'queen_of_hearts2.png',
            '2D': '2_of_diamonds.png',
            }