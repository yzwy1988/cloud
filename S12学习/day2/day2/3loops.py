#!_*_coding:utf-8_*_


# don't make your programs have too many layers
# if you do have that many layers , try to use the function feature .

#in shell , break 2 3
break_flag = False
break_flag2 = False
break_flag3 = False
while not break_flag:
    print("the first layer is running...")
    option=raw_input(">>>[b:back, q:quit,c:continue]:").strip()
    if option == "b":
        break_flag2 = True
    elif option == "q":
        break_flag = True
    else:
        break_flag3,break_flag2 = False,False
    while not (break_flag or break_flag2):
        print("in layer two...")
        option=raw_input(">>>[b:back, q:quit,c:continue]:").strip()
        if option == "b":
            break_flag2 = True
        elif option == "q":
            break_flag = True
        else:
            pass

        while not(break_flag or break_flag2 or break_flag3):
            print("in layer three...")
            option=raw_input(">>>[b:back, q:quit,c:continue]:").strip()
            if option == "b":
                break_flag3 = True
            elif option == "q":
                break_flag = True