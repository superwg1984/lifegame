#!/usr/bin/env python
# coding=utf-8
__author__ = 'superewg'
import random
import time
import logging

import config
import view


def main():
    a = random.randint(1, config.X)
    b = random.randint(1, config.Y)

    root = view.get_tk()
    view.set_tk(root, "life1", "500x500")
    cv = view.get_canvas(root, 'white')
    cv.pack()

    L = config.ALL
    xs = random.sample(range(0, 100), 50)
    ys = random.sample(range(0, 100), 50)
    for i in range(0, 50):
        lname = str(xs[i]) + str(ys[i])
        L[lname] = Life(lname, [xs[i], ys[i]], random.randint(0, 10))

    lifecolor = ["red", "red", "red", "yellow", "yellow", "yellow", "green", "green", "green", "green", "green"]

    while True:
        s=time.clock()
        for i in list(L.keys()):
            # print("L size:", len(L.keys()))
            j=L.get(i)
            j.lifeordie(L)

            # logging.info(f"[{j.getXY()[0]},{j.getXY()[1]}]lifeHP:{j.getHp()}")
            if j.getHp() >= 10:
                x, y = L[i].addLife(L)
                lname = str(x) + str(y)
                if x != -1:
                    L[lname] = Life(lname, [x, y], 5)
            elif j.getHp() <= 0:
                del L[i]
                cv.delete(j.getName())
        for i, j in L.items():
            xy = j.getXY()
            cv.create_rectangle(xy[0] * 5, xy[1] * 5, xy[0] * 5, xy[1] * 5, outline=lifecolor[L[i].getHp()],
                                tags=j.getName())
            root.update()
            # time.sleep(2)

        logging.info(f"总细胞数:{len(L)},用时{time.clock()-s}")
    root.mainloop()


class Life:
    def __init__(self, name, xy, hp):
        """
        初始化生命
        :rtype : object
        """
        self.__xy = xy
        self.__name = name
        self.__hp = hp

    def die(self):
        del self

    def addLife(self, llist):
        '''
        返回一个可以添加细胞的位置
        :param list:
        :return:
        '''
        ret = []
        mylist = self.round()
        # print("mylist", mylist)
        # print("list.key", llist.keys())
        for i in mylist:
            x, y = i
            # print("i:",i)

            if 0 < x < config.X and 0 < y < config.Y:
                # print(type(llist))
                c = list(llist.keys()).count(i)
                if c == 0:
                    ret.append(i)
        # print(len(ret))
        r = random.randint(0, len(ret))
        # print(ret[r - 1])
        if len(ret) <= 0:
            return [-1, -1]
        else:
            self.__hp = 5
            return ret[r - 1]

    def round(self):
        '''
        返回周围位置
        :return:
        '''
        x, y = self.__xy
        ret = [[x + 1, y], [x + 1, y + 1], [x, y + 1], [x - 1, y + 1], [x - 1, y], [x - 1, y - 1], [x, y - 1],
               [x, y - 1]]
        return ret

    def round2(self):
        '''
        返回周围位置
        :return:
        '''
        x, y = self.__xy
        ret = [str(x + 1) + str(y), str(x + 1) + str(y + 1), str(x) + str(y + 1), str(x - 1) + str(y + 1),
               str(x - 1) + str(y), str(x - 1) + str(y - 1), str(x) + str(y - 1),
               str(x) + str(y - 1)]
        return ret

    def lifeordie(self, list):
        '''
        判断细胞生命值增减
        :param xy:
        :return:
        '''
        ret = self.round2()
        # print("周围", ret)
        c = 0
        for i in list.keys():
            c = c + ret.count(i)

        # logging.info("%s周围细胞数量:%d", self.__name, c)
        isLife = False
        if 0 <= c < 4:
            isLife = True
        elif c >= 4:
            isLife = False

        if isLife:
            self.__hp += 1
        else:
            self.__hp -= 1

    def getHp(self):
        return self.__hp

    def getXY(self):
        return self.__xy

    def getName(self):
        return self.__name


if __name__ == '__main__':
    main()
