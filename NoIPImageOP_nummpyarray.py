import cv2
import cvfy


app = cvfy.register('nongh:0.0.0.0:4045468:5001:7001:0.0.0.0')

@cvfy.crossdomain
@app.listen()
def grayscale():

    cvfy.sendTextArrayToTerminal(['Loading Image...'])
    image_1 = cv2.imread('/home/alekhya/123.jpg') # Hardcoded output image

    print type(image_1)
    #print image_1

    cvfy.sendTextArrayToTerminal(['Image Loaded successfully']);

    gray_image_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY)

    cvfy.sendTextArrayToTerminal(['Converting RGB Image to Grayscale']);

    cvfy.sendImageArray([gray_image_1], mode = 'numpy_array')

    cvfy.sendTextArrayToTerminal([
        'Operation completed successfully'
        ]);

    return 'OK'

app.run()