from models import najiadz
from models import najiatg
from models import variable
from models import shiying
from models import liuqin
from models.dict import Gua
import random
import os
import datetime
import cnlunar

Gua = Gua()


class Divination:
    def __init__(self):
        self.cntime = ""
        self.empty = ""
        self.label = ""

    def __str__(self) -> str:
        return self.label

    def get_cntime(self):
        ### 四值###
        self.now = datetime.datetime.now()
        self.now = str(self.now)
        now_year = self.now[0:4]
        now_month = self.now[5:7]
        now_day = self.now[8:10]
        now_hour = self.now[11:13]
        now_minute = self.now[14:16]
        self.now = self.now[0:10]+"-"+now_hour + \
            "-"+now_minute+"-"+self.now[17:19]
        lunar = cnlunar.Lunar(datetime.datetime(int(now_year), int(now_month),
                                                int(now_day), int(now_hour)),
                              godType='8char')  # 常规算法
        self.year = lunar.year8Char  # 年干支
        self.month = lunar.month8Char  # 月干支
        self.day = lunar.day8Char  # 日干支
        self.twohour = lunar.twohour8Char  # 时干支
        self.cntime = self.year+" "+self.month+" "+self.day+" "+self.twohour

    def get_empty(self):
        ### 旬空###
        HeavenlyStem = int(Gua.HeavenlyStem[self.day[0]])
        EarthlyBranches = int(Gua.EarthlyBranches[self.day[1]])
        result = EarthlyBranches - HeavenlyStem - 1
        if result > 0:
            empty1 = result
            empty2 = result+1
        elif result == -1:
            empty1 = 11
            empty2 = 0
        else:
            empty1 = result+12
            empty2 = result+13

        self.empty = Gua.NumtoEarthlyBranches[empty1] + \
            Gua.NumtoEarthlyBranches[empty2]

    def randomStart(self):
        self.get_cntime()
        self.get_empty()
        ### 六爻###
        self.yao1 = int(random.choice("01112223"))  # 获取爻数字
        self.yao2 = int(random.choice("01112223"))
        self.yao3 = int(random.choice("01112223"))
        self.yao4 = int(random.choice("01112223"))
        self.yao5 = int(random.choice("01112223"))
        self.yao6 = int(random.choice("01112223"))

        self.yao_1 = variable.transform(self.yao1)  # 创建爻元组
        self.yao_2 = variable.transform(self.yao2)
        self.yao_3 = variable.transform(self.yao3)
        self.yao_4 = variable.transform(self.yao4)
        self.yao_5 = variable.transform(self.yao5)
        self.yao_6 = variable.transform(self.yao6)
        self.vyao_1 = variable.variable(self.yao1)  # 变卦爻数
        self.vyao_2 = variable.variable(self.yao2)
        self.vyao_3 = variable.variable(self.yao3)
        self.vyao_4 = variable.variable(self.yao4)
        self.vyao_5 = variable.variable(self.yao5)
        self.vyao_6 = variable.variable(self.yao6)
        # print(self.yao_6)
        # print(self.yao_5)
        # print(self.yao_4)
        # print(self.yao_3)
        # print(self.yao_2)
        # print(self.yao_1)
        gua_num = (str(self.yao_1[0]) + str(self.yao_2[0]) + str(self.yao_3[0])
                   + str(self.yao_4[0]) + str(self.yao_5[0]) + str(self.yao_6[0]))
        self.Gua64 = gua_num  # 字符串卦数字
        ### 纳甲地支###
        self.EB_num1, self.EB_num2, self.EB_num3 = najiadz.najiadz(int(
            Gua.NumToEightGua[str(self.yao_3[0]) + str(self.yao_2[0]) + str(self.yao_1[0])]), 0)
        self.EB_num4, self.EB_num5, self.EB_num6 = najiadz.najiadz(int(
            Gua.NumToEightGua[str(self.yao_6[0]) + str(self.yao_5[0]) + str(self.yao_4[0])]), 1)
        self.VEB_num6, self.VEB_num2, self.VEB_num3 = najiadz.najiadz(
            int(Gua.NumToEightGua[str(self.vyao_3) + str(self.vyao_2) + str(self.vyao_1)]), 0)
        self.VEB_num4, self.VEB_num5, self.VEB_num6 = najiadz.najiadz(
            int(Gua.NumToEightGua[str(self.vyao_6) + str(self.vyao_5) + str(self.vyao_4)]), 1)
        ### 纳甲天干###
        self.HS_num1 = najiatg.najiatg(
            int(Gua.NumToEightGua[str(self.yao_3[0]) + str(self.yao_2[0]) + str(self.yao_1[0])]), 0)  # 内卦天干
        self.HS_num2 = najiatg.najiatg(
            int(Gua.NumToEightGua[str(self.yao_6[0]) + str(self.yao_5[0]) + str(self.yao_4[0])]), 1)  # 外卦天干
        self.VHS_num1 = najiatg.najiatg(
            int(Gua.NumToEightGua[str(self.vyao_3) + str(self.vyao_2) + str(self.vyao_1)]), 0)
        self.VHS_num2 = najiatg.najiatg(
            int(Gua.NumToEightGua[str(self.vyao_6) + str(self.vyao_5) + str(self.vyao_4)]), 1)
        ### 排世应、找卦宫###
        SY1, SY2, SY3, SY4, SY5, SY6, guagong = shiying.shiying(
            self.yao_1[0], self.yao_2[0], self.yao_3[0], self.yao_4[0], self.yao_5[0], self.yao_6[0])
        VSY1, VSY2, VSY3, VSY4, VSY5, VSY6, vguagong = shiying.shiying(
            self.vyao_1, self.vyao_2, self.vyao_3, self.vyao_4, self.vyao_5, self.vyao_6)
        ### 安六亲###
        GuaG = Gua.EightGua[int(Gua.NumToEightGua[guagong])]
        liuqin1 = liuqin.liuqin(GuaG, Gua.FiveAttribute[self.EB_num1])
        liuqin2 = liuqin.liuqin(GuaG, Gua.FiveAttribute[self.EB_num2])
        liuqin3 = liuqin.liuqin(GuaG, Gua.FiveAttribute[self.EB_num3])
        liuqin4 = liuqin.liuqin(GuaG, Gua.FiveAttribute[self.EB_num4])
        liuqin5 = liuqin.liuqin(GuaG, Gua.FiveAttribute[self.EB_num5])
        liuqin6 = liuqin.liuqin(GuaG, Gua.FiveAttribute[self.EB_num6])
        VGuaG = Gua.EightGua[int(Gua.NumToEightGua[guagong])]
        vliuqin1 = liuqin.liuqin(VGuaG, Gua.FiveAttribute[self.VEB_num6])
        vliuqin2 = liuqin.liuqin(VGuaG, Gua.FiveAttribute[self.VEB_num2])
        vliuqin3 = liuqin.liuqin(VGuaG, Gua.FiveAttribute[self.VEB_num3])
        vliuqin4 = liuqin.liuqin(VGuaG, Gua.FiveAttribute[self.VEB_num4])
        vliuqin5 = liuqin.liuqin(VGuaG, Gua.FiveAttribute[self.VEB_num5])
        vliuqin6 = liuqin.liuqin(VGuaG, Gua.FiveAttribute[self.VEB_num6])
        ### 格式化输出###
        self.label = f"""        四值：{self.year} {self.month} {self.day} {self.twohour} （旬空：{self.empty}）
        {Gua.gua64[self.Gua64]}({Gua.EightGua[int(Gua.NumToEightGua[guagong])]}宫)        {Gua.gua64[str(self.vyao_1) + str(self.vyao_2) + str(self.vyao_3) + str(self.vyao_4) + str(self.vyao_5) + str(self.vyao_6)]}({Gua.EightGua[int(Gua.NumToEightGua[vguagong])]}宫)
        {Gua.Yao[self.yao6]} {SY6} {Gua.NumtoHeavenlyStem[self.HS_num2]}{Gua.NumtoEarthlyBranches[self.EB_num6]}{Gua.FiveAttribute[self.EB_num6]} {liuqin6}  {Gua.VYao[self.vyao_6]} {VSY6} {Gua.NumtoHeavenlyStem[self.VHS_num2]}{Gua.NumtoEarthlyBranches[self.VEB_num6]} {Gua.FiveAttribute[self.VEB_num6]} {vliuqin6}
        {Gua.Yao[self.yao5]} {SY5} {Gua.NumtoHeavenlyStem[self.HS_num2]}{Gua.NumtoEarthlyBranches[self.EB_num5]}{Gua.FiveAttribute[self.EB_num5]} {liuqin5}  {Gua.VYao[self.vyao_5]} {VSY5} {Gua.NumtoHeavenlyStem[self.VHS_num2]}{Gua.NumtoEarthlyBranches[self.VEB_num5]} {Gua.FiveAttribute[self.VEB_num5]} {vliuqin5}
        {Gua.Yao[self.yao4]} {SY4} {Gua.NumtoHeavenlyStem[self.HS_num2]}{Gua.NumtoEarthlyBranches[self.EB_num4]}{Gua.FiveAttribute[self.EB_num4]} {liuqin4}  {Gua.VYao[self.vyao_4]} {VSY4} {Gua.NumtoHeavenlyStem[self.VHS_num2]}{Gua.NumtoEarthlyBranches[self.VEB_num4]} {Gua.FiveAttribute[self.VEB_num4]} {vliuqin4}
        {Gua.Yao[self.yao3]} {SY3} {Gua.NumtoHeavenlyStem[self.HS_num1]}{Gua.NumtoEarthlyBranches[self.EB_num3]}{Gua.FiveAttribute[self.EB_num3]} {liuqin3}  {Gua.VYao[self.vyao_3]} {VSY3} {Gua.NumtoHeavenlyStem[self.VHS_num1]}{Gua.NumtoEarthlyBranches[self.VEB_num3]} {Gua.FiveAttribute[self.VEB_num3]} {vliuqin3}
        {Gua.Yao[self.yao2]} {SY2} {Gua.NumtoHeavenlyStem[self.HS_num1]}{Gua.NumtoEarthlyBranches[self.EB_num2]}{Gua.FiveAttribute[self.EB_num2]} {liuqin2}  {Gua.VYao[self.vyao_2]} {VSY2} {Gua.NumtoHeavenlyStem[self.VHS_num1]}{Gua.NumtoEarthlyBranches[self.VEB_num2]} {Gua.FiveAttribute[self.VEB_num2]} {vliuqin2}
        {Gua.Yao[self.yao1]} {SY1} {Gua.NumtoHeavenlyStem[self.HS_num1]}{Gua.NumtoEarthlyBranches[self.EB_num1]}{Gua.FiveAttribute[self.EB_num1]} {liuqin1}  {Gua.VYao[self.vyao_1]} {VSY1} {Gua.NumtoHeavenlyStem[self.VHS_num1]}{Gua.NumtoEarthlyBranches[self.VEB_num6]} {Gua.FiveAttribute[self.VEB_num6]} {vliuqin1}"""

    def save(self):
        path = "./results/"
        if not os.path.exists(path):
            os.makedirs(path)
        with open(f"./results/{self.now}.txt", "w", encoding="utf-8") as f:
            f.write(self.label)

    def analysis(self):
        pass


if __name__ == "__main__":
    Divination = Divination()
    Divination.randomStart()
    Divination.save()
    print(Divination)
