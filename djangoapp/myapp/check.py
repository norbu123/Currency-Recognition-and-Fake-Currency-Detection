import cv2
import numpy as np
import tensorflow as tf

# Load saved and compiled model
loaded_model = tf.keras.models.load_model('currency.h5')

# Define list of label names
label_names = ['FakeIndianNote','IndianNote','Nu. 1','Nu. 10','Nu. 100','Nu. 1000','Nu. 20','Nu. 5','Nu. 50','Nu. 500']

# Open default camera (id=0)
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Preprocess image for prediction
    img = cv2.resize(frame, (224, 224))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img.astype(np.float32) / 255.
    img = np.expand_dims(img, axis=0)

    # Make prediction using loaded model
    prediction = loaded_model.predict(img)

    # Display prediction on frame
    label_index = np.argmax(prediction, axis=1)[0]  # get predicted label index
    label_name = label_names[label_index]  # look up corresponding label name
    cv2.putText(frame, label_name, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), thickness=2)  # add label name to frame
    cv2.imshow('Webcam', frame)  # show frame

    # Check for 'Esc' key press to exit
    if cv2.waitKey(1) == 27:
        break

# Release camera and close window
cap.release()
cv2.destroyAllWindows()
