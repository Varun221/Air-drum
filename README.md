# Air-drum
Beat the drums in the air.
Some things I learned in this project about Object Detection - 
1. Instead of hunting for ranges of values for colour, find them out yourself using cvtColor function (hsv.py)
2. Object tracking can be directly done with the use of masks, basically I am just finding out the number of white cells in the    box and producing the appropriate sound.
3. Noise reduction is done using erode functions.
4. I had to go through many sound libraries to produce sounds from mp3/wav files, pygame works for me.

