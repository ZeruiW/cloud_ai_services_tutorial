
------

### Part I: Azure Cloud AI Service



#### What is Azure Cognitive Services?

Cognitive Services brings AI within reach of every developer and data scientist. A variety of use cases can be unlocked. All it takes is an API call to embed the ability to see, hear, speak, search, understand, and accelerate advanced decision-making into your apps. Enable developers and data scientists of all skill levels to easily add AI capabilities to their apps.



![image-20230826194816986](https://s2.loli.net/2023/08/27/yLubQjnOwl7qFg5.png)



#### How to access the Azure cloud?

To get started with Azure Cognitive Services, you'll first need to access the Azure Cloud platform. Below are the steps to get started:

1. **Sign-Up for an Azure Account**
    - If you don't have an Azure subscription, you can create an account with Concordia University Account login. Go to the education page to get more than a hundred dollars of free credits.
2. **Login to Azure Portal**
    - Go to the [Azure Portal](https://portal.azure.com/) and log in using your credentials.
3. **Navigate to Cognitive Services**
    - In the left sidebar, scroll down and click on "Create a resource". Then, search for "Cognitive Services" and select it.
4. **Create a New Service**
    - Click on the "Create" button to start setting up a new Cognitive Services resource. You'll be prompted to fill in details like:
        - **Resource Name**: A unique name for your service
        - **Subscription**: Choose your Azure subscription, and choose a **Student account** for free credits.
        - **Resource Group**: Create a new one or select an existing one
        - **Region**: Select the geographical area closest to you or your customers
        - **Pricing Tier**: Choose a pricing tier based on your needs





![image-20230826195708158](https://s2.loli.net/2023/08/27/rNYq2dfayniPpsO.png)

![image-20230826195258232](https://s2.loli.net/2023/08/27/BTL1sFEhWXUrVo4.png)

![image-20230826195429182](https://s2.loli.net/2023/08/27/RhGyFqgUD1KOS3w.png)





#### Accessing Custom Vision

Azure offers a specialized service for image recognition: Custom Vision on another address instead of Azure Cloud Portal. This service is highly user-friendly and is designed for the rapid and easy creation of custom image classification models.

Differing from the Azure Platform Portal, this Custom Vision can be access by navigating to the [Custom Vision Portal](https://www.customvision.ai/).

#### Detailed Steps

1. **Sign In or Sign Up**
    - If you already have an Azure account, you can sign in. 
2. **Create a New Project**
    - Click on the "New Project" button and fill in the details for your project, such as the name, description, and the resource you wish to use.
    - The type selection is classification, multiclass, and a general domain.
3. **Upload Images and Annotate**
    - After creating your project, you must upload images with label to train your model. 
    - This tutorial provides example data in the “dataset“ folder. This contains a split train dataset and a test dataset. The dataset contains types of Animals. The ImageNet original label is given as the folder name. You are also free to change to the label to the ground-truth name, given in the readme file.
    - In another case, when you have too much data and labels, write your own script for uploading images and labels. Please check the Azure Custom Vision official documents using the given APIs to upload data.
4. **Train the Model**
    - Once your images are uploaded and annotated, click on the "Train" button to start training your model. Setting the resources as you prefer.
5. **Evaluate the Model**
    - After the training is complete, you can see the model's accuracy and other performance metrics.
6. **Quick Test**
    - Use the "Quick Test" option to upload an image and quickly check the model's accuracy.
7. **Publish the Endpoint**
    - If you are satisfied with your model's performance, click on the "Publish" button to publish your model. During this publishing process, you will need to choose a resource and name your endpoint.
8. **Get Endpoint and Key**
    - Once published, you'll receive an Endpoint URL and a key. You can use this information for API calls within your application.







![image-20230826195856417](https://s2.loli.net/2023/08/27/zO6hyU8jofwTCVl.png)





![image-20230826195930399](C:/Users/wangz/AppData/Roaming/Typora/typora-user-images/image-20230826195930399.png)







![image-20230826200014803](https://s2.loli.net/2023/08/27/VU5l8TrceJGbFI4.png)



![image-20230826200108430](https://s2.loli.net/2023/08/27/yEXFB95OjlP4tkY.png)

![image-20230826200147986](https://s2.loli.net/2023/08/27/hB64wJva3OmEFpW.png)



Now that your Custom Vision model has been published and you have your endpoint URL and prediction key, you can start making API calls to classify new images.

Once your Custom Vision model is up and running, testing its API endpoints is crucial for ensuring it works as expected before you integrate it into your application. Below are step-by-step guides for testing your API using both image URLs and image files.



### Testing the Model Service

If you have an image URL:

https://eastus.api.cognitive.microsoft.com/customvision/v3.0/Prediction/projectname/classify/iterations/imagenetAzure/url

Set `Prediction-Key` Header to : `12861a3a15xxxxxxxxxxxxxxxxx`

Set `Content-Type` Header to : `application/json`

Set Body to : `{"Url": "https://example.com/image.png"}`

If you have an image file:

https://eastus.api.cognitive.microsoft.com/customvision/v3.0/Prediction/projectname/classify/iterations/imagenetAzure/image

Set `Prediction-Key` Header to : `12861a3a1xxxxxxxxxxxxxxxx`

Set `Content-Type` Header to : `application/octet-stream`

Set Body to : <image file>

#### 1 Using python HTTP request to test

##### Testing with an Image URL

**Step 1: Install Required Software**

If you haven't already, install Python and the requests library.

```
pip install requests
```

**Step 2: Prepare Python Script**

Create a Python script and add the following code:

```
import requests
import json

# Endpoint and headers setup
endpoint_url = "https://eastus.api.cognitive.microsoft.com/customvision/v3.0/Prediction/projectname/classify/iterations/imagenetAzure/url"
headers = {
    "Prediction-Key": "12861a3a15xxxxxxxxxxxxxxxxx",
    "Content-Type": "application/json"
}

# Image URL
payload = json.dumps({"Url": "https://example.com/image.png"})

# API call
response = requests.post(endpoint_url, headers=headers, data=payload)

# Output results
results = response.json()
print(results)
```

**Step 3: Run the Script**

Run the Python script. If everything is set up correctly, you should see the predicted labels and confidence scores.

##### Testing with an Image File

**Step 1: Install Required Software**

If you haven't already, install Python and the requests library.

```
pip install requests
```

**Step 2: Prepare Python Script**

Create a Python script and add the following code:

```
import requests

# Endpoint and headers setup
endpoint_url = "https://eastus.api.cognitive.microsoft.com/customvision/v3.0/Prediction/projectname/classify/iterations/imagenetAzure/image"
headers = {
    "Prediction-Key": "12861a3a1xxxxxxxxxxxxxxxx",
    "Content-Type": "application/octet-stream"
}

# Read the image file
image_path = "path/to/your/image.jpg"
with open(image_path, "rb") as image_data:
    # API call
    response = requests.post(endpoint_url, headers=headers, data=image_data)

# Output results
results = response.json()
print(results)
```

**Step 3: Run the Script**

Run the Python script. If everything is set up correctly, you should see the predicted labels and confidence scores.

#### 2 Using Postman to Test Your Custom Vision API

Postman is a popular tool for testing APIs. It provides a user-friendly interface to send requests to your API endpoints and view responses. Below is a step-by-step guide to using Postman for testing your Custom Vision API.

#### Prerequisites

- Download and install Postman from [here](https://www.postman.com/downloads/).

##### Testing with an Image URL

**Step 1: Open Postman**

Open Postman and create a new request by clicking on the `New` button and then selecting `Request`.

**Step 2: Configure the Request**

- Set the HTTP method to `POST`.

- Enter your Custom Vision URL endpoint for image URL classification in the request URL field:
    `https://eastus.api.cognitive.microsoft.com/customvision/v3.0/Prediction/projectname/classify/iterations/imagenetAzure/url`

- In the Headers tab, add the following headers:

    - `Prediction-Key`: `12861a3a15xxxxxxxxxxxxxxxxx`
    - `Content-Type`: `application/json`

**Step 3: Add Body**

Go to the `Body` tab, select `raw` and choose `JSON` from the dropdown. Then enter the following payload:

```
{
  "Url": "https://example.com/image.png"
}
```

**Step 4: Send Request and Review Output**

Click the `Send` button to send the request. You should see the response at the bottom of the Postman window, which will include the predicted labels and their confidence scores.

##### Testing with an Image File

**Step 1: Open Postman**

Open Postman and create a new request by clicking on the `New` button and then selecting `Request`.

**Step 2: Configure the Request**

- Set the HTTP method to `POST`.

- Enter your Custom Vision URL endpoint for image file classification in the request URL field:
    `https://eastus.api.cognitive.microsoft.com/customvision/v3.0/Prediction/projectname/classify/iterations/imagenetAzure/image`

- In the Headers tab, add the following headers:

    - `Prediction-Key`: `12861a3a1xxxxxxxxxxxxxxxx`
    - `Content-Type`: `application/octet-stream`

**Step 3: Add Body**

- Go to the `Body` tab.
- Select `binary`.
- Click the `Choose Files` button and upload your image file.

**Step 4: Send Request and Review Output**

Click the `Send` button to send the request. You should see the response at the bottom of the Postman window, which will include the predicted labels and their confidence scores.

 By following these steps, you can ensure your model's API is functioning as expected before integrating it into your application.

![image-20230826224403509](https://s2.loli.net/2023/08/27/eyHBaj3T4hqEvx9.png)





