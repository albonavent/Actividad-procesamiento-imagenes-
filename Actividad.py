from skimage import io,color
import matplotlib.pyplot as plt
img =io.imread('ejemplo.jpg')
cimg =io.imread('ejemplo.jpg')
img_gris = color.rgb2gray(img)
img3 = color.rgb2gray(img)
plt.title('1 channel image')
info=img.shape
img2=img_gris

for i in range(info[0]):
    for j in range(info[1]):
        if img2[i][j]<=0.95  and img2[i][j]>=0.6:
            aux=img[i][j]
            aux[0]=255
            aux[1]=255
            aux[2]=255
            img2[i][j]=0
        else:
            img2[i][j]=1
plt.subplot(221)
io.imshow(img2)
plt.title('CAMINOS')
plt.subplot(222)
plt.imshow(img)
plt.title('RESTO DE ELEMENTOS')
plt.subplot(223)
plt.imshow(cimg)
plt.title('IMG ORIGINAL')
plt.subplot(224)
io.imshow(img3)
plt.title('IMG ESCALA DE GRISES')
plt.show()





