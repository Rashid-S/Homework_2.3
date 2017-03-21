import json


def get_cook_book():
    with open('cook_book.json', 'r') as f:
        cook_book = json.load(f)
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish.title()]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество персон: '))
    dishes = input('Введите блюдо из расчета на одну персону'
                   '(несколько блюд разделяйте их знаком "/"): ').lower().split(',')
    cook_book = get_cook_book()
    shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
    print_shop_list(shop_list)

if __name__ == "__main__":
    create_shop_list()
