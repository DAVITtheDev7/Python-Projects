import cv2

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# For static images:
image = cv2.imread('hand.jpg')
boxes = hog.detectMultiScale(image)
weights = hog.detectMultiScale(image)
for (x, y, w, h) in boxes:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow('OpenCV Hand Detector', image)
cv2.waitKey(0)

# For real-time video:
cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, image = cap.read()
    if not success:
        break
    boxes, weights = hog.detectMultiScale(image)
    for (x, y, w, h) in boxes:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('OpenCV Hand Detector', image)
