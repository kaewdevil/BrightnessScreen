import screen_brightness_control as sbc
import easygui as egui
import sys

#BRIGHTNESS
def st():
    valb = egui.enterbox("ระดับความสว่าง : ")
    if valb:
        pass
    else:sys.exit()
#valb = input("ระดับความสว่าง : ") 
    sbc.set_brightness(valb)
while 1==1:
    st()
st()

