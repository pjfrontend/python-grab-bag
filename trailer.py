from moviepy.editor import ImageSequenceClip, AudioFileClip, CompositeVideoClip, ImageClip

# List of image file paths
image_paths = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg'] * 12 # Add your image file paths

# Audio file path
audio_path = 'Vanishing.mp3'  # Replace with your audio file path

# Create an ImageSequenceClip from the list of images
clip = ImageSequenceClip(image_paths, fps=1, load_images=True)  # Adjust the fps as needed
# clip =CompositeVideoClip([
#     ImageClip('1.jpg').set_duration(12),
#     ImageClip('2.jpg').set_duration(12),
#     ImageClip('3.jpg').set_duration(12),
#     ImageClip('4.jpg').set_duration(12),
#     ImageClip('5.jpg').set_duration(12),
# ]).set_fps(1)

# Load the audio clip
audio_clip = AudioFileClip(audio_path).set_duration(60)

# Set the audio of the video clip
video_clip = clip.set_audio(audio_clip)

# Write the final video file
video_clip.write_videofile('output_video.mp4', codec='libx264', audio_codec='aac')

# Make sure you have the MoviePy library installed (`pip install moviepy`) and that you replace the placeholders with your actual file paths.

# This example assumes all images have the same duration and frame rate. If your images have different durations, you may need to adjust the `fps` parameter accordingly.