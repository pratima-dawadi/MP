from moviepy.editor import *

from moviepy.editor import VideoFileClip
from PIL import Image
import os

# clip = VideoFileClip(r"C:\Users\Dell\OneDrive\Documents\django_projects\mp_user_upload\movie_test\sample.mp4").subclip(56, 66)
# clip2 = VideoFileClip(r"C:\Users\Dell\OneDrive\Documents\django_projects\mp_user_upload\movie_test\sample.mp4").subclip(70, 76)
# clip3 = VideoFileClip(r"C:\Users\Dell\OneDrive\Documents\django_projects\mp_user_upload\movie_test\sample.mp4").subclip(50, 52)
# clip4 = VideoFileClip(r"C:\Users\Dell\OneDrive\Documents\django_projects\mp_user_upload\movie_test\sample.mp4").subclip(30, 35)
# final_clip = concatenate_videoclips([clip, clip2, clip3, clip4])
# final_clip.write_videofile("output_1.mp4")



# from moviepy.editor import VideoFileClip

# # Load the video
# clip = VideoFileClip(r"C:\Users\Dell\OneDrive\Documents\django_projects\mp_user_upload\media\video\23\video-3da40ab8e7941eb6393547e445e8d475-V_JhjNIRj.mp4")

# # Select the frames to pick (e.g. every 10th frame)
# frames_to_pick = clip.subclip(0, clip.duration).iter_frames(step=10)

# # Save the frames to a file
# for i, frame in enumerate(frames_to_pick):
#     frame_image = Image.fromarray(frame)
#     frame_image.save(f"frame_{i}.png")


# Load the video
clip = VideoFileClip(r"C:\Users\Dell\OneDrive\Documents\django_projects\mp_user_upload\media\video\23\video-3da40ab8e7941eb6393547e445e8d475-V_JhjNIRj.mp4")

fps = clip.fps
frame_skip = 50
frame_count = 0

for frame in clip.iter_frames():
    if frame_count % frame_skip == 0:
        frame_file = os.path.join("frame_images/", f"frame_{frame_count}.png")
        with open(frame_file, "wb") as f:
            # f.write(frame)
            Image.fromarray(frame).save(f, format='png')
    frame_count += 1
clip.reader.close()
clip.audio.reader.close_proc()
