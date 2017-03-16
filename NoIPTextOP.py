import cvfy
import cv2

app = cvfy.register('nongh:0.0.0.0:8142133:5001:8001:0.0.0.0')

@cvfy.crossdomain
@app.listen()
def runner():
	cvfy.sendTextArrayToTerminal(['Before output is displayed'])
	cvfy.sendTextArray(['Hello World!']) # Hardcode Text Output
	cvfy.sendTextArrayToTerminal(['After output is displayed'])
	return 'OK'

app.run()
