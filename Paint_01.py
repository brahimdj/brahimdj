import pyautogui as p
import time
#distance is about the first line
dis=input("Enter distance: ")
dis=int(dis)
print("wait for 5 sec ('Enter your Paint' )..")
p.sleep(3)
#while distance up to 0
while dis > 0:
    dis=dis-10
    p.dragRel(dis,0)
    dis=dis-10
    p.dragRel(0,dis)
    dis=dis-10
    p.dragRel(-dis,0)
    dis=dis-10
    p.dragRel(0,-dis)
print("Done!")
#distance =0
    









