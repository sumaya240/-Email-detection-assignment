# -*- coding: utf-8 -*-
"""mugabekazisumaya2401001608.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WdZbuwECm7T4uSXY-hwdZ_3YiTAwTQTm
"""

offensive_words = [
    "inyenzi", "cockroaches", "kill", "exterminate", "destroy",
    "traitors", "snakes", "rats", "hutu power", "tutsi",
    "ethnic cleansing", "wipe out", "enemy", "revenge",
    "impurity", "traitors", "infiltrators", "parasites"
]
# Function to detect hate speech
def detect_hate_speech(text):
    detected_words = [word for word in offensive_words if word in text.lower()]
    return detected_words

# Example usage
text = "Why don’t we seize those parents who sent their children and exterminate them? Why don’t we seize all those who bring them and exterminate them all? Are we really waiting now for them to come and exterminate us?."
hate_words = detect_hate_speech(text)
if hate_words:
    print("Hate speech detected! Offensive words:", hate_words)
else:
    print("No hate speech detected.")