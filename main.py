import cv2
import dlib
from imutils import face_utils, resize
import numpy as np

# print(cv2.__version__)
# print(dlib.__version__)
# print(np.__version__)

orange_img = cv2.imread('orange.jpg')
orange_img = cv2.resize(orange_img, dsize=(512, 512))

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

cap = cv2.VideoCapture(0)  # webcam

while cap.isOpened():
    ret, img = cap.read()

    if not ret:
        break

    faces = detector(img)

    result = orange_img.copy()

    if len(faces) > 0:
        face = faces[0]

        x1, y1, x2, y2 = face.left(), face.top(), face.right(), face.bottom()
        face_img = img[y1:y2, x1:x2].copy()

        shape = predictor(img, face)
        shape = face_utils.shape_to_np(shape)

        # for p in shape:
        cv2.circle(face_img, )
