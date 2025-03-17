import subprocess as sp
import argparse

parser = argparse.ArgumentParser(
    description="Concatenate two videos into one using ffmpeg"
)
parser.add_argument("-1", "--first", type=str, help="First video file", required=True)
parser.add_argument("-2", "--second", type=str, help="Second video file", required=True)
parser.add_argument("-o", "--output", type=str, help="Output video file", required=True)
args = parser.parse_args()

concat_videos = f'ffmpeg -i {args.first} -i {args.second} -filter_complex "concat=n=2" -y {args.output}'
sp.run(concat_videos)
