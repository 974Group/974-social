# Assemble the band version of the "cloth faces" reel: 7 clips, each trimmed, scaled to 1080x1920, with the white "N FACES" label.
import subprocess, json, sys, os
from PIL import Image, ImageDraw, ImageFont
D = os.path.dirname(os.path.abspath(__file__)) + '/'
F = ImageFont.truetype('/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf', 44)
# (clip, label, start, end) seconds inside each generated clip
SEG = json.load(open(D + 'segs.json'))
os.makedirs(D + 'lab', exist_ok=True); os.makedirs(D + 'parts', exist_ok=True)
lst = []
for i, (clip, label, ss, ee) in enumerate(SEG):
    im = Image.new('RGBA', (1080, 120), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.text((540, 60), label, font=F, fill='white', anchor='mm')
    im.save(D + f'lab/{i}.png')
    out = D + f'parts/p{i}.mp4'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(ss), '-to', str(ee), '-i', D + f'clips/{clip}.mp4', '-i', D + f'lab/{i}.png',
                    '-filter_complex', '[0:v]scale=1080:1920:flags=lanczos,fps=24[v];[v][1:v]overlay=0:210,format=yuv420p[o]',
                    '-map', '[o]', '-an', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', D + 'parts/tmp.mp4'], check=True)
    os.replace(D + 'parts/tmp.mp4', out)
    lst.append(f"file '{out}'")
open(D + 'parts/list.txt', 'w').write('\n'.join(lst))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', D + 'parts/list.txt', '-c', 'copy', D + 'parts/video.mp4'], check=True)
dur = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', D + 'parts/video.mp4']))
src = D + '../gen/src_cut.mp4'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', D + 'parts/video.mp4', '-i', src, '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
                '-af', f'afade=t=out:st={dur-0.6:.2f}:d=0.6', '-t', f'{dur:.3f}', '-movflags', '+faststart', D + '../out/tmp.mp4'], check=True)
os.replace(D + '../out/tmp.mp4', D + '../out/974-maroon-faces-reel-v2.mp4')
print('duration', dur)
