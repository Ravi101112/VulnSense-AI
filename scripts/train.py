from models.model import build_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Example placeholders
input_shape = (128, 128, 3)
model = build_model(input_shape)

print("Model built successfully.")
