

import cv2

import os

import numpy as np






def detect_face(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    

    face_cascade = cv2.CascadeClassifier(os.getcwd()+'/django_precog/opencv-files/lbpcascade_frontalface.xml')

    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
    

    if (len(faces) == 0):
        return None, None
    
    
    (x, y, w, h) = faces[0]
    

    return gray,faces

    #gray[y:y+w, x:x+h], faces[0]

def prepare_training_data(data_folder_path):
    
    
    dirs = os.listdir(data_folder_path)


    faces = []

    labels = []
    

    for dir_name in dirs:
        
       
        if not dir_name.startswith("s"):
            continue;
            
       
        label = int(dir_name.replace("s", ""))

        
        subject_dir_path = data_folder_path + "/" + dir_name
        

        subject_images_names = os.listdir(subject_dir_path)

        
        for image_name in subject_images_names:
            

            if image_name.startswith("."):
                continue;
            
            
            image_path = subject_dir_path + "/" + image_name


            image = cv2.imread(image_path)


            #cv2.imshow("Training on image...", cv2.resize(image, (400, 500)))
            #cv2.waitKey(100)
            

            face, rect = detect_face(image)
            
            
            if face is not None:

                faces.append(face)

                labels.append(label)

            
    '''cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.destroyAllWindows()'''
    print("Total faces: ", len(faces))
    return faces, labels



#print("Preparing data...")

#print("Data prepared")


#print("Total faces: ", len(faces))
#print("Total labels: ", len(labels))







def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    

def draw_text(img, text, x, y):
    cv2.putText(img, '', (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)



def predict(test_img,subjects):
    s=''
    faces, labels = prepare_training_data(os.getcwd()+"/django_precog/training-data")
    face_recognizer =  cv2.createLBPHFaceRecognizer()

    face_recognizer.train(faces, np.array(labels))

    img = test_img.copy() 

    print "hi\n"
    #face, rect = detect_face(img)
    gray,faces = detect_face(img)
    if len (faces)>0: 
	    for g in range(len(faces)):
		rect=faces[g]
	    	(x, y, w, h) = rect
		face=gray[y:y+w, x:x+h]

		label, confidence = face_recognizer.predict(face)
	    
		print "hello"

		if label>2 or label==0 :
		    label_text=''
		    if s=='':
		    	s= "Not present"
		else:
	    	    label_text = subjects[label]
		    if label==1 :
			s=s+ "Found:Narendra Modi"+"\n"
		    else:
			s=s+ "Found:Arvind Kejriwal"+"\n"
	    
		print label,confidence
	    	draw_rectangle(img, rect)

	    	draw_text(img, label_text, rect[0], rect[1]-5)
    else:
		s= "Not present"
    
    return img,s



def main(filename):

	subjects = ["", "Narendra Modi","Arvind Kejriwal"]


	
	#print("Predicting images...")



	test_img = cv2.imread(os.getcwd()+"/django_precog/static/"+filename)



	predicted_img,s = predict(test_img,subjects)
	#cv2.imshow("Output",cv2.resize(predicted_img, (400, 500)))

	cv2.imwrite( os.getcwd()+"/django_precog/static/"+filename.split(".")[0]+"_"+"Output.jpg", cv2.resize(predicted_img, (400, 500)));



	cv2.waitKey(0)
	cv2.destroyAllWindows()
	cv2.waitKey(1)
	cv2.destroyAllWindows()

	return s





