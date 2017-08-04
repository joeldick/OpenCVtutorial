import cv2
import numpy

if __name__ == '__main__':
    img = numpy.zeros([512, 512, 3], dtype=numpy.uint8)
    img.fill(255)

    #cv2.line(img, (0,0), (512,512), (255,0,0), 5)
    #cv2.rectangle(img, (171,341),(341,171),(0,255,0),3)
    #cv2.circle(img,(256,256),(121),(0,0,255), 5)

    # draw a horcrux
    triangle = numpy.array([[171, 305],[341, 305],[256, 157]], numpy.int32)
    #triangle = triangle.reshape((-1,1,2))
    cv2.polylines(img,[triangle],True,(0, 0, 0), 3)
    cv2.line(img, (256, 157), (256, 305), (0, 0, 0), 3)
    cv2.circle(img, (256, 256), 49, (0, 0, 0), 3)

    cv2.imshow('imange',img)
    if cv2.waitKey(0) == ord('q'):
        cv2.destroyAllWindows()
