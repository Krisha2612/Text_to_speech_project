# Text to Speech Project 🎤

This simple Python project converts text to speech using the `gTTS` (Google Text-to-Speech) library. The speech is saved as an `.mp3` file inside a folder named after the user.

## 📦 Features

- Takes a text string and user name as input.
- Converts the text into speech using Google Text-to-Speech.
- Saves the output in a directory named after the user.
- Stores the audio in `.mp3` format.

## 🛠️ Requirements

- Python 3.x
- gTTS

## 📁 Project Structure

## 🚀 Installation & Usage

### 1. Clone or Download the Project

Download the ZIP or clone the repository.

bash
    git clone <your-repo-url>
    cd text_to_speech_project

### 2. Install Dependencies
bash
    pip install -r requirements.txt

### 3. Run the Program
bash
    python main.py

### 4. Example
Input:
Enter your name: Krisha
Enter the text to convert to speech: Hello, this is a test message.

Output:
text_to_speech_project/
└── Krisha/
    └── output.mp3
