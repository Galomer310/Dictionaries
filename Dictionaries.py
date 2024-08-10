# Challenge 1
word = input("Enter a word: ")
letter_position = {}
for index, letter in enumerate(word):
    if letter in letter_position:
        letter_position[letter].append(index)
    else:
        letter_position[letter] = [index]
print(letter_position)

# Challenge 2
items_dict = {
    "water": 1,
    "Bread": 3,
    "TV": 1000,
    "Fertilizer": 20,
    "Apple": 4,
    "Honey": 3,
    "Fan": 14,
    "Bananas": 4,
    "Pan": 100,
    "Spoon": 2,
    "Phone": 999,
    "Speakers": 300,
    "Laptop": 5000,
    "PC": 1200
}
items_purchase = []
items_could_not_buy = []
money_in_wallet = int(input("how much in your wallet?\n"))
for key, value in items_dict.items():
    if value < money_in_wallet:
        money_in_wallet -= value
        items_purchase.append(key)
        items_purchase.append(value)
    elif value > money_in_wallet:
        items_could_not_buy.append(key)
        items_could_not_buy.append(value)
print(f"items purchased : {items_purchase}")
print(f"items i could not buy : {items_could_not_buy}")
print(f"money left in wallet {money_in_wallet}")

























