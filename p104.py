import cv2


img = cv2.imread('solar-system.jpg')

cv2.putText(img, 'Sun', (10,10), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, color=(0,0,255), thickness=1)

cv2.imshow('output',img)
cv2.waitKey(0)

