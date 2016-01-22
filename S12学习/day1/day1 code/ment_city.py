# -*-coding:utf-8-*-
# author:shen
# DATE:2016/1/20
# 作业二:多级菜单
# 三级菜单
# 可依次选择进入各子菜单
# 所需新知识:列表,字典


city_dict = {
    '北京': {'朝阳': ['国贸', '东直门', '望京'], '海淀': ['中关村', '五道口', '知春路'], '丰台': ['大红门', '方庄', '宋家庄']},
    '上海': {'黄浦区': ['外滩', '人民广场', '大世界'],'徐汇区': ['徐家汇', '交通大学', '上海南站'],'浦东新区': ['陆家嘴', '张江', '浦东机场']}}

print(city_dict.keys())


while True:
    input_city = input("input city:")
    if input_city not in city_dict.keys():
        print("input error!!")
        continue
    else:
        input_city in city_dict.keys()
        city = city_dict[input_city]
        print(city)
        break

