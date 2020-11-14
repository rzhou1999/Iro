# Iro (色)

## Introduction

Iro is a visualization project developed for the ASIAN 2252 course at Cornell university. Taking inspiration from projects such as [Harry Potter Movie Colors](http://movie-colors.com/hp/), Iro is intended to serve as an educational and interactive visualization tool that synthesizes and presents usage of color and lighting throughout a film's runtime.

## Webpage Usage

Iro is deployed and viewable online at https://randyzhou.com/Iro/. It is hosted on Github Pages (who we are forever indebted to for free web hosting).

Scrolling over a color bar will also load the corresponding frame, its dominant color's rgb values, as well as its timestamp.

Specific films can be selected using the "Select film" dropdown menu on the upper half of the webpage. We include the contents of the ASIAN 2252 syllabus starting from Kurosawa's *Rashomon* up to Miyazaki's *Spirited Away* (although the missing entries will likely be added once the authors get a spare moment to breathe).

All films are also accessible via direct link by using the "film" [query parameter](https://en.wikipedia.org/wiki/Query_string)-- for example, in order to link directly to the film *I Was Born, But...*, one may use the URL https://randyzhou.com/Iro/?film=iwasbornbut. Only films part of the ASIAN 2252 curriculum are included in the default dropdown, but other [hidden entries](https://github.com/rzhou1999/Iro/tree/master/backend/json) (mostly just KyoAni films because I stan KyoAni *hard*) can be accessed by modifying the URL.

A "scroll mode" which may help when inspecting movies on a closer level can be activated by first enabling the "Fixed length" checkbox, and then reloading the visualizer.

## Developer Usage

Iro can be deployed locally by simply cloning this github repository and hosting on a different webserver. However, due to cross origin request limitations, it does not seem possible to host the entire project locally (in particular, the contents of the backend/json folder cannot be retrieved running locally).

Adding new visualizations can be achieved by using the iro-backend.py script (Python3). You will need to use pip to install some dependencies (see backend/requirements.txt).

`python3 iro-backend.py [movie name] [movie file path] [second sample rate] [scale]`

- [movie name] determines the output json file name, as well as the location where sample frames are saved to (backend/frames/[movie name]).
- [movie file path] is a file path to the video file (we have verified with .mp4 and .m4v, but other formats should theoretically work as well).
- [second sample rate] is how many seconds should be in between each sample frame.
- [scale] is a float that determines how much to scale the final sample images, with respect to the original input video dimensions.

We used the following workflow:

1. Use [HandBrake](https://handbrake.fr/) to downscale input videos (usually targeting a ~144p output video). We also generally changed fps to a constant 24 fps to avoid rounding issues with the second sample rate.
2. Run iro-backend.py as above, with scale set to .75 (this results in approximately 100p images).
3. Push to web (add an extra field in index.html if you want this to appear in the dropdown!).

## Libraries used

D3 for visualization: https://d3js.org/

Color Thief Py for extracting chromatic information from movie stills: https://github.com/fengsp/color-thief-py

OpenCV Python for general image/video processing: https://pypi.org/project/opencv-python/

## Authors

Iro was writen by [Randy Zhou](https://github.com/rzhou1999) and [Alexander DeGraff](https://github.com/degraffa).

## Disclaimer (please don't sue us)

https://randyzhou.com/Iro/disclaimer.html
