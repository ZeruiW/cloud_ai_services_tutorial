Tutorial：Using Cloud AI Services and Deploying model on Azure



### Objective

1. **How to Obtain Cloud AI services**:

    - Azure Cognitive Service
    - Amazon Rekognition
    - Google Vertex AI
    - Huggingface
2. **Integration & Deployment**:

    - Integrate Cloud AI services(e.g. Hugging Face) 
    - Make the server design follow OpenAPI standard through Swagger API
3. **Integration & Deployment**:
    - Deploy on Azure Cloud， CI/CD

#### Part I: Acquiring Cloud AI Services

------

1. Azure Cognitive Service
    - **Introduction to Azure Cognitive Services**
        - Overview of Azure Cognitive Service capabilities.
        	
        - Importance of AI in Azure's ecosystem.
    - **Setting up Azure Cognitive Service**
        - Creating an Azure account.
        - Provisioning a new Cognitive Service resource.
        - Understanding pricing and service limits.
    - **Accessing Services with SDKs and APIs**
        - Installing and setting up the required SDKs.
        - Making your first API call.
        - Understanding response structures and handling results.



## What is Azure Cognitive Services?

Cognitive Services brings AI within reach of every developer and data scientist. With leading models, a variety of use cases can be unlocked. All it takes is an API call to embed the ability to see, hear, speak, search, understand, and accelerate advanced decision-making into your apps. Enable developers and data scientists of all skill levels to easily add AI capabilities to their apps.





![image-20230826194816986](https://s2.loli.net/2023/08/27/yLubQjnOwl7qFg5.png)

![image-20230826195708158](https://s2.loli.net/2023/08/27/rNYq2dfayniPpsO.png)

![image-20230826195258232](https://s2.loli.net/2023/08/27/BTL1sFEhWXUrVo4.png)

![image-20230826195429182](https://s2.loli.net/2023/08/27/RhGyFqgUD1KOS3w.png)





![image-20230826195856417](https://s2.loli.net/2023/08/27/zO6hyU8jofwTCVl.png)





![image-20230826195930399](C:/Users/wangz/AppData/Roaming/Typora/typora-user-images/image-20230826195930399.png)







![image-20230826200014803](https://s2.loli.net/2023/08/27/VU5l8TrceJGbFI4.png)



![image-20230826200108430](https://s2.loli.net/2023/08/27/yEXFB95OjlP4tkY.png)

![image-20230826200147986](https://s2.loli.net/2023/08/27/hB64wJva3OmEFpW.png)





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



![image-20230826224403509](https://s2.loli.net/2023/08/27/eyHBaj3T4hqEvx9.png)


------

1. Amazon Rekognition
    - **Introduction to Amazon Rekognition**
        - Overview of Rekognition capabilities: image and video analysis.
        - Importance of AI in AWS's ecosystem.
    - **Configuring Rekognition in AWS Console**
        - Navigating the AWS console.
        - Provisioning a new Rekognition service.
        - Assigning IAM roles and permissions.
    - **Accessing Services with SDKs and APIs**
        - Integrating with AWS SDK.
        - Using the AWS CLI for Rekognition.
        - Interpreting results and common use cases.



![image-20230826201405076](https://s2.loli.net/2023/08/27/LtnDiqHwU3AGS4X.png)



![image-20230826201641987](https://s2.loli.net/2023/08/27/BSYcvA8HCg4V7yj.png)





![image-20230826201719851](https://s2.loli.net/2023/08/27/Rkqno7J4DBrA8l2.png)

## Pricing (US)

Inference hour$4 per hour

Training hour$1 per hour



![image-20230826202015873](https://s2.loli.net/2023/08/27/hUYe95DCyA1RHBQ.png)









------

1. Google Vertex AI
    - **Introduction to Google Vertex AI**
        - Overview of Vertex AI capabilities: AutoML, custom training, and more.
        - Importance of AI in Google Cloud's ecosystem.
    - **Setting Up Google Vertex AI**
        - Navigating the Google Cloud Console.
        - Creating a new Vertex AI project.
        - Understanding service integrations and dependencies.
    - **Accessing Services with SDKs and APIs**
        - Using Google Cloud client libraries.
        - Authenticating and making API requests.
        - Understanding Vertex AI's unified interface.



![image-20230826202439063](https://s2.loli.net/2023/08/27/s1cB8EXmqd3Viut.png)



![image-20230826202605352](https://s2.loli.net/2023/08/27/owHMCTglazyed1b.png)



![image-20230826202640478](https://s2.loli.net/2023/08/27/3RYLpuvDxmseojO.png)







------

1. Huggingface
    - **Introduction to Huggingface**
        - Exploring the Huggingface ecosystem: Models, Datasets, and Spaces.
        - Understanding the role of Huggingface in democratizing AI.
    - **Utilizing Huggingface's Cloud Services**
        - Navigating the Huggingface Inference API.
        - Deploying models on Huggingface Spaces.
        - Working with the Huggingface Model Hub.
    - **Building Custom Models and APIs with Huggingface**
        - Training custom models using Huggingface's Trainer.
        - Fine-tuning pre-trained models.
        - Integrating models into custom applications.



https://huggingface.co/microsoft/resnet-50

![image-20230826202751569](https://s2.loli.net/2023/08/27/6JhaenpFKSsA8yf.png)



![image-20230826202901893](https://s2.loli.net/2023/08/27/edQqHfZ6sGX9PIn.png)









#### Part II: Integration & Deployment of Cloud AI Services

------

1. **Integration of Cloud AI Services**
    - Integrating with Hugging Face
        - **Setting the Stage**
            - Briefly recap of Hugging Face's capabilities.
            - Importance of integration in application development.
        - **Building Server Applications with Hugging Face**
            - Setting up a server (e.g., Flask, FastAPI).
            - Integrating Hugging Face models into the server.
            - Handling user requests and sending them to Hugging Face for inference.
        - **Utilizing Hugging Face SDK & API for Integration**
            - Introduction to the Hugging Face SDK.
            - Making API calls using the SDK.
            - Parsing and presenting results to end-users.

------

1. **Designing Server with Swagger API to Adhere to OpenAPI Standards**
    - **Introduction to OpenAPI & Swagger**
        - What is the OpenAPI Specification (OAS)?
        - Role of Swagger in API development and documentation.
    - **Designing Your API with Swagger**
        - Using Swagger Editor to create API definitions.
        - Defining endpoints, methods, parameters, and response formats.
        - Generating API documentation automatically with Swagger UI.
    - **Integrating Your Server with Swagger**
        - Implementing Swagger in a Flask or FastAPI server.
        - Using annotations and decorators for automatic documentation.
        - Ensuring adherence to OpenAPI standards for better compatibility and interoperability.
    - **Testing and Validating Your API**
        - Using tools like Postman or Swagger UI for testing.
        - Importance of validation for robust applications.
        - Handling errors and exceptions gracefully.





### how to use

Here is how to use this model to classify an image of the COCO 2017 dataset into one of the 1,000 ImageNet classes:

```python
from transformers import AutoImageProcessor, ResNetForImageClassification
import torch
from datasets import load_dataset

dataset = load_dataset("huggingface/cats-image")
image = dataset["test"]["image"][0]

processor = AutoImageProcessor.from_pretrained("microsoft/resnet-50")
model = ResNetForImageClassification.from_pretrained("microsoft/resnet-50")

inputs = processor(image, return_tensors="pt")

with torch.no_grad():
    logits = model(**inputs).logits

# model predicts one of the 1000 ImageNet classes
predicted_label = logits.argmax(-1).item()
print(model.config.id2label[predicted_label])
```





```python
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```



![Swagger UI](https://s2.loli.net/2023/08/27/4HhGQ6tj7Xkxdcq.png)





![image-20230826210938294](https://s2.loli.net/2023/08/27/R3CNBztZkVKWSeG.png)

















https://www.gradio.app/



## 

Gradio supports many types of components, such as `Image`, `DataFrame`, `Video`, or `Label`. Let’s try an image-to-image function to get a feel for these!

```python
import numpy as np
import gradio as gr

def sepia(input_img):
    sepia_filter = np.array([
        [0.393, 0.769, 0.189], 
        [0.349, 0.686, 0.168], 
        [0.272, 0.534, 0.131]
    ])
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    return sepia_img

demo = gr.Interface(sepia, gr.Image(shape=(200, 200)), "image")
demo.launch()
```

![image-20230826211233311](https://s2.loli.net/2023/08/27/w3ORMXUWy8TtE9n.png)



  

#### Part III: Deployment - Azure Cloud CI/CD Deployment

------

1. **Introduction to Azure Cloud**
    - **Azure Infrastructure and Services Overview**
        - Brief about Azure's global infrastructure.
        - Key services offered: Compute, Networking, Storage, and AI.
    - **Creating and Managing an Azure Account**
        - Setting up an Azure account.
        - Navigating the Azure Portal.
        - Understanding subscription and resource groups.

------

1. **Deploying Cloud AI Service on Azure Cloud**
    - **Deploying on Azure App Service**
        - What is Azure App Service?
        - Creating a Web App in Azure App Service.
        - Deploying a server application with Cloud AI integrations to Azure App Service.
        - Monitoring and logging with Azure Monitor.
    - **Deploying Using Azure Kubernetes Service (AKS)**
        - Introduction to Kubernetes and AKS.
        - Setting up an AKS cluster.
        - Deploying a containerized AI application on AKS.
        - Scaling and managing applications on AKS.

------

1. **CI/CD on Azure**
    - **Introduction to Azure DevOps**
        - Overview of Azure DevOps Services: Boards, Pipelines, Repos, and more.
        - Importance of CI/CD in modern software development.
    - **Setting Up Continuous Integration with Azure DevOps**
        - Creating a new project in Azure DevOps.
        - Setting up a CI pipeline: Fetching code from repositories, building, testing, and packaging.
        - Integrating automated tests to ensure code quality.
    - **Setting Up Continuous Deployment with Azure DevOps**
        - Deploying to different environments: Development, Staging, and Production.
        - Configuring release pipelines.
        - Rolling out updates with zero downtime using deployment strategies like blue-green or canary deployments.
    - **Monitoring and Management**
        - Utilizing Azure Monitor and Azure Application Insights for real-time monitoring.
        - Setting up alerts and diagnostics.
        - Continuous feedback and improvement in the CI/CD process.





## [What is a container?](https://docs.docker.com/get-started/#what-is-a-container) 

A container is a sandboxed process running on a host machine that is isolated from all other processes running on that host machine. That isolation leverages [kernel namespaces and cgroupsopen_in_new](https://medium.com/@saschagrunert/demystifying-containers-part-i-kernel-space-2c53d6979504), features that have been in Linux for a long time. Docker makes these capabilities approachable and easy to use. To summarize, a container:

- Is a runnable instance of an image. You can create, start, stop, move, or delete a container using the Docker API or CLI.
- Can be run on local machines, virtual machines, or deployed to the cloud.
- Is portable (and can be run on any OS).
- Is isolated from other containers and runs its own software, binaries, configurations, etc.

If you're familiar with `chroot`, then think of a container as an extended version of `chroot`. The filesystem comes from the image. However, a container adds additional isolation not available when using chroot.



## [What is an image?](https://docs.docker.com/get-started/#what-is-an-image) 

A running container uses an isolated filesystem. This isolated filesystem is provided by an image, and the image must contain everything needed to run an application - all dependencies, configurations, scripts, binaries, etc. The image also contains other configurations for the container, such as environment variables, a default command to run, and other metadata.



### GitHub Actions: CI/CD for Azure Cloud with Containerized Applications

------

**1. Introduction to GitHub Actions**

- **Overview:** GitHub Actions helps automate tasks within the software development lifecycle.
- **Workflows:** Defined by `.yml` or `.yaml` files in the `.github/workflows` directory of a repository.







![image-20230826212537348](https://s2.loli.net/2023/08/27/rLGjZ4dgxQa8hPf.png)







![image-20230826212615465](https://s2.loli.net/2023/08/27/nqbMNtRhPfluAYL.png)



------

**2. Setting Up a Basic Workflow**

1. **In your repository**, click on the `Actions` tab.
2. **New workflow:** Use a template or set up a custom workflow.

For our tutorial, we'll use a custom setup.

1. **Choose the "Set up a workflow yourself" option.**

**. Integrating with Azure**

steps:
- name: Login to Azure
  uses: azure/login@v1
  with:
    creds: ${{ secrets.AZURE_CREDENTIALS }}



![image-20230826213108217](https://s2.loli.net/2023/08/27/Kdj8ORonD6rwPqG.png)

 



    name: Build and deploy a container to an Azure Web App
    
    env:
      AZURE_WEBAPP_NAME: your-app-name  # set this to the name of your Azure Web App
    
    on:
      push:
        branches: [ "main" ]
      workflow_dispatch:
    
    permissions:
      contents: read
    
    jobs:
      build:
        runs-on: ubuntu-latest
    
        steps:
          - uses: actions/checkout@v3
    
          - name: Set up Docker Buildx
            uses: docker/setup-buildx-action@v1
    
          - name: Log in to GitHub container registry
            uses: docker/login-action@v1.10.0
            with:
              registry: ghcr.io
              username: ${{ github.actor }}
              password: ${{ github.token }}
    
          - name: Lowercase the repo name and username
            run: echo "REPO=${GITHUB_REPOSITORY,,}" >>${GITHUB_ENV}
    
          - name: Build and push container image to registry
            uses: docker/build-push-action@v2
            with:
              push: true
              tags: ghcr.io/${{ env.REPO }}:${{ github.sha }}
              file: ./Dockerfile
    
      deploy:
        permissions:
          contents: none
        runs-on: ubuntu-latest
        needs: build
        environment:
          name: 'Development'
          url: ${{ steps.deploy-to-webapp.outputs.webapp-url }}
    
        steps:
          - name: Lowercase the repo name and username
            run: echo "REPO=${GITHUB_REPOSITORY,,}" >>${GITHUB_ENV}
    
          - name: Deploy to Azure Web App
            id: deploy-to-webapp
            uses: azure/webapps-deploy@v2
            with:
              app-name: ${{ env.AZURE_WEBAPP_NAME }}
              publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE }}
              images: 'ghcr.io/${{ env.REPO }}:${{ github.sha }}'





**Build and Push Docker Image to Azure Container Registry (ACR)**

- name: Set up Docker Buildx
  uses: docker/setup-buildx-action@v1

- name: Build Docker Image
  run: docker build -t <ACR_NAME>.azurecr.io/myapp:${{ github.sha }} .



 **Deploying to Azure**

- name: Deploy to Azure Container Instances
  run: |
    az container create --resource-group <RESOURCE_GROUP> --name myapp --image <ACR_NAME>.azurecr.io/myapp:${{ github.sha }} --cpu 1 --memory 1Gi --registry-login-server <ACR_NAME>.azurecr.io --registry-username ${{ secrets.REGISTRY_USERNAME }} --registry-password ${{ secrets.REGISTRY_PASSWORD }}





![image-20230826224725861](https://s2.loli.net/2023/08/27/zx5EH8iyJWgFLpP.png)

### Using GitHub Actions to Push Container Images and Deploy to Azure

------

**Prerequisites:**

- An Azure account and an active subscription.
- A GitHub repository with your application code.
- Dockerfile in your repository for containerization.
- Azure Container Registry (ACR) created to store your Docker images.

------

**1. Setting Up Secrets in GitHub**

To securely interact with Azure, you'll need to set up secrets in your GitHub repository:

- **Azure Credentials**: Go to your repo's `Settings > Secrets` and add a new secret named `AZURE_CREDENTIALS`. The value should be a JSON string containing your Azure service principal details:

    ```
    jsonCopy code{
      "clientId": "<APP_ID>",
      "clientSecret": "<PASSWORD>",
      "subscriptionId": "<SUBSCRIPTION_ID>",
      "tenantId": "<TENANT_ID>"
    }
    ```

- **Container Registry Credentials**: Add secrets `REGISTRY_USERNAME` and `REGISTRY_PASSWORD` for your Azure Container Registry authentication.

------

**2. GitHub Actions Workflow**

Here's a step-by-step breakdown of the workflow to push a container to ACR and deploy it using Azure services.

```
yamlCopy codename: Deploy to Azure

on:
  push:
    branches:
      - main

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Login to Azure
      uses: azure/login@v1
      with:
        creds: ${{ secrets.AZURE_CREDENTIALS }}

    - name: Build and push Docker image
      uses: docker/build-push-action@v2
      with:
        context: .
        file: ./Dockerfile
        push: true
        tags: <ACR_NAME>.azurecr.io/myapp:${{ github.sha }}
        registry: <ACR_NAME>.azurecr.io
        username: ${{ secrets.REGISTRY_USERNAME }}
        password: ${{ secrets.REGISTRY_PASSWORD }}

    # Here you can add deployment steps, for instance:

    - name: Deploy to Azure Kubernetes Service (AKS)
      run: |
        az aks get-credentials --resource-group <RESOURCE_GROUP> --name <AKS_CLUSTER_NAME>
        kubectl set image deployment/<DEPLOYMENT_NAME> <CONTAINER_NAME>=<ACR_NAME>.azurecr.io/myapp:${{ github.sha }}

    # Or, if using Azure Container Instances (ACI):
    - name: Deploy to Azure Container Instances (ACI)
      run: |
        az container create --resource-group <RESOURCE_GROUP> --name myapp-container --image <ACR_NAME>.azurecr.io/myapp:${{ github.sha }} --dns-name-label myapp-container --ports 80

    - name: Logout from Azure
      run: az logout
```
