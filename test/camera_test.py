import picamera
imgpath = "/home/pi/cashma/sample.jpg"


def capture():
    camera.start_preview()
    
    camera.capture(imgpath)
    return imgpath


if __name__ == "__main__":
    capture()