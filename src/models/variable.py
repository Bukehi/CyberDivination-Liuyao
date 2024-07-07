def transform(yao):
    if yao == 0:
        tuple_yao = (1, 1)
    elif yao == 1:
        tuple_yao = (1, 0)
    elif yao == 2:
        tuple_yao = (0, 0)
    elif yao == 3:
        tuple_yao = (0, 1)
    return tuple_yao  ##tuple=(爻,变)；0=阳爻，1=阴爻；0=静爻，1=变爻


def variable(yao):
    if yao == 0:
        yao = 0
    elif yao == 3:
        yao = 1
    elif yao == 1:
        yao = 1
    elif yao == 2:
        yao = 0
    return yao
