from moviepy import TextClip, VideoFileClip, CompositeVideoClip
from tkinter.messagebox import showerror, showinfo
import os

font = './fonts/Overpass.ttf'

def str_to_sec(time_str):
    time_str = time_str.replace(',', '.')

    parts = time_str.split(':')
    h = float(parts[0])
    m = float(parts[1])
    s = float(parts[2])

    return h * 3600 + m * 60 + s

def create_clips_from_srt(srt_filepath, video_width):
    final_clips = []

    with open(srt_filepath, 'r', encoding='utf-8') as f:

        content = f.read().strip().split('\n\n')

    for block in content:
        lines = block.split('\n')

        if len(lines) < 3 or not lines[0].isdigit():
            continue


        try:
            times = lines[1].split(' --> ')
            start_sec = str_to_sec(times[0])
            end_sec = str_to_sec(times[1])
        except Exception:

            continue


        text_content = '\n'.join(lines[2:]).strip()


        txt_clip = TextClip(
            text=text_content,
            font=font,
            font_size=32,
            color='white',
            stroke_color='black',
            stroke_width=2,
            method='caption',
            size=(video_width, 600)
        ).with_start(start_sec).with_end(end_sec).with_position('bottom')

        final_clips.append(txt_clip)

    return final_clips

def render_video(video_path):
    if not video_path:
        showerror("Error", "Create captions first before rendering the video.")
        return
    
    video = VideoFileClip(video_path)

    text_clips = create_clips_from_srt('subs.srt', video.w)
    vid = CompositeVideoClip([video, *text_clips])

    showinfo("Info", "Rendering video. This may take a while... Don't close the program.")
    vid.write_videofile('result.mp4', threads=4)
    showinfo("Success", "Video rendered successfully as result.mp4. Opening it...")
    os.system('open result.mp4')