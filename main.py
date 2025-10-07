from moviepy import VideoFileClip, CompositeVideoClip, TextClip
import whisper

text_clips = [] #list for text clips

#model loading
video = VideoFileClip('video.mp4')
model = whisper.load_model("medium")

#extracting audio from video
audio = video.audio
audio.write_audiofile('audio.mp3')

#extracting text from audio
result = model.transcribe('audio.mp3', language='uk')

for seg in result["segments"]:
    txt = TextClip(
        seg["text"].strip(),
        fontsize=32,
        color='white',
        stroke_color='black',
        stroke_width=2
    ).set_start(seg["start"]).set_end(seg["end"]).set_pos("bottom")

    text_clips.append(txt)

final_vid = CompositeVideoClip([video, *text_clips])

final_vid.write_videofile(final_vid)