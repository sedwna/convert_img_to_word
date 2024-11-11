import pytesseract
from PIL import Image
from googletrans import Translator, LANGUAGES

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open the image (corrected path)
image = Image.open(r'C:\Users\priso\OneDrive\Desktop\convert_img_to_word\photo\2.png')

# Extract the text from the image
text = pytesseract.image_to_string(image)

# Split the text into sentences
sentences = text.split('.')

# Print the sentences
for sentence in sentences:
    print(sentence.strip())


translator = Translator()


# Translate each sentence to Persian and print it
for sentence in sentences:
    if sentence.strip():  # Check if the sentence is not empty
        try:
            translated = translator.translate(sentence.strip(), dest='fa')  # 'fa' is the language code for Persian
            print(translated.text)
        except Exception as e:
            print(f"Error translating sentence: {sentence.strip()}. Error: {e}")