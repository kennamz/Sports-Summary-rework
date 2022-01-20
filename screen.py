from event import EventType, Make

import time
import vlc
import tkinter as tk
from PIL import ImageTk, Image


class Screen(tk.Frame):

    def __init__(self, parent):
        self.events_filter = {
            (EventType.FREE_THROW, Make.MAKE): tk.BooleanVar(),
            (EventType.FREE_THROW, Make.MISS): tk.BooleanVar(),
            (EventType.TWO_PTR, Make.MAKE): tk.BooleanVar(),
            (EventType.TWO_PTR, Make.MISS): tk.BooleanVar(),
            (EventType.THREE_PTR, Make.MAKE): tk.BooleanVar(),
            (EventType.THREE_PTR, Make.MISS): tk.BooleanVar(),
            EventType.REBOUND: tk.BooleanVar(),
            EventType.FOUL: tk.BooleanVar(),
            EventType.TURNOVER: tk.BooleanVar(),
            EventType.VIOLATION: tk.BooleanVar(),
            EventType.TIMEOUT: tk.BooleanVar(),
            EventType.ENTERS_THE_GAME: tk.BooleanVar(),
            EventType.JUMP_BALL: tk.BooleanVar(),
            EventType.QUARTER_START_END: tk.BooleanVar(),
            EventType.INSTANT_REPLAY: tk.BooleanVar(),
            EventType.EJECTION: tk.BooleanVar()
        }

        tk.Frame.__init__(self, parent, bg='black')
        self.parent = parent
        self.parent.state('zoomed')

        # Creating VLC player
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

        self.court_img_top, self.court_img_bottom = None, None

        self.make_court()
        self.make_controls()
        self.pack(side=tk.TOP, expand=1, fill=tk.BOTH)

        self.play('LongOvertimeClip.mp4')

    def make_court(self):
        frame = tk.Frame(self.parent)

        orig_court_width, orig_court_height = 500, 472
        scale_factor = 2 / 3.1
        court_width, court_height = int(orig_court_width * scale_factor), int(orig_court_height * scale_factor)

        canvas = tk.Canvas(frame, width=court_width, height=court_height * 2)
        canvas.pack(side=tk.TOP)

        court = Image.open("nbahalfcourt.png").resize((court_width, court_height))
        self.court_img_top = ImageTk.PhotoImage(court)
        court = court.rotate(180)
        self.court_img_bottom = ImageTk.PhotoImage(court)

        canvas.create_image(3, 3, anchor=tk.NW, image=self.court_img_top)
        canvas.create_image(3, court_height + 1, anchor=tk.NW, image=self.court_img_bottom)

        checkbuttons_frame = tk.Frame(frame)
        self.make_checkbuttons(checkbuttons_frame)
        checkbuttons_frame.pack(side=tk.BOTTOM)

        frame.pack(side=tk.RIGHT)

    def make_checkbuttons(self, frame):
        c1 = tk.Checkbutton(frame, text='Free Throw Made', onvalue=True, offvalue=False,
                            variable=self.events_filter[(EventType.FREE_THROW, Make.MAKE)])
        c1.grid(row=0, column=0)

        c2 = tk.Checkbutton(frame, text='Free Throw Missed', onvalue=True, offvalue=False,
                            variable=self.events_filter[(EventType.FREE_THROW, Make.MISS)])
        c2.grid(row=1, column=0)

        c3 = tk.Checkbutton(frame, text='2 Pointer Made', onvalue=True, offvalue=False,
                            variable=self.events_filter[(EventType.TWO_PTR, Make.MAKE)])
        c3.grid(row=2, column=0)

        c4 = tk.Checkbutton(frame, text='2 Pointer Missed', onvalue=True, offvalue=False,
                            variable=self.events_filter[(EventType.TWO_PTR, Make.MISS)])
        c4.grid(row=3, column=0)

        c5 = tk.Checkbutton(frame, text='3 Pointer Made', onvalue=True, offvalue=False,
                            variable=self.events_filter[(EventType.THREE_PTR, Make.MAKE)])
        c5.grid(row=4, column=0)

        c6 = tk.Checkbutton(frame, text='3 Pointer Missed', onvalue=True, offvalue=False,
                            variable=self.events_filter[(EventType.THREE_PTR, Make.MISS)])
        c6.grid(row=5, column=0)

        c7 = tk.Checkbutton(frame, text='Rebound', variable=self.events_filter[EventType.REBOUND],
                            onvalue=True, offvalue=False)
        c7.grid(row=6, column=0)

        c8 = tk.Checkbutton(frame, text='Foul', variable=self.events_filter[EventType.FOUL],
                            onvalue=True, offvalue=False)
        c8.grid(row=7, column=0)

        c8 = tk.Checkbutton(frame, text='Turnover', variable=self.events_filter[EventType.TURNOVER],
                            onvalue=True, offvalue=False)
        c8.grid(row=0, column=1)

        c9 = tk.Checkbutton(frame, text='Violation', variable=self.events_filter[EventType.VIOLATION],
                            onvalue=True, offvalue=False)
        c9.grid(row=1, column=1)

        c10 = tk.Checkbutton(frame, text='Timeout', variable=self.events_filter[EventType.TIMEOUT],
                             onvalue=True, offvalue=False)
        c10.grid(row=2, column=1)

        c11 = tk.Checkbutton(frame, text='Enters the game', variable=self.events_filter[EventType.ENTERS_THE_GAME],
                             onvalue=True, offvalue=False)
        c11.grid(row=3, column=1)

        c12 = tk.Checkbutton(frame, text='Jump Ball', variable=self.events_filter[EventType.JUMP_BALL],
                             onvalue=True, offvalue=False)
        c12.grid(row=4, column=1)

        c13 = tk.Checkbutton(frame, text='Quarter Start/End', variable=self.events_filter[EventType.QUARTER_START_END],
                             onvalue=True, offvalue=False)
        c13.grid(row=5, column=1)

        c14 = tk.Checkbutton(frame, text='Instant Replay', variable=self.events_filter[EventType.INSTANT_REPLAY],
                             onvalue=True, offvalue=False)
        c14.grid(row=6, column=1)

        c15 = tk.Checkbutton(frame, text='Ejection', variable=self.events_filter[EventType.EJECTION],
                             onvalue=True, offvalue=False)
        c15.grid(row=7, column=1)

    def make_controls(self):
        controls = tk.Frame(self.parent)
        previous_play = tk.Button(controls, text="Previous")
        pause = tk.Button(controls, text="Pause")
        play = tk.Button(controls, text="Play")
        stop = tk.Button(controls, text="Stop")
        next_play = tk.Button(controls, text="Next")
        pady, ipadx, ipady = 2, 10, 1
        previous_play.pack(side=tk.LEFT, padx=200, pady=pady, ipadx=ipadx, ipady=ipady)
        pause.pack(side=tk.LEFT, padx=5, pady=pady, ipadx=ipadx, ipady=ipady)
        play.pack(side=tk.LEFT, padx=5, pady=pady, ipadx=ipadx, ipady=ipady)
        stop.pack(side=tk.LEFT, padx=50, pady=pady, ipadx=ipadx, ipady=ipady)
        next_play.pack(side=tk.LEFT, padx=200, pady=pady, ipadx=ipadx, ipady=ipady)
        controls.pack(side=tk.BOTTOM)

        duration_slider = tk.Frame(self.parent)
        self.scale_var = tk.DoubleVar()
        self.timeslider_last_val = ""
        self.timeslider = tk.Scale(duration_slider, variable=self.scale_var,
                                   from_=0, to=1000, orient=tk.HORIZONTAL, length=500)
        self.timeslider.pack(side=tk.BOTTOM, fill=tk.X, expand=1)
        self.timeslider_last_update = time.time()
        duration_slider.pack(side=tk.BOTTOM, fill=tk.X)

    def play(self, _source):
        # Function to start player from given source
        media = self.instance.media_new(_source)
        media.get_mrl()
        self.player.set_media(media)

        self.player.set_hwnd(self.winfo_id())
        self.player.play()
