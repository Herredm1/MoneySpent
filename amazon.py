import pandas as pd

file_loc = input('Where is your Amazon account report? (without qoutes) ')

df = pd.read_csv(f'{file_loc}')

total = []
new_total = 0
items_bought = 0

for value in df['Item Total']:
    total.append(value)

sales = [total[i].strip('$') for i in range(len(total))]

for sale in sales:
    new_total += float(sale)

for times in sales:
    items_bought += 1

print(new_total, items_bought)

address = df['Shipping Address Street 1']

address_dict = {

}

for add in address:
    if add not in address_dict:
            address_dict.update({f'{add}':1})
    elif add in address_dict:
            address_dict[add] += 1

for key, value in address_dict.items():
    print(key)
    print(value)

input('Press any key to exit.........')