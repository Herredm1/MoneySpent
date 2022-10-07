import pandas as pd


file_loc = input('Location of Amazon Data: ')
file = file_loc.replace('"', '')

df = pd.read_csv(f'{file}')

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

print(f"""
The number of Items you Purchased: {items_bought}

The total prices of all items: {round(new_total)}""")

address = df['Shipping Address Street 1']

address_dict = {

}

for add in address:
    if add not in address_dict:
            address_dict.update({f'{add}':1})
    elif add in address_dict:
            address_dict[add] += 1

for key, value in address_dict.items():
    print(f"""
    Address: {key}
    Times: {value}\n""")

input('Press any key to exit.........')