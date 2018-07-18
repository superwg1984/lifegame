[![Build Status](https://travis-ci.org/superwg1984/lifegame.svg?branch=master)](https://travis-ci.org/superwg1984/lifegame)

# lifegame
用python写的生命游戏
规则:
    当生命周围没有其他生命时,当前生命hp+1,周围生命大于4个时,hp-1
    当生命hp>=10时,生命开始分裂出新的生命,这两个生命的hp=5
    
*遇到的问题*:
    随着时间增加,执行速度越来越慢
