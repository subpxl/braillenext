from objectdetect import ObjectDetect
from textDetect import text_within

image = '/home/pi/cashma/images/testimages/text/text.jpg'

result = text_within(image)
print(result)