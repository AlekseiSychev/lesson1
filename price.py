def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    delimiter = f'{one} {two}'.upper()
    return delimiter

sentence = get_summ("Learn", "python")
print(sentence)

def format_price(price):
    price = int(price)
    f_price = f'Цена: {price} руб.'
    return f_price

total_price = format_price(56.24)
print(total_price)