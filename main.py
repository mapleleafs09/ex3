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
            ingridient_dict['quantity'] = quantity
            ingridient_dict['measure'] = measure
            ingridient_list.append(ingridient_dict)
        cook_book[dish_name] = ingridient_list
        file.readline()


print(cook_book)