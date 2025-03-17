from natsort import natsorted
import subprocess as sp
import argparse
import glob
import re
import os

parser = argparse.ArgumentParser(
    description="Create animation from rendered frames using ffmpeg"
)
parser.add_argument(
    "-i", "--dir", type=str, help="Directory containing frames", required=True
)
parser.add_argument("-o", "--output", type=str, help="Output file name", required=True)
parser.add_argument(
    "-k",
    "--keep",
    action="store_true",
    help="Keep frames after animation",
    default=False,
)
args = parser.parse_args()

# Create list of frames in directory
frames = [
    img
    for img in glob.glob(f"{args.dir}/*.png")
    if re.search(r"^area_render(_\d+_)?\.png$", os.path.basename(img))
]
frames = natsorted(frames)

# Create list of frames for ffmpeg
with open("frames.txt", "w") as f:
    for frame in frames:
        frame = frame.replace("\\", "/")
        f.write(f"file '{frame}'\n")

# Create base animation
base_animation = "ffmpeg -r 20 -safe 0 -f concat -i frames.txt -c:v libx264 -pix_fmt yuv420p -y ./temp.mp4"
sp.run(base_animation)
os.unlink("frames.txt")

# Repeat first frame of animation to add delay
repeat_first_frame = (
    "ffmpeg -i temp.mp4"
    ' -filter_complex "[0:v]loop=loop=-1:size=1,trim=end=1[v0];[v0][0:v]concat"'
    f" -y {args.output}"
)
sp.run(repeat_first_frame)
os.unlink("temp.mp4")

# Remove frames if not keeping
if not args.keep:
    for frame in frames:
        os.unlink(frame)
