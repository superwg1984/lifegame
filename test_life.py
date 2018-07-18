import main


x=32
y=55
hp=4

def test_t1():
    l=main.Life(f"{x}{y}",[x,y],hp)
    print(l)