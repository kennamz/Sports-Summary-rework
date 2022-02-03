from event import EventType, Make

import time
import vlc
import tkinter as tk
from PIL import ImageTk, Image


class Screen(tk.Frame):

    def __init__(self, parent, video_file_name):
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
        self.parent.geometry("350x600+0+100")

        self.court_img = None

        self.make_court()
        self.make_checkbuttons()
        self.make_controls()
        self.pack(side=tk.TOP, expand=1, fill=tk.BOTH)

        self.video_file_name = video_file_name

    def make_court(self):
        orig_court_width, orig_court_height = 500, 472
        scale_factor = 2 / 3.1
        court_width, court_height = int(orig_court_width * scale_factor), int(orig_court_height * scale_factor)

        canvas = tk.Canvas(self.parent, width=court_width, height=court_height)
        canvas.pack(side=tk.TOP)

        court = Image.open("nbahalfcourt.png").resize((court_width, court_height))
        self.court_img = ImageTk.PhotoImage(court)

        canvas.create_image(3, 3, anchor=tk.NW, image=self.court_img)

    def make_checkbuttons(self):
        frame = tk.Frame(self.parent)

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

        frame.pack(side=tk.TOP)

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

    def play_next_item(self, event):
        self.player.parent.destroy()

        self.summary_index += 1
        summary_item = self.summary[self.summary_index]

        self.new_window = tk.Toplevel(self.parent)
        self.player = Player(self.new_window, self.video_file_name, summary_item.begin_time, summary_item.end_time)

        self.player.events.event_attach(vlc.EventType.MediaPlayerEndReached, self.play_next_item)
        self.player.play()

    def play_summary(self, summary):
        self.summary = summary
        self.summary_index = 0
        summary_item = summary[self.summary_index]

        self.new_window = tk.Toplevel(self.parent)
        self.player = Player(self.new_window, self.video_file_name, summary_item.begin_time, summary_item.end_time)

        self.player.events.event_attach(vlc.EventType.MediaPlayerEndReached, self.play_next_item)
        self.player.play()

    # def play_summary_item(self, summary_item):


class Player:
    def __init__(self, parent, video_file_name, start_timestamp, end_timestamp):
        self.parent = parent
        self.parent.geometry("1100x750+400+25")

        self.frame = tk.Frame(self.parent, width=1100, height=750)
        self.frame.pack()

        self.video_file_name = video_file_name
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.events = self.player.event_manager()

        self.player.set_hwnd(self.frame.winfo_id())
        self.player.play()

        self.start_timestamp = start_timestamp
        self.end_timestamp = end_timestamp

        self.play()

    def play(self):
        media = self.instance.media_new(self.video_file_name)
        media.add_option('start-time=' + str(self.start_timestamp))
        media.add_option('stop-time=' + str(self.end_timestamp))
        media.get_mrl()
        self.player.set_media(media)

        self.player.play()
