""" QR Code Reader in python """

import cv2
import sys

filename = sys.argv[1]

#read the QRCode img

img = cv2.imread(filename)

#initialise the cv2 QRCode detector
detector = cv2.QRCodeDetector()

#detect and decode
data, bbox, straight_qrcode = detector.detectAndDecode(img)


#If there is a QR code
if bbox is not None:
    print(f"QRCode data:\n{data}")
    #display the image with lines
    #length of bounding box
    n_lines = len(bbox)
    for i in range(n_lines):
        #draw all lines
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1)% n_lines][0])
        cv2.line(img, point1, point2, color=(225, 0, 0), thickness=2)

#display the result
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
