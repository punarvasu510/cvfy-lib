import cvfy

app = cvfy.register("nongh:0.0.0.0:4045468:5001:7001:0.0.0.0")

@cvfy.crossdomain
@app.listen()
def runner():

	cvfy.sendTextArrayToTerminal(['Fetching image........']);

    cvfy.sendImageArray(['/home/alekhya/123.jpg'],mode ='file_path') # Hardcoded image

    cvfy.sendTextArrayToTerminal(['Done!']);
    
    return 'OK'

app.run()