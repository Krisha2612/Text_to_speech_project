import os
from gtts import gTTS

def text_to_speech(text: str, username: str):
    # Create a directory for the user if it doesn't exist
    user_folder = os.path.join(os.getcwd(), username)
    os.makedirs(user_folder, exist_ok=True)

    # Set file path
    file_path = os.path.join(user_folder, "output.mp3")

    # Convert text to speech
    tts = gTTS(text)
    tts.save(file_path)

    print(f"Speech file saved successfully at: {file_path}")

# Get input from the user
if __name__ == "__main__":
    username = input("Enter your name: ").strip()
    text = input("Enter the text to convert to speech: ").strip()
    
    if username and text:
        text_to_speech(text, username)
    else:
        print("Username and text cannot be empty.")
