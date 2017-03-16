import cv2
import cvfy


app = cvfy.register('nongh:0.0.0.0:4045468:5001:7001:0.0.0.0')

@cvfy.crossdomain
@app.listen()
def grayscale():

    image = cv2.imread('/home/alekhya/123.jpg') # Hardcoded input image

    #print type(image)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cvfy.sendTextArrayToTerminal(['Converting RGB image to Grayscale............']);

    cvfy.sendImageArray([gray_image], mode = 'numpy_array')

    cvfy.sendTextArrayToTerminal(['Done!']);

    return 'OK'

app.run()