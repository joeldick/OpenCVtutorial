import cv2
from matplotlib import pyplot as plt

if __name__ == "__main__":
    img = cv2.imread("Lenna.png", cv2.IMREAD_COLOR)

    cv2.imshow('image', img)
    key = cv2.waitKey(0)
    if key == 27:
        cv2.destroyWindow('image')

    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.xticks([]), plt.yticks([])
    plt.show()

