import io
import os
import pygame.camera
import time
import csv

# Imports the Google Cloud client library
from google.cloud import vision


def take_picture():
    image = cam.get_image()
    pygame.image.save(image, "01.jpg")


if __name__ == '__main__':
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/matthew/Documents/My First Project-b5e1e25e8952.json"

    pygame.init()
    pygame.camera.init()
    pygame.camera.list_cameras()
    cam = pygame.camera.Camera("/dev/video0", (1280, 720))
    cam.start()
    # Instantiates a client
    client = vision.ImageAnnotatorClient()
    while True:
        time.sleep(1)
        take_picture()
        # The name of the image file to annotate
        file_name = os.path.join(
            os.path.dirname(__file__),
            '01.jpg')

        # Loads the image into memory
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)

        response = client.face_detection(image=image)
        faces = response.face_annotations

        # Names of likelihood from google.cloud.vision.enums
        likelihood_name = (-1, 0, 1, 2, 3, 4)
        print('Faces:')
        avg = 0
        temp = 0
        num_faces = 0
        for face in faces:
            temp = max(likelihood_name[face.anger_likelihood], likelihood_name[face.joy_likelihood], likelihood_name[face.surprise_likelihood])
            num_faces += 1
            avg = ((num_faces - 1) * (avg) + temp) / num_faces
        print(avg)
        num_faces = 0
        temp = 0
        avg = 0




# Imports the Google Cloud client library
from google.cloud import vision


def take_picture():
    image = cam.get_image()
    pygame.image.save(image, "01.jpg")


if __name__ == '__main__':
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/matthew/PycharmProjects/video_capture/My First Project-b5e1e25e8952.json"

    pygame.init()
    pygame.camera.init()
    pygame.camera.list_cameras()
    cam = pygame.camera.Camera("/dev/video0", (1280, 720))
    cam.start()
    # Instantiates a client
    client = vision.ImageAnnotatorClient()
    while True:
        time.sleep(1)
        take_picture()
        # The name of the image file to annotate
        file_name = os.path.join(
            os.path.dirname(__file__),
            '01.jpg')

        # Loads the image into memory
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)

        response = client.face_detection(image=image)
        faces = response.face_annotations

        # Names of likelihood from google.cloud.vision.enums
        likelihood_name = (-1, 0, 1, 2, 3, 4)
        print('Faces:')
        avg = 0
        temp = 0
        num_faces = 0
        for face in faces:
            temp = max(likelihood_name[face.anger_likelihood], likelihood_name[face.joy_likelihood], likelihood_name[face.surprise_likelihood])
            avg = ((num_faces - 1) * (avg) + temp) / num_faces
            num_faces += 1

        # Prints average of facial data
        print(avg)
        num_faces = 0
        temp = 0
        avg = 0



