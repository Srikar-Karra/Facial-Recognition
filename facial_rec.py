#Dependicies and Packages
import face_recognition
import cv2 
import time

#This initlizes the webcam from your computer using opencv
vid = cv2.VideoCapture(0)


def take_picture():
    """This takes a picture with the webcam"""

    #This reads the data from the webcam
    ret, frame = vid.read()  
    
    #This writes the image to the unknown directory
    cv2.imwrite('/Users/srikarkarra/Downloads/Important Stuff/Coding/facial_rec/unknown/unknown.jpg', frame)


while True:
    #This code allows the camera to take a picture once the camera is able to take in light after 5 seconds. 
    #Otherwise, the light wont be able enter the camera in the time that the code runs
    time.sleep(1)
    take_picture()

    #This loads the images into a variable
    known_image = face_recognition.load_image_file('./known/srikar.jpg')
    unknown_image = face_recognition.load_image_file('./unknown/unknown.jpg')

    #This encodes the images by loading all the aspects of the face into the variables 
    srikar_encoding = face_recognition.face_encodings(known_image)[0]
    try:
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    
        #This code compares the faces encoding to one and other. The tolerance is set to 0.6 so that the match doesn't have to be perfect.
        results = face_recognition.compare_faces([srikar_encoding], unknown_encoding, tolerance=0.6)

        #This code checks whether the code returned a True or False Value. The code has to be converted to a string since it is a numpy object.
        #Instead of printing whether its a match or not you could use this as a authentication process and call different scripts or functions
        if str(results[0]) == "True":
            print("its a match")
        
        elif str(results[0]) == "False":
            print("nope not a match")
        else:
            print("something is wrong")  
        
        #This is used to break the loop
        new_input = input("1 to stop or 2 to stop")
        if new_input.lower() == "1":
            break
        else:
            pass 
    except:
        print("Pls try again, your face wasn't clearly detected in the picture")
        time.sleep(3)


