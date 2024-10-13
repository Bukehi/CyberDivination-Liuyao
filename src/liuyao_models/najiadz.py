def najiadz(gua, place):
    if place == 0:
        if gua <= 3:
            EB_num1 = 2 * gua - 1
            EB_num2 = EB_num1 + 2
            EB_num3 = EB_num2 + 2
        elif gua == 4:
            EB_num1 = gua - 3
            EB_num2 = EB_num1 + 2
            EB_num3 = EB_num2 + 2
        else:
            EB_num1 = (gua - 4) * 2
            EB_num2 = EB_num1 - 2
            EB_num3 = EB_num2 - 2
    else:
        if gua <= 3:
            EB_num1 = 2 * gua - 1 + 6
            EB_num2 = EB_num1 + 2
            EB_num3 = EB_num2 + 2
        elif gua == 4:
            EB_num1 = gua - 3 + 6
            EB_num2 = EB_num1 + 2
            EB_num3 = EB_num2 + 2
        else:
            EB_num1 = (gua - 4) * 2 + 6
            EB_num2 = EB_num1 - 2
            EB_num3 = EB_num2 - 2
        EB_num1 = EB_num1 % 12
        EB_num2 = EB_num2 % 12
        EB_num3 = EB_num3 % 12
    if EB_num1 < 0:
        EB_num1 += 12
    if EB_num2 < 0:
        EB_num2 += 12
    if EB_num3 < 0:
        EB_num3 += 12
    return EB_num1, EB_num2, EB_num3