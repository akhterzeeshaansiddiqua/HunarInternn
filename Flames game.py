# flames_game.py

def remove_common_letters(name1, name2):
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()

    name1_list = list(name1)
    name2_list = list(name2)

    for letter in name1[:]:
        if letter in name2_list:
            name1_list.remove(letter)
            name2_list.remove(letter)

    count = len(name1_list) + len(name2_list)
    return count

def flames_result(count):
    flames = ["Friends", "Lovers", "Affectionate", "Marriage", "Enemies", "Siblings"]

    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        if split_index >= 0:
            flames = flames[split_index + 1:] + flames[:split_index]
        else:
            flames = flames[:len(flames)-1]
    return flames[0]

def main():
    print("Welcome to the FLAMES Game!")
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")

    count = remove_common_letters(name1, name2)
    result = flames_result(count)

    print(f"\nThe relationship between {name1} and {name2} is: {result}!")

if __name__ == "__main__":
    main()
