with open('recipes.txt') as file:
    cook_book = {}
    for dish in file:
        dish_name = dish.strip()
        ingridients_count = int(file.readline().strip())
        ingridient_list = []
        for ingridients in range(ingridients_count):
            ingridient_dict = {}
            ingridient, quantity, measure = file.readline().split(' | ')
            ingridient_dict['ingredient_name'] = ingridient
            ingridient_dict['quantity'] = int(quantity)
            ingridient_dict['measure'] = measure.strip()
            ingridient_list.append(ingridient_dict)
        cook_book[dish_name] = ingridient_list
        file.readline()


# print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    ingridient_list_dict = {}
    for dish in dishes:
        for ingridient_dict in cook_book[dish]:
            if ingridient_dict['ingredient_name'] in ingridient_list_dict:
                ingridient_list_dict[ingridient_dict['ingredient_name']]['quantity'] += (ingridient_dict['quantity'] * person_count)
            else:
                ingridient_list_dict[ingridient_dict['ingredient_name']] = {}
                ingridient_list_dict[ingridient_dict['ingredient_name']]['measure'] = ingridient_dict['measure']
                ingridient_list_dict[ingridient_dict['ingredient_name']]['quantity'] = ingridient_dict['quantity'] * person_count
    return ingridient_list_dict

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(get_shop_list_by_dishes(['Омлет', 'Омлет-проверка'], 1))