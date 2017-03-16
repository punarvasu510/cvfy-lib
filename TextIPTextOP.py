import cvfy
import cv2

app = cvfy.register('nongh:0.0.0.0:9106717:5001:8002:0.0.0.0:5001')

@cvfy.crossdomain
@app.listen()
def runner():

	cvfy.sendTextArrayToTerminal(['Before input is sent to get()'])
	textdata = cvfy.getTextArray()

	cvfy.sendTextArray(textdata)
	cvfy.sendTextArrayToTerminal(['After output is sent to send()'])

	return 'OK'

app.run()
