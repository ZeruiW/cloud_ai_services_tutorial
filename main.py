from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import torchvision.models as models
import torch
import torchvision.transforms as transforms
from PIL import Image
import io

app = FastAPI()

model = models.resnet18(pretrained=True)
model.eval()
LABELS = open("imagenet_classes.txt").read().strip().split("\n")

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

@app.get("/")
def read_root():
    return {"message": "Welcome to the ML service"}

@app.get("/model_name")
def get_model_name():
    return {"model_name": "ResNet18"}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    image_stream = io.BytesIO(await file.read())
    image = Image.open(image_stream).convert("RGB")
    input_tensor = preprocess(image)
    input_batch = input_tensor.unsqueeze(0)
    with torch.no_grad():
        output = model(input_batch)
    _, predicted_idx = torch.max(output, 1)
    predicted_label = LABELS[predicted_idx.item()]

    return JSONResponse(content={"predicted_label": predicted_label})
