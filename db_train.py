from moviepy.editor import VideoFileClip

video_path = "video\\vid1.mp4"
output_path = "video\\vid_slowed2.mp4"

speed = 0.73  # Set kecepatan yang diinginkan (0.5 untuk setengah kecepatan)

clip = VideoFileClip(video_path)
modified_clip = clip.speedx(speed)
modified_clip.write_videofile(output_path)
