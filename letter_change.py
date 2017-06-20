def letter_change():
    input_text = input('Input text: ')
    position_index = input('Input index for change: ')
    position_index = int(position_index)
    if position_index <= 0:
        print('Error, need positive number!')
        return False
    symbol = input('Input symbol for change: ')
    if len(symbol) > 1:
        print('Error, need a one symbol!')
        return False
    text_list = input_text.split(' ')
    for word in text_list:
        if position_index <= len(word):
            word = word[:position_index-1] + symbol + word[position_index:]
        print(word, end=' ')


if __name__ == "__main__":
    letter_change()        
