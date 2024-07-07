dic = {"木": 1, "火": 2, "土": 3, "金": 4, "水": 5}
EightGua_attribute = {"乾": "金", "坎": "水", "艮": "土", "震": "木", "巽": "木", "离": "火", "坤": "土",
                      "兑": "金"}
rel = ""


def shengke(a, b):
    global rel
    a = dic[a]
    b = dic[b]
    if (a + 1) % 5 == b:
        rel = "生"  # a生b
    elif (a + 2) % 5 == b:
        rel = "克"  # a克b
    elif (a + 4) % 5 == b:
        rel = "被生"  # a被b生
    elif (a + 3) % 5 == b:
        rel = "被克"  # a被b克
    elif a == b:
        rel = "比合"  # a与b比合
    return rel


def liuqin(guagong, yao):
    guagong = EightGua_attribute[guagong]
    ret = shengke(guagong, yao)
    if ret == "生":
        ret = "子孙"
    elif ret == "克":
        ret = "妻财"
    elif ret == "被生":
        ret = "父母"
    elif ret == "被克":
        ret = "官鬼"
    elif ret == "比合":
        ret = "兄弟"
    return ret
