import cv2
import os
from mtcnn import MTCNN
from IPython.display import display
from PIL import Image
from deepface import DeepFace
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib
detector = MTCNN()


# give the path of folder of each person and get the list of embeddings and labels of same person
def get_embeddings(roll_path):
    embeddings = []
    labels = []
    for file in os.listdir(roll_path):
        file_path = os.path.join(roll_path,file)
        embedding = DeepFace.represent(file_path, model_name='Facenet',enforce_detection=False)
        embeddings.append(embedding[0]['embedding'])
    roll_number = os.path.basename(roll_path)
    labels = [roll_number]*len(os.listdir(roll_path))  
    return embeddings,labels


data_path = r'C:\Users\Venkatesh Yeturi\OneDrive\Desktop\auto_attendance_python\Data\cropped_faces_dataset'

# if knn_model is not already existing , get all the embeddings and train a model and save. 
if not os.path.exists('knn_model.joblib'):

    embeddings = []
    labels = []
    for each_roll in os.listdir(data_path):
        roll_path = os.path.join(data_path,each_roll)
        person_embeddings, person_labels = get_embeddings(roll_path)
        embeddings.append(person_embeddings)
        labels.append(person_labels)
    embeddings = np.concatenate(embeddings, axis=0)
    labels = np.concatenate(labels, axis=0)

    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(embeddings, labels)
    joblib.dump(knn,'knn_model.joblib')

# give path of test_image and saved model, get the predictions ( roll numbers )
def get_predicted_roll_numbers(model, test_image_path):
    raw_test_image_path = os.path.normpath(test_image_path)
    # raw_test_image_path = 'r'+raw_test_image_path
    test_image = cv2.imread(raw_test_image_path)
    faces = detector.detect_faces(test_image)
    parent_folder_path = os.path.dirname(raw_test_image_path)
    str = os.path.basename(raw_test_image_path)[:-4] + "_faces"
    new_faces_folder = os.path.join(parent_folder_path,str)
    if not os.path.exists(new_faces_folder):
        os.makedirs(new_faces_folder)
    roll_numbers = []
    for i,face in enumerate(faces):
        x,y,w,h = face['box']
        face_image = test_image[y:y+h,x:x+w]
        image_saving_path = os.path.join(new_faces_folder,f'face_{i}.jpg')
        cv2.imwrite(image_saving_path,face_image)
        face_embedding = DeepFace.represent(image_saving_path,model_name='Facenet',enforce_detection=False)[0]['embedding']
        roll_number = model.predict([face_embedding])
        roll_numbers.append(roll_number)
    return roll_numbers


