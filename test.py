# Can you tell me if this works? I had this working with a random number generator spanning numbers one through five, so hopefully this works with our real data.

import io
import os
import pygame.camera
import time
from matplotlib import pyplot as plt
from matplotlib import style

# Imports the Google Cloud client library
from google.cloud import vision

z = time.time()
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
    count = 0
    while count < 10:
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
            print(temp)


        # Prints average of facial data

        style.use('ggplot')
        x = avg
        y = time.time()-z
        plt.scatter(y,x)

        plt.title("Performance over Time")
        plt.ylabel("Average Engagement")
        plt.xlabel("Time Elapsed")
        count += 1
    plt.show()


