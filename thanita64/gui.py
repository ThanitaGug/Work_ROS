#!/usr/bin/env python3

#thanita kaeoking6452500244
import rospy
from tkinter import*
# สร้างหน้าต่างของ_gui ใช้โครงสร้างของ tk or tk inter รันโดยอัตโนมัติโดยไม่มี main
from std_srvs.srv import Empty  # Import the Empty service from std_srvs package

from geometry_msgs.msg import Twist
frame = Tk()
frame.title("REMOTE")
frame.geometry("300x200") # ขนาดของ frame

rospy.init_node("GUI_Remote") #สร้างโนดชื่อ GUI_Remote
pub = rospy.Publisher("turtle1/cmd_vel",Twist, queue_size=10) #ส่งข้อมูลไปที่ turtle1/cmd_vel" ในรูปแบบของ Twist

#topics = rospy.get_published_topics()
#for topic, _ in topics:
#    print(topic)

def fw():
    print("fw")
    cmd = Twist()
    cmd.linear.x = 1.0
    cmd.angular.z=0.0
    pub.publish(cmd)

def bw():
    print("bw")
    cmd = Twist()
    cmd.linear.x = -1.0
    cmd.angular.z=0.0
    pub.publish(cmd)

def sl():
    print("sl")
    cmd = Twist()
    cmd.linear.x = 0.0
    cmd.angular.z= 0.0
    cmd.linear.y = 1.0
    pub.publish(cmd)

def sr():
    print("sr")
    cmd = Twist()
    cmd.linear.x = 0.0
    cmd.angular.z= 0.0
    cmd.linear.y = -1.0
    pub.publish(cmd)

def rol():
    print("rotate L")
    cmd = Twist()
    cmd.linear.x = 0.0
    cmd.angular.z= 1.0
    cmd.linear.y = 0.0
    pub.publish(cmd)

def ror():
    print("rotate R")
    cmd = Twist()
    cmd.linear.x = 0.0
    cmd.angular.z= -1.0
    cmd.linear.y = 0.0
    pub.publish(cmd)

def reset_tur():
    print("Reset")
    rospy.wait_for_service('/reset')  # รอให้บริการ "reset" พร้อมใช้งาน
    try:
        reset_service = rospy.ServiceProxy('/reset', Empty)
        response = reset_service()
        rospy.loginfo("Reset Turtlesim Service Response: %s", response)
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s", e)

B1 = Button(text = "FW", command= fw, bg="#4F80C0") #โครงสร้างปุ่ม โดยเรียกไปที่ฟังก์ชั่น
B1.place(x=73, y=20)                 #ตำแหน่ง

B2 = Button(text = "BW", command= bw)
B2.place(x=73, y=130)

B3 = Button(text = "SL", command= sl)
B3.place(x=20, y=80)

B4 = Button(text = "SR", command= sr)
B4.place(x=128, y=80)

B5 = Button(text = "RoL", command= rol)
B5.place(x=200, y=30)

B6 = Button(text = "RoR", command= ror)
B6.place(x=200, y=80)

B7 = Button(text = "reset", command=reset_tur)
B7.place(x=200, y=130)

frame.mainloop()
