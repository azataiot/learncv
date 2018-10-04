import cv2 as cv


img_src="./img/coins.jpg" # 图像路径
img=cv.imread(img_src) # read the picture
print(type(img)) # <class 'numpy.ndarray'>

# show the picture ,so we need a GUI to show it 
cv.namedWindow("current img",cv.WINDOW_AUTOSIZE)
cv.imshow("current img",img)
cv.waitKey(0)
cv.destroyAllWindows()

print("Successfully imported and readed the image~\n")