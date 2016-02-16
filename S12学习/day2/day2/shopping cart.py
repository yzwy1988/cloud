#!_*_coding:utf-8_*_

shop_list = {
    "electronic_devices":{
        "pc":['levnovo',"apple","dell"],
        "mobile":['huawai',"iphone","xiaomi"],
    }
}
print shop_list["electronic_devices"]["mobile"][2]



# display product list
# allow user to buy
# add user's option to shopping cart
# pay

product_list = [
    ('Iphone6sPlus', 6888),
    ('MacBook', 11300),
    ('CookBook', 50),
    ('Coffee', 30),
    ('KindleFire', 1200),
    ('NB', 800),
]
user_asset = 10000

break_flag = False
shopping_cart = []
paid_list = []
while not break_flag:
    for index,i in enumerate(product_list):
        print(index,i[0],i[1])
    user_choice = raw_input("[quit,check,pay]What do you want to buy?:").strip()
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice < len(product_list) and user_choice > -1:
            shopping_cart.append(product_list[user_choice])
            print("\033[32;1mJust added [%s,%s] in to your shopping cart\033[0m" %(product_list[user_choice]))
        else:
            print("\033[31;1mProduct [%s] is not exist!\033[0m")
    elif user_choice == "check":
        total_price = 0
        print("\033[34;1mYou have bought below products...:\033[0m")
        for index,p in enumerate(shopping_cart):
            print(index,p)
            total_price += p[1]
        print("Total Price:\033[31;1m[%s]\033[0m" % total_price)
    elif user_choice == "pay":
        total_price = 0
        print("\033[34;1mYou have bought below products...:\033[0m")
        for index,p in enumerate(shopping_cart):
            print(index,p)
            total_price += p[1]
        print("Total Price:\033[31;1m[%s]\033[0m" % total_price)
        pay_confirm = raw_input("\033[31;1mGoing to pay?\033[0m").strip()
        if pay_confirm == "y":
            money_left = user_asset - total_price
            if money_left > 0:
                paid_list += shopping_cart
                shopping_cart = []
                user_asset = money_left
                print("\033[31;1mYou have just paid[%s], your current balance is [%s]\033[0m" %(total_price,money_left))
                go_confirm = raw_input("press any key to continue shopping!").strip()

            else:
                print("\033[31;1mYour current balance is [%s], still need [%s] to pay the whole deal!\033[0m" %(user_asset,total_price-user_asset))

    elif user_choice == "quit":
        if shopping_cart:
            print("You still have some product haven't paid yet!")
        else:
            print("Thanks for comming!")
            break_flag = True