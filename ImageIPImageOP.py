import cv2
import cvfy


app = cvfy.register('nongh:0.0.0.0:1129210:5001:7002:0.0.0.0:5001')

@cvfy.crossdomain
@app.listen()
def grayscale():

    all_image_paths = cvfy.getImageArray() 

    image_0_path = all_image_paths[0]
    
    #print image_0_path

    cvfy.sendTextArrayToTerminal(['Loading Image...'])
    image_0 = cv2.imread(image_0_path)

    print type(image_0)

    cvfy.sendTextArrayToTerminal(['Image Loaded successfully']);

    gray_image_0 = cv2.cvtColor(image_0, cv2.COLOR_BGR2GRAY)

    cvfy.sendTextArrayToTerminal(['Converting RGB Image to Grayscale']);

    cvfy.sendImageArray([gray_image_0], mode = 'numpy_array')

    cvfy.sendTextArrayToTerminal([
        'Operation completed successfully'
        ]);

    return 'OK'

app.run()