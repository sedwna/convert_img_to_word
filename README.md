# Image to Text and Translation Script

This script extracts text from an image using Optical Character Recognition (OCR) and translates the extracted text into Persian (Farsi). It utilizes the `pytesseract` library for OCR and the `googletrans` library for translation.

## Prerequisites

Before running the script, ensure you have the following installed:

1. **Python**: The script is written in Python. Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Tesseract-OCR**: The script uses Tesseract for OCR. Download and install Tesseract from [Tesseract's GitHub page](https://github.com/tesseract-ocr/tesseract). Make sure to note the installation path, as it will be needed in the script.

3. **Python Libraries**: Install the required Python libraries using pip:
   ```bash
   pip install pytesseract pillow googletrans==4.0.0-rc1
   ```

   - `pytesseract`: A Python wrapper for Tesseract.
   - `Pillow`: A Python Imaging Library (PIL) fork used to open and manipulate images.
   - `googletrans`: A Python library for Google Translate API.

## Script Overview

The script performs the following steps:

1. **Set Tesseract Path**: The path to the Tesseract executable is set.
2. **Open Image**: The script opens an image file from a specified path.
3. **Extract Text**: The text is extracted from the image using `pytesseract`.
4. **Split Text into Sentences**: The extracted text is split into sentences.
5. **Translate Sentences**: Each sentence is translated into Persian (Farsi) using `googletrans`.
6. **Print Sentences**: Both the original and translated sentences are printed.

## Usage

1. **Set the Tesseract Path**: Update the `pytesseract.pytesseract.tesseract_cmd` variable with the correct path to your Tesseract installation.

2. **Set the Image Path**: Update the `Image.open()` function with the correct path to your image file.

3. **Run the Script**: Execute the script using Python:
   ```bash
   python script_name.py
   ```

   Replace `script_name.py` with the name of your script file.

## Example

Given an image containing the text:
```
Hello, world! This is a test.
```

The script will output:
```
Hello, world!
This is a test.
سلام دنیا!
این یک تست است.
```

## Notes

- **Language Support**: The script is currently set to translate text into Persian (`fa`). You can change the destination language by modifying the `dest` parameter in the `translator.translate()` function. Refer to the `LANGUAGES` dictionary in `googletrans` for supported language codes.

- **Error Handling**: The script includes basic error handling for translation errors. If a sentence cannot be translated, an error message will be printed.

- **Image Quality**: The accuracy of the OCR depends on the quality of the input image. Ensure the image is clear and the text is legible for best results.


## Acknowledgments

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Google Translate API](https://pypi.org/project/googletrans/)
- [Pillow](https://python-pillow.org/)

---
