import tkinter as tk
import os
import make_subtitles
import render_video as rv
from tkinter.messagebox import showerror, showinfo
from tkinter import font as ft, filedialog as fd


class App:
    def __init__(self):
        root = tk.Tk()
        root.title("Captions maker")
        root.geometry("500x500+400+100")
        root['bg'] = 'steel blue'
        root.resizable(False, False)

        #variable to store selected video path
        self.selected_video_path = None

        def select_video():
            showinfo("Info", "Please select a video file. Then captions will be created and you can edit them.")
            #asking user to select a video file
            path = fd.askopenfilename(title="Select video file",
                                              filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv")])
            if path:
                self.selected_video_path = path
                make_subtitles.make_subtitles(path)
            else:
                showerror("Warning", "No video file selected.")
                return


        tk.Label(text="Captions maker", font=('Arial', 40, 'bold'), bg='steel blue').pack(pady=10)

        #create captions button
        create_subtitle = tk.Button(root, text="Create captions", font=('Arial', 14), bg='steel blue', width=20, height=2, command=select_video)
        create_subtitle.pack(pady=20)

        render_video = tk.Button(root, text="Render video", font=('Arial', 14), bg='steel blue', width=20, height=2, command=lambda: rv.render_video(self.selected_video_path))
        render_video.pack(pady=20)

        root.mainloop()


App()
