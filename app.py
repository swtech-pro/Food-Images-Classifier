
import torch
from torchvision import models, transforms
from PIL import Image
import gradio as gr
import os

labels = [line.strip() for line in open("labels.txt")]

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = models.efficientnet_b0(pretrained=False)
model.classifier[1] = torch.nn.Linear(model.classifier[1].in_features, len(labels))
model.load_state_dict(torch.load("food101_efficientnetb0.pth", map_location=device))
model.to(device)
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

def predict(image):
    image = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        outputs = model(image)
        probs = torch.nn.functional.softmax(outputs, dim=1)
        top_prob, top_cls = torch.topk(probs, 1)
    return {labels[top_cls.item()]: float(top_prob)}

gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=1),
    title="🍔 Food Image Classifier",
    description="Upload a food image and get the predicted category using EfficientNet-B0."
).launch()
