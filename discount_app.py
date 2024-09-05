# def function to calculate discount
def calculate_discount ( price, discount_percent ):
    if (discount_percent >= 20):
        new_price = (price - ((discount_percent / 100) * price))
        print(f'\t -: Discounted price is: {new_price}')
        return
    print(f'\t -: Price without discount is: {price}')


# prompt user for original price and percent
print(f'*' * 50)
print(f'DISCOUNT ON PRICE CALCULATOR for (discount) >= 20%')
print(f'*' * 50)

price = int(input('input item price: '))
discount_percent = int(input('input discount percentage: '))

# call the function and compare 
calculate_discount(price, discount_percent)