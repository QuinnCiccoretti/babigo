# Import everything needed to edit video clips
from moviepy.editor import *

# Load myHolidays.mp4 and select the subclip 00:00:50 - 00:00:60
clip = VideoFileClip("./jalapenoF.mp4").subclip(30,40)

# Reduce the audio volume (volume x 0.8)
clip = clip.volumex(0.8)



# Write the result to a file (many options available !)
clip.write_videofile("myHolidays_edited.webm")
