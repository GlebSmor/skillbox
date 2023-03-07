import requests
import json

name = input('Search: ')
response = json.loads(requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + name).text)

try:
    cocktails = [response['drinks'][x] for x in range(0, len(response['drinks']))]
except TypeError:
    print('No drinks found\n')


count = 0
for cocktail in cocktails:
    print(f'{count+1} - {cocktail["strDrink"]}')
    count += 1


num = int(input('\nPick cocktail: '))
count = 0
cocktail = cocktails[num-1]
print(f'\nName: {cocktail["strDrink"]}')
print('Ingredients:')


for ingredient in cocktail:
    if cocktail[ingredient] and 'strIngredient' in ingredient:
        count += 1
        if cocktail["strMeasure" + str(count)]:
            print(f'    {cocktail[ingredient]}: {cocktail["strMeasure" + str(count)]}')
        else:
            print(f'    {cocktail[ingredient]}')

instruction = cocktail['strInstructions'].split('.')

print('\nInstruction:\n')
for string in range(0, len(instruction) - 1):
    instruction[string] = instruction[string].strip() + '.'
print('\n'.join(instruction))
