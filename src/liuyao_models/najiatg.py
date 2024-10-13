def najiatg(gua, place):
    if gua == 1:
        if place == 0:
            HS_num = 1
        else:
            HS_num = 9
    elif gua == 2:
        HS_num = 5
    elif gua == 3:
        HS_num = 3
    elif gua == 4:
        HS_num = 7
    elif gua == 5:
        HS_num = 8
    elif gua == 6:
        HS_num = 6
    elif gua == 7:
        HS_num = 4
    elif gua == 8:
        if place == 0:
            HS_num = 2
        else:
            HS_num = 0
    return HS_num
