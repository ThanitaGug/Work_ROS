#!/usr/bin/env python3

#thanita kaeoking6452500244
import rospy
from std_msgs.msg import Int16
from tkinter import *

frame = Tk()
frame.geometry('200x200')

rospy.init_node('GUI_RandBT_control')
rate = rospy.Rate(10)
rate.sleep()

def read(num):
    sensor_read = num.data
    Show_sensor.config(text = str(sensor_read))

def Talker(val):
    cmd_val = Int16(val)
    rospy.loginfo(cmd_val)
    pub.publish(cmd_val)

sub = rospy.Subscriber("Topic_led", Int16, callback = read)
pub = rospy.Publisher("Topic_led", Int16, queue_size = 10)

#โชว์ข้อความ ที่ฟรอนต์ 'Arial'ขนาด 60 ข้อความกดคือ 0 หมยความว่าถ้ามีเลขอื่นเข้ามา จะขึ้นเป็นเลขนั้น
Show_sensor = Label(frame, font = ('Arial',60), text = "0")
Show_sensor.pack()

#สร้างปุ่ม ON AND OFF ที่ตำแหน่ง....
BT_ON = Button(frame, text = "ON", command = lambda: Talker(1))
BT_ON.place(x=40, y=150)

BT_OFF = Button(frame, text = "OFF", command = lambda: Talker(0))
BT_OFF.place(x=110, y=150)

frame.mainloop()
