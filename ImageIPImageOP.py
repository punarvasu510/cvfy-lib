import cv2
import cvfy


app = cvfy.register('nongh:0.0.0.0:1129210:5001:7002:0.0.0.0:5001')

@cvfy.crossdomain
@app.listen()
def grayscale():

    images = cvfy.getImageArray() # From input image component

    image_i_path = images[0]

    cvfy.sendTextArrayToTerminal(['Loading Image............'])

    image_i = cv2.imread(image_i_path)

    #print type(image_i)

    gray_image_i = cv2.cvtColor(image_i, cv2.COLOR_BGR2GRAY)

    cvfy.sendTextArrayToTerminal(['Converting RGB image to Grayscale.............']);

    cvfy.sendImageArray([gray_image_i], mode = 'numpy_array')

    cvfy.sendTextArrayToTerminal(['Done!']);

    return 'OK'

app.run()