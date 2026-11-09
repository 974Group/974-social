#!/bin/bash
# Compose the hoodie spin story: grey canvas + scaled feathered video + Designy overlay
# usage: build.sh <A.mp4> <B.mp4> <out.mp4>
set -e
A=$1; B=$2; OUT=$3
VW=778; VH=1382; X=151; Y=232
python3 - <<EOF
from PIL import Image, ImageFilter, ImageDraw
import subprocess, numpy as np
# feather mask
m=Image.new('L',($VW,$VH),0); d=ImageDraw.Draw(m); f=70
d.rectangle([f,f,$VW-f,$VH-f],fill=255); m=m.filter(ImageFilter.GaussianBlur(f/2.2)); m.save('mask.png')
# background colour from the first frame's border
raw=subprocess.run(['ffmpeg','-v','error','-i','$A','-frames:v','1','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
a=np.frombuffer(raw,np.uint8).reshape(1924,1076,3)
b=np.concatenate([a[:40].reshape(-1,3),a[:, :30].reshape(-1,3),a[:, -30:].reshape(-1,3)])
c=np.median(b,axis=0).astype(int); open('bg.txt','w').write('0x%02x%02x%02x'%tuple(c)); print(c)
EOF
BG=$(cat bg.txt)
seg(){ # in, start_hold, stop_hold, out
ffmpeg -v error -y -i "$1" -loop 1 -i mask.png -loop 1 -i overlay.png -f lavfi -i "color=$BG:s=1080x1920:r=30" -filter_complex "
[0:v]fps=30,scale=$VW:$VH:flags=lanczos,tpad=start_mode=clone:start_duration=$2:stop_mode=clone:stop_duration=$3,format=rgb24[v];
[1:v]format=gray,scale=$VW:$VH[m];[v][m]alphamerge[va];
[3:v][va]overlay=$X:$Y:shortest=1[c];[c][2:v]overlay=0:0:shortest=1,format=yuv420p[o]" -t $5 -map "[o]" -c:v libx264 -preset veryfast -crf 17 -r 30 "$4.tmp.mp4" && mv "$4.tmp.mp4" "$4"; }
seg "$A" 0.7 1.1 segA.mp4 6.84
seg "$B" 0 0.9 segB.mp4 5.94
printf "file segA.mp4\nfile segB.mp4\n" > list.txt
ffmpeg -v error -y -f concat -safe 0 -i list.txt -c copy -movflags +faststart "$OUT.tmp.mp4" && mv "$OUT.tmp.mp4" "$OUT"
