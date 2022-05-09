from TextBase import *

def __main__() :
    w = Wolf()
    k = Knight()
    k.blabla()
    w.blabla()
    w.attackSomeone(k)
    k.attackSomeone(w)
    k.berserkerSlash(w)
    w.attackSomeone(k)
    k.berserkerSlash(w)
    k.blabla()
    w.blabla()

if __name__ == "__main__" :
    __main__()