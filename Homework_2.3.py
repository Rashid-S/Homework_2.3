# pip instal pyyaml
import json
import yaml
from pprint import pprint

cook_book = {
  'Яичница': [
    {'ingredient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
    ],
  'Стейк': [
    {'ingredient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
    {'ingredient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
    {'ingredient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
    ],
  'Салат': [
    {'ingredient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
    {'ingredient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
    {'ingredient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
    {'ingredient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
    ]
  }

with open('cook_book.json', 'w') as f:
    json.dump(cook_book, f, ensure_ascii=False, indent=2)

with open('cook_book.yml', 'w', encoding='utf-8') as g:
    yaml.dump(cook_book, g, allow_unicode = True)

