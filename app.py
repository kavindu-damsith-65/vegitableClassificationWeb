from flask import Flask, request, jsonify, render_template
from PIL import Image
import numpy as np
import cv2
import base64
import os

app = Flask(__name__)





@app.route('/')
def home():
    return render_template('index.html')




@app.route('/upload', methods=['POST'])
def upload():
    clean_input_folder("input")
    clean_input_folder("output")


    file = request.files['image']
    img = Image.open(file)
    image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR) 
    
    
    # Convert image to JPEG format
    image_jpg = cv2.imencode('.jpg', image)[1].tobytes()

    # Save the image to the input folder
    image_path = os.path.join("input", file.filename.split(".")[0]+"Modified" + ".jpg")
    with open(image_path, 'wb') as f:
        f.write(image_jpg)
    
    
    imagePath=os.path.join('input',os.listdir('input')[0])




     # apply to model and get image path
    otputLi=os.listdir("output")




    

    if(len(otputLi)>0):
        
        imagePath=os.path.join('output',otputLi[0])
       
    
    image2 = cv2.imread(imagePath)
    # cv2.imshow("image",image)
    # cv2.waitKey(0)
    image2 =cv2.flip(image2,1)
    
    img_base64 = base64.b64encode(cv2.imencode('.jpg', image2)[1])
    
    # Return the JSON response
    response = {'message': "Nothing", 'image_data': str(img_base64)}
   
    return jsonify(response)







def clean_input_folder(input_folder):
    # Check if the input folder exists, create it if necessary
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
    else:
        # Clean the input folder by removing all files
        for filename in os.listdir(input_folder):
            file_path = os.path.join(input_folder, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)





if __name__ == '__main__':
    app.run()
