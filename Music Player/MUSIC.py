from tkinter import *
from tkinter import filedialog
import pygame
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

root = Tk()
root.title("Music Player")
root.geometry("500x360")

# initialising mixer for music player
pygame.mixer.init()


# Grab Song Length
def play_time():
    # Check for Double timing
    if stopped:
        return
    # grabbed the current song Elapsed time
    current_time = pygame.mixer.music.get_pos() / 1000

    # Temporary label
    # slider_label.config(text=f"Slider : {int(my_slider.get())} and SongPos:{int(current_time)}")

    converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))

    # Get Currently Playing Song
    # current_song = songs_box.curselection()
    # take song title from the playlist
    song = songs_box.get(ACTIVE)
    song = f'C:/Users/sunil/Desktop/code clause/Music Player/MUSIC/{song}.mp3'
    # Get Song Length
    global song_length
    song_MUT = MP3(song)
    song_length = song_MUT.info.length
    converted_Song_Length = time.strftime('%M:%S', time.gmtime(song_length))

    # increase current time by 1
    current_time += 1

    if int(my_slider.get() == int(song_length)):
        status_bar.config(text=f"Time Elapse : {converted_Song_Length} ")

    elif paused:
        pass
    elif int(my_slider.get()) == int(current_time):
        # slider has not been moved
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(current_time))
    else:
        # slider must move
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(my_slider.get()))

        # Convert to time format
        converted_current_time = time.strftime('%M:%S', time.gmtime(int(my_slider.get())))

        # Show length in status Bar
        status_bar.config(text=f"Time Elapse : {converted_current_time} of {converted_Song_Length} ")

        # Move this thing by one second
        next_time = int(my_slider.get()) + 1
        my_slider.config(value=next_time)

    # Show length in status Bar
    # status_bar.config(text=f"Time Elapse : {converted_current_time} of {converted_Song_Length} ")

    # Update slider position value to song position..
    # my_slider.config(value=int(current_time))

    # Update time
    status_bar.after(1000, play_time)


# Add Song Function
def add_song():
    song = filedialog.askopenfilename(initialdir="MUSIC/", title="Choose a Song", filetypes=(("mp3 Files", "*.mp3"),))
    # remove directory from song name
    song = song.replace("C:/Users/sunil/Desktop/code clause/Music Player/MUSIC/", "")
    song = song.replace(".mp3", "")
    # add songs
    songs_box.insert(END, song)


# Add Many Songs to Playlist
def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir="MUSIC/", title="Choose a Song", filetypes=(("mp3 Files", "*.mp3"),))
    for song in songs:
        song = song.replace("C:/Users/sunil/Desktop/code clause/Music Player/MUSIC/", "")
        song = song.replace(".mp3", "")
        songs_box.insert(END, song)


# Play selected song
def play():
    # Set stopped variable to false so the song can play
    global stopped
    stopped = False
    song = songs_box.get(ACTIVE)
    song = f'C:/Users/sunil/Desktop/code clause/Music Player/MUSIC/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Call the play time function
    play_time()

    # Update slider to position
    # slider_position = int(song_length)
    # my_slider.config(to=slider_position, value=0)

    # Get current Volume
    # current_volume = pygame.mixer.music.get_volume()
    # slider_label.config(text =current_volume * 100)


# Stop the song
global stopped
stopped = False


def stop():
    # Reset slider and status bar
    status_bar.config(text="")
    my_slider.config(value=0)
    # Stop Song
    pygame.mixer.music.stop()
    songs_box.selection_clear(ACTIVE)

    # Clear the Status Bar
    status_bar.config(text="")

    # Set stop variable True
    global stopped
    stopped = True


# Global Pause Variable
global paused
paused = False


# Pause and unpause the song
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        # For Unpause
        pygame.mixer.music.unpause()
        paused = False
    else:
        # For Pause
        pygame.mixer.music.pause()
        paused = True


# Play the next song in the playlist
def next_song():
    # Reset slider and status bar
    status_bar.config(text="")
    my_slider.config(value=0)

    # get the current song
    next_one = songs_box.curselection()
    # add one to the current song number
    next_one = next_one[0] + 1
    # take song title from the playlist
    song = songs_box.get(next_one)
    song = f'C:/Users/sunil/Desktop/code clause/Music Player/MUSIC/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Clear active Bar
    songs_box.selection_clear(0, END)
    # Move active Bar to next song
    songs_box.activate(next_one)
    songs_box.selection_set(next_one, last=None)


# Play the previous song in the playlist
def previous_song():
    # Reset slider and status bar
    status_bar.config(text="")
    my_slider.config(value=0)

    # get the current song
    next_one = songs_box.curselection()

    # add one to the current song number
    next_one = next_one[0] - 1

    # Take song title from the playlist
    song = songs_box.get(next_one)
    song = f'C:/Users/sunil/Desktop/code clause/Music Player/MUSIC/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Clear active Bar
    songs_box.selection_clear(0, END)
    # Move active Bar to next song
    songs_box.activate(next_one)
    songs_box.selection_set(next_one, last=None)


# Delete a song
def delete_song():
    stop()
    songs_box.delete(ANCHOR)
    pygame.mixer.music.stop()


# Delete all song from the playlist
def delete_all_songs():
    stop()
    songs_box.delete(0, END)
    pygame.mixer.music.stop()


# Create slider Function
def slide(x):
    # slider_label.config(text=f"{int(my_slider.get())} of {int(song_length)}")
    song = songs_box.get(ACTIVE)
    song = f'C:/Users/sunil/Desktop/code clause/Music Player/MUSIC/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(my_slider.get()))


# Volume Function
def volume(x):
    pygame.mixer.music.set_volume(volume_slider.get())

    # get current Volume
    # current_volume = pygame.mixer.music.get_volume()
    # slider_label.config(text=current_volume * 100)


# Create Master frame
master_frame = Frame(root)
master_frame.pack(pady=20)

# Create playlist for songs
songs_box = Listbox(master_frame, bg="black", fg="green", width=50, selectbackground="gray", selectforeground="Black")
songs_box.grid(row=0, column=0)

# Create Player Control  Images
back_img = PhotoImage(file="Buttons/back.png")
forward_img = PhotoImage(file="Buttons/forward.png")
play_img = PhotoImage(file="Buttons/play.png")
pause_img = PhotoImage(file="Buttons/pause.png")
stop_img = PhotoImage(file="Buttons/stop.png")

# Create Player Control Frames
controls_frame = Frame(master_frame)
controls_frame.grid(row=1, column=0, pady=20)

# Create Volume Control Frame
volume_frame = LabelFrame(master_frame, text="Volume")
volume_frame.grid(row=0, column=1, padx=20)

# Create Player Control Buttons
back_button = Button(controls_frame, image=back_img, borderwidth=0, command=previous_song)
forward_button = Button(controls_frame, image=forward_img, borderwidth=0, command=next_song)
play_button = Button(controls_frame, image=play_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_img, borderwidth=0, command=lambda: pause(paused))
stop_button = Button(controls_frame, image=stop_img, borderwidth=0, command=stop)

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=4, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=1, padx=10)

# Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add songs Menu
add_songs_menu = Menu(my_menu)
my_menu.add_cascade(label="ADD SONGS", menu=add_songs_menu)
add_songs_menu.add_command(label="Add one Song to Playlist", command=add_song)

# Add many songs into playlist
add_songs_menu.add_command(label="Add Many Songs to Playlist", command=add_many_songs)

# Create Delete song Menu
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="REMOVE SONG/SONGS", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete a Song From the Playlist", command=delete_song)
remove_song_menu.add_command(label="Delete all Songs From the Playlist", command=delete_all_songs)

# Create Status bar
status_bar = Label(root, text="", bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

# Create Music Position Slider
my_slider = ttk.Scale(master_frame, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)
my_slider.grid(row=2, column=0, pady=10)


# Volume Slider
volume_slider = ttk.Scale(volume_frame, from_=0, to=1, orient=VERTICAL, value=1, command=volume, length=125)
volume_slider.pack(pady=10)


# Temporary slider label
# slider_label = Label(root, text=0)
# slider_label.pack(pady=10)


root.mainloop()
