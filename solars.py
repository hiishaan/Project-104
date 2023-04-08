import cv2

solar = cv2.imread("solar-system.jpg")

cv2.putText(solar, "Sun", (70,30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (225 ,255 ,255))
cv2.putText(solar, "Mercury", (110,190), cv2.FONT_HERSHEY_COMPLEX, 0.5, (225 ,67 ,255))
cv2.putText(solar, "Venus", (200,180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (90 ,67 ,255))
cv2.putText(solar, "Earth", (275,165), cv2.FONT_HERSHEY_COMPLEX, 0.5, (225 ,132 ,225))
cv2.putText(solar, "Mars", (360,185), cv2.FONT_HERSHEY_COMPLEX, 0.5, (10 ,132 ,225))
cv2.putText(solar, "Jupiter", (450,325), cv2.FONT_HERSHEY_COMPLEX, 0.5, (48 ,255 ,255))
cv2.putText(solar, "Satern", (750,295), cv2.FONT_HERSHEY_COMPLEX, 0.5, (29 ,53 ,73))
cv2.putText(solar, "Uranus", (950,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (225 ,32 ,255))
cv2.putText(solar, "Neptune", (1100,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (225 ,255 ,56))

cv2.imshow("image", solar)
cv2.imwrite("C:/Ishaan/SolarSystem.jpg", solar)
cv2.waitKey(5000)