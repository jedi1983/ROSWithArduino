"""Subclass of MyFrame1, which is generated by wxFormBuilder."""

import wx
import testerROSUI
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int16
from wx.lib.pubsub import pub as wxPub
import os
import threading
import time


# Implementing MyFrame1
class TesterROSMyFrame1( testerROSUI.MyFrame1 ):

	pub = ''

	def __init__( self, parent ):
		testerROSUI.MyFrame1.__init__( self, parent )
		self.pub = rospy.Publisher('toggle_servo', Int16, queue_size=2)
		rospy.init_node('PythonTest')
		r = rospy.Rate(10) # 10hz
		rospy.Subscriber("current_pos",Int16, self.callback)
		self.moveHandle()

	def threaded(fn):
		def wrapper(*args, **kwargs):
			thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
			thread.setDaemon(True)
			thread.start()
			return thread
		return wrapper

	@threaded
	def moveHandle(self):
		rospy.spin()
	
	# Handlers for MyFrame1 events.
	def onClick( self, event ):
		# Check
		val_1 = self.m_textCtrl1.GetValue()
		val_2 = self.m_textCtrl2.GetValue()
		print rospy.is_shutdown()
		if rospy.is_shutdown() is False:
			self.pub.publish(int(val_1))

	def callback(self,data):
		dataBack = str(data.data)
		print dataBack
		self.m_textCtrl2.SetValue('')
		self.m_textCtrl2.SetValue(dataBack)
    	
if __name__ == '__main__':
    app = wx.App()
    frm = TesterROSMyFrame1(None)
    frm.Show()
    app.MainLoop()
