# cartoon_classifier/classifier.py

from transformers import pipeline

class CartoonClassifier:
    def __init__(self):
        self.pipe = pipeline("image-classification", model="TTNVXX/CartoonOrNot")

    def classify_image(self, image_path):
        result = self.pipe(image_path)
        return result