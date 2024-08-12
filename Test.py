
import cv2

img=cv2.imread('picture\Screenshot 2024-08-12 115229.png')
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("picture\exampe_1.png")