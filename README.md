
# 🍔 Food-101 Image Classification App

This is a fast prototype AI app for image classification using the **Food-101 dataset** and **EfficientNet-B0** architecture. It uses **PyTorch** for model training and **Gradio** for real-time prediction UI.

---

## 📦 Project Structure

```
.
├── app.py                # Gradio UI
├── labels.txt            # List of food categories
├── food101_efficientnetb0.pth  # Trained model file (add manually)
├── requirements.txt      # Required Python packages
├── LICENSE.txt           # MIT License
├── README.md             # Documentation
```

---

## 🔧 Setup Instructions

### 🧑‍💻 Clone the Repo
```bash
git clone https://github.com/yourusername/food101-app.git
cd food101-app
```

### 💾 Install Requirements
```bash
pip install -r requirements.txt
```

### 🧠 Download Trained Model
Download `food101_efficientnetb0.pth` from your training (or ask provider) and place it in the root directory.

Also update `labels.txt` with the actual 101 class names of Food-101.

---

## 🚀 Run the App

```bash
python app.py
```

It will open a **Gradio web UI** where you can upload an image and get the predicted food class.

---

## 📊 Model Details

- **Architecture:** EfficientNet-B0
- **Dataset:** Food-101 from Hugging Face
- **Framework:** PyTorch
- **Frontend:** Gradio Interface

---

## 🧠 Training (Optional)

If you want to retrain:
- Use the `Food101_Classifier_Gradio_EfficientNetB0.ipynb` notebook provided
- Train on Google Colab using Hugging Face `datasets`
- Save the model as `food101_efficientnetb0.pth`

---

## ✅ How to Use

1. Run the app
2. Upload a food image (jpg/png)
3. Wait for model to process
4. See prediction result with confidence

---

## 📜 License

This project is under the MIT License. See LICENSE.txt.

---

## ✨ Author

Made with ❤️ by Your Name (replace with your info)
