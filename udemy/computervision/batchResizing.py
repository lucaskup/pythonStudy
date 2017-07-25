import glob2
import cv2

arquivos = glob2.glob('sample-images/*')
for fil in arquivos:
    img=cv2.imread(fil,0)
    img_r = cv2.resize(img,(100,100))
    cv2.imwrite(fil+'res.jpeg',img_r)
