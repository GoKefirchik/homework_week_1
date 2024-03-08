"""+

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    products = [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]

    all_position_sum = 0
    all_position_average_sum = 0

    for product in products:
        one_position_sum = sum(product['items_sold'])
        all_position_sum += one_position_sum
        one_position_average_sum = one_position_sum / len(product['items_sold'])
        all_position_average_sum += one_position_average_sum

        print(f'Всего продаж {product["product"]}: {one_position_sum}')
        print(f'Среднее количество продаж {product["product"]}: {round(one_position_average_sum, 1)}')

    print()
    print(f'Суммарное количесвтво прождаж всех товаров: {all_position_sum}')
    print(f'Среднее количество продаж всех товаров: {round(all_position_average_sum, 1)}')

if __name__ == "__main__":
    main()
