# -*-coding:utf-8-*-
# author:shen
# DATE:2016/1/20
# 作业二:多级菜单
# 三级菜单
# 可依次选择进入各子菜单
# 所需新知识:列表,字典

# 初始化数据
city_menu = {
    '北京': {'朝阳': ['国贸', '东直门', '望京'],
           '海淀': ['中关村', '五道口', '知春路'],
           '丰台': ['大红门', '方庄', '宋家庄']
           },
    '上海': {'黄浦区': ['外滩', '人民广场', '大世界'],
           '徐汇区': ['徐家汇', '交通大学', '上海南站'],
           '浦东新区': ['陆家嘴', '张江', '浦东机场']
           }}

# print(city_menu.keys())

# 输入城市名称判断是否存在
while True:
    input_city = input('请输入城市名：')
    if input_city not in city_menu.keys():
        print('城市不再列表中，请重新输入！')
        continue
    # 如果存在把城市对应的市区赋值给变量raw_districts
    else:
        districts = city_menu[input_city]
        # 循环遍历市区变量，判断用户输入的市区是否存在
        for item in districts:
            input_districts = input("请输入市区名：")
            if input_districts not in city_menu[input_city].keys():
                print('没有这个市区，请重新输入！')
                continue
            # 输出市区信息，并判断是否继续操作
            else:
                for item in city_menu[input_city][input_districts]:
                    print(item)
            quit = input('是否继续操作,输入Y继续，输入N退出：')
            if quit == 'Y':
                continue
            elif quit == 'N':
                break
                # 是否继续，继续就输入Y，返回输入城市，否则退出
    quit = input('是否继续选择城市, 输入Y继续，输入N退出：')
    if quit == 'Y':
        continue
    elif quit == 'N':
        break
