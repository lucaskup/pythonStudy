import cv2

img=cv2.imread('galaxy.jpg',0)

print(type(img))
print(img)

resized_image=cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))
cv2.imshow('Galaxy',resized_image)
cv2.imwrite('galaxy_resized.jpeg',resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
