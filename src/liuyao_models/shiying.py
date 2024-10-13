def transform(a):
    if a == 0:
        a = 1
    else:
        a = 0
    return a


def shiying(yao1, yao2, yao3, yao4, yao5, yao6):
    if yao3 == yao6 and yao1 != yao4 and yao2 != yao5:
        guagong = str(yao6) + str(yao5) + str(yao4)
        yao6 = "  "
        yao5 = "应"
        yao4 = "  "
        yao3 = "  "
        yao2 = "世"
        yao1 = "  "
    elif yao3 != yao6 and yao1 == yao4 and yao2 == yao5:
        guagong = str(transform(yao3)) + \
            str(transform(yao2)) + str(transform(yao1))
        yao6 = "  "
        yao5 = "世"
        yao4 = "  "
        yao3 = "  "
        yao2 = "应"
        yao1 = "  "
    elif yao3 != yao6 and yao1 == yao4 and yao2 != yao5:
        guagong = str(transform(yao3)) + str(yao2) + str(yao1)
        yao6 = "  "
        yao5 = "  "
        yao4 = "世"
        yao3 = "  "
        yao2 = "  "
        yao1 = "应"
    elif yao3 == yao6 and yao1 != yao4 and yao2 == yao5:
        guagong = str(yao6) + str(yao5) + str(yao4)
        yao6 = "  "
        yao5 = "  "
        yao4 = "应"
        yao3 = "  "
        yao2 = "  "
        yao1 = "世"
    elif yao3 != yao6 and yao1 != yao4 and yao2 == yao5:  # 游魂卦
        guagong = str(yao6) + str(transform(yao5)) + str(yao4)
        yao6 = "  "
        yao5 = "  "
        yao4 = "世"
        yao3 = "  "
        yao2 = "  "
        yao1 = "应"
    elif yao3 == yao6 and yao1 == yao4 and yao2 != yao5:  # 归魂卦
        guagong = str(yao3) + str(yao2) + str(yao1)
        yao6 = "应"
        yao5 = "  "
        yao4 = "  "
        yao3 = "世"
        yao2 = "  "
        yao1 = "  "
    elif yao3 == yao6 and yao1 == yao4 and yao2 == yao5:
        guagong = str(yao6) + str(yao5) + str(yao4)
        yao6 = "世"
        yao5 = "  "
        yao4 = "  "
        yao3 = "应"
        yao2 = "  "
        yao1 = "  "
    elif yao3 != yao6 and yao1 != yao4 and yao2 != yao5:
        guagong = str(yao6) + str(yao5) + str(yao4)
        yao6 = "应"
        yao5 = "  "
        yao4 = "  "
        yao3 = "世"
        yao2 = "  "
        yao1 = "  "
    return yao1, yao2, yao3, yao4, yao5, yao6, guagong
