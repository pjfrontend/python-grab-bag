import pyttsx3

def save_text_to_speech(text, output_file):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech

    # Save the speech to an audio file
    engine.save_to_file(text, output_file)

    # Wait for the speech to finish
    engine.runAndWait()

# Example usage
text = "Hello, this is a text-to-speech example using pyttsx3."
output_file = "output_audio.mp3"

save_text_to_speech(text, output_file)