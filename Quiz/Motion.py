#!/usr/bin/env python3
from tkinter import *
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import os

root = Tk()
root.geometry("300x300")
root.title(" Show Action ")

def reset_turtle():
    try:
        #Call the "reset" service
        rospy.wait_for_service('/reset')
        reset_service = rospy.ServiceProxy('/reset', Empty)
        reset_service()
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

def clearToTextInput():
	reset_turtle()
	ActOut.delete("1.0","end")

def run(val):
	ActOut.insert(END, val.data + "\n")


if __name__ == "__main__":
	#  Initial ROS node and determine Publish or Subscribe action	
	sub = rospy.Subscriber("chatter",String,callback = run)
	rospy.init_node("Motion")

	

	ActLabel = Label(text = "Motion", font = ("",18))
	ActLabel.place(x=113, y=10)
	ActOut = Text(root, height = 7, width = 10, bg = "light cyan", font = ("",16))
	ActOut.place(x=83, y=50)

	ClearBtn=Button(root,height=1,width=10,text="Clear",command=clearToTextInput)
	ClearBtn.place(x=103, y=250)

	mainloop()


