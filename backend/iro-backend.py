import cv2
from colorthief import ColorThief
import json
import os
import sys

JSON_FOLDER_FILE_PATH = r'json/'

# saves every [frame_sample_rate] frames from the mp4 [movie_file]
# to the /frames folder
def save_frames(movie_file_path, frame_sample_rate):
    frame_colors = []
    
    vidcap = cv2.VideoCapture(movie_file_path)
    success, image = vidcap.read()
    count = 0
    success = True
    while success:
        if count % FRAME_SAMPLE_RATE == 0:
            file_name = r"frames/" + MOVIE_NAME + "/frame%d.jpg" % count
            image = scale_image(image, .2)
            write_image(file_name, image)

            dominant_color = get_dominant_color(file_name)
            frame_colors.append(
                {
                "file_name":"backend/" + file_name,
                "color":dominant_color
                }
            )
    
        success, image = vidcap.read()
        count += 1
        # vidcap.set(cv2.CAP_PROP_FRAME_WIDTH, count * FRAME_SAMPLE_RATE)

    #save json of the colors for each sample frame
    with open(JSON_FOLDER_FILE_PATH + MOVIE_NAME + '.json', 'w') as outfile:
        json.dump(frame_colors, outfile)
# scales a given opencv image by the scale amount
def scale_image(image, scale):
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    dim = (width, height)
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    return resized

# writes an opencv image to disk
def write_image(file_path, image):
    dir_path = file_path[:file_path.rindex("/")]
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    if not cv2.imwrite(file_path, image):
        raise Exception("Could not write image")

def get_dominant_color(img_path):
    color_thief = ColorThief(img_path)
    # get the dominant color
    dominant_color = color_thief.get_color(quality=10)
    return dominant_color


args = sys.argv
if (len(args) != 4):
    print("Expecting: movie name, movie file path, frame sample rate")

MOVIE_NAME = args[1]
MOVIE_FILE_PATH = args[2]
FRAME_SAMPLE_RATE = int(args[3])
    
save_frames(MOVIE_FILE_PATH, FRAME_SAMPLE_RATE)
