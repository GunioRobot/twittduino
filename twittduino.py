from urllib import urlopen
import base64
import urllib2
import time
import codecs
import sys
import serial
from xml.dom.minidom import parse,parseString

streamWriter = codecs.lookup('utf-8')[-1]
sys.stdout = streamWriter(sys.stdout)

ser = serial.Serial('/dev/tty.usbserial-A60049lS', 115200)
ser.write("Twittduino 0.1 FTW")
time.sleep(2)
ser.write("~")

base64string = base64.encodestring('%s:%s' % ('USERNAME', 'PASSWORD'))[:-1] 
req = urllib2.Request('http://twitter.com/statuses/friends_timeline.xml')
req.add_header("Authorization", "Basic %s" % base64string)

while 1:
	try:
		handle = urllib2.urlopen(req)
	except IOError, e:
		if hasattr(e, 'reason'):
			print 'Reason : '
			print e.reason
	else:
			string = handle.read()      
	numNodes = 0;
	dom = parseString(string)
	for node in dom.getElementsByTagName('status'):  
		for node2 in node.getElementsByTagName('text'):  
			 for text in node2.childNodes:
				 msg=  text.toxml()
		for node3 in node.getElementsByTagName('user'):  
			for node4 in node.getElementsByTagName('screen_name'):  
				 for text2 in node4.childNodes:
					 sn = text2.toxml()
		output = "@" + sn + " Wrote:" + msg
		if numNodes < 4:
			ser.write('~')
			ser.write(output.encode('ascii','ignore'))
			time.sleep(10)
			print output
		numNodes +=1;
	time.sleep(60) #update every 60 min
