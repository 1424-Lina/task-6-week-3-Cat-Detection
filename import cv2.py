import cv2

cat_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')

image_path = 'cat.jpg'
image = cv2.imread(image_path)

if image is None:
    print("Failed to load image.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cats = cat_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

for (x, y, w, h) in cats:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 255), 2)
    cv2.putText(image, "Cat", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)

cv2.imshow("Cat Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()