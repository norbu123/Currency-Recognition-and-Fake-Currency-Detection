import os
import tensorflow as tf
import numpy as np
from django.shortcuts import render, redirect
from django.conf import settings
from io import BytesIO
from PIL import Image
import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Define the function to preprocess the image
def preprocess_image(image):
    # Read the image content
    image_content = image.read()
    
    # Convert the image content to a bytes-like object
    image_bytes = BytesIO(image_content)
    
    # Convert the bytes-like object to a PIL image
    pil_image = Image.open(image_bytes)
    
    # Resize the image
    resized_image = pil_image.resize((224, 224))
    
    # Convert the image to a numpy array
    image_array = np.array(resized_image)
    
    # Rescale the pixel values to the range [0, 1]
    image_array = image_array.astype('float32') / 255.0
    
    # Add a batch dimension to the array
    image_array = np.expand_dims(image_array, axis=0)
    
    return image_array


# Define the function to convert the model prediction to a label
def decode_prediction(prediction):
    # Get the class index with the highest probability
    class_index = np.argmax(prediction)
    
    # Load the class labels
    class_labels_path = os.path.join(settings.BASE_DIR, 'models', 'class_labels.txt')
    with open(class_labels_path, 'r') as f:
        class_labels = [line.strip() for line in f.readlines()]
    
    # Get the corresponding class label
    label = class_labels[class_index]
    
    return label

import time

def classify_image(request):
    if request.method == 'POST':
        # Load the model from the file
        model_path = os.path.join(settings.BASE_DIR, 'models', 'currencyDetector.h5')
        model = tf.keras.models.load_model(model_path)
        
        # Load the uploaded image
        image = request.FILES['image']
        image_array = preprocess_image(image)
        
        # Add a loading indicator
        loading = True
        request.loading = loading
        time.sleep(2)  # Simulating the prediction process
        
        # Make a prediction using the model
        prediction = model.predict(image_array)
        label = decode_prediction(prediction)
        
        # Remove the loading indicator
        loading = False
        request.loading = loading
        
        # Add the prediction to the request object
        request.prediction = label
        
    return render(request, 'form.html', {'prediction': getattr(request, 'prediction', None), 'loading': getattr(request, 'loading', False)})


def classify_captured_image(request):
    # Load the model from the file
    model_path = os.path.join(settings.BASE_DIR, 'models', 'currencyDetector.h5')
    model = load_model(model_path)
    
    # Start the video capture
    cap = cv2.VideoCapture(0)
    
    # Check if the video capture is successfully opened
    if not cap.isOpened():
        # Handle the case when the video capture fails to open
        print("Failed to open the video capture.")
        # Optionally, you can return an error response or perform appropriate error handling
        return
    
    while True:
        # Read a frame from the video capture
        ret, frame = cap.read()
        
        if not ret:
            # Handle the case when frame retrieval fails
            print("Failed to retrieve frame from the video capture.")
            # Optionally, you can return an error response or perform appropriate error handling
            break
        # Print the frame dimensions (optional)
        print("Frame dimensions:", frame.shape)
        
        # Resize the frame
        frame_resized = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
        
        # Convert the frame to a numpy array
        frame_array = np.array(frame_resized)
        
        # Rescale the pixel values to the range [0, 1]
        frame_array = frame_array.astype('float32') / 255.0
        
        # Add a batch dimension to the array
        frame_array = np.expand_dims(frame_array, axis=0)
        
        # Make a prediction using the model
        prediction = model.predict(frame_array)
        label = decode_prediction(prediction)
        
        # Display the classification result on the video capture window
        cv2.putText(frame, label, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Identification Result', frame)
        
        # Wait for the user to press a key
        key = cv2.waitKey(1)
        
        # If the user presses the 'q' key, exit the loop
        if key == ord('q'):
            break
    # Release the video capture and destroy the window
    cap.release()
    cv2.destroyAllWindows()

    request.prediction = label

   # Return an HttpResponse object with the desired response
    return HttpResponse(render(request, 'form.html',{'prediction'}: getattr(request, 'predicttion')))

def classify_captured_image(request):
    # Load the model from the file
    model_path = os.path.join(settings.BASE_DIR, 'models', 'currencyDetector.h5')
    model = load_model(model_path)
    
    # Start the video capture
    cap = cv2.VideoCapture(0)
    
    while True:
        # Read a frame from the video capture
        ret, frame = cap.read()
        
        # Resize the frame
        frame_resized = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
        
        # Convert the frame to a numpy array
        frame_array = np.array(frame_resized)
        
        # Rescale the pixel values to the range [0, 1]
        frame_array = frame_array.astype('float32') / 255.0
        
        # Add a batch dimension to the array
        frame_array = np.expand_dims(frame_array, axis=0)
        
        # Make a prediction using the model
        prediction = model.predict(frame_array)
        label = decode_prediction(prediction)
        
        # Display the classification result on the video capture window
        cv2.putText(frame, label, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Identification Result', frame)
        
        # Wait for the user to press a key
        key = cv2.waitKey(1)
        
        # If the user presses the 'q' key, exit the loop
        if key == ord('q'):
            break
    # Release the video capture and destroy the window
    cap.release()
    cv2.destroyAllWindows()

    request.prediction = label

    # return render(request, 'result.html', {'prediction': label})
    return render(request, 'form.html', {'prediction': getattr(request, 'prediction', None)})

    
def home(request):
    return render(request, 'home.html')

def back_view(request):
    referer=request.META.get('HTTP_REFERER')
    if referer:
        return redirect(referer)
    else:
        pass
