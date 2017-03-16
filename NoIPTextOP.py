import cvfy
import cv2

app = cvfy.register('nongh:0.0.0.0:8142133:5001:8001:0.0.0.0')

@cvfy.crossdomain
@app.listen()
def runner():
	cvfy.sendTextArrayToTerminal(['This data will be sent before output is injected in ', 'Output Component'])
	cvfy.sendTextArray(['Hello']) # Hardcode Text Output
	cvfy.sendTextArrayToTerminal(['This data will be sent after output is injected in ', 'Output Component'])
	return 'OK'

app.run()
