# -*-coding:utf-8-*-
# author:shen
# DATE:2016/1/28


shop_list = [
    ('iphone6s', 5299),
    ('coffee', 30),
    ('Macbook', 11000),
    ('coffee', 30),
    ('CookBook', 50),
    ('NB', 780)
]
shopping_cart = []
break_flag = False
while not break_flag:
    for index, i in enumerate(shop_list):
        print(index, i[0], i[1])
    user_choice = input("[Q:quit,check,pay]what do you want to buy?:").strip()
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice < len(shop_list) and user_choice > 0:
            shopping_cart.append(shop_list[user_choice])
            print("\033[32;1mJust added [%s,%s] in to your shopping cart\033[0m" %(shop_list[user_choice]))
        else:
            print("\033[31;1mProduct [%s] is not exist!\033[0m")
    elif user_choice =="check":
        total_price = 0
        print("\033[34;1mYou have bought below products...:\-33[0m")
        for index, p in enumerate(shopping_cart):
            print(index,p)
            total_price += p[1]
        print("Total Price:"%total_price)
