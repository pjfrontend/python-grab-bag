from moviepy.editor import ImageSequenceClip, AudioFileClip

# List of image file paths
image_paths = ['image1.jpg', 'image2.jpg', 'image3.jpg']  # Add your image file paths

# Audio file path
audio_path = 'audio.mp3'  # Replace with your audio file path

# Create an ImageSequenceClip from the list of images
clip = ImageSequenceClip(image_paths, fps=24)  # Adjust the fps as needed

# Load the audio clip
audio_clip = AudioFileClip(audio_path)

# Set the audio of the video clip
video_clip = clip.set_audio(audio_clip)

# Write the final video file
video_clip.write_videofile('output_video.mp4', codec='libx264', audio_codec='aac')

# Make sure you have the MoviePy library installed (`pip install moviepy`) and that you replace the placeholders with your actual file paths.

# This example assumes all images have the same duration and frame rate. If your images have different durations, you may need to adjust the `fps` parameter accordingly.