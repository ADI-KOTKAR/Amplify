import tkinter as tk
from Pages.HomePage.Home import Home
from Pages.Browse.browse import Browse
from Pages.ArtistPage.Artist import Artist
from Pages.AlbumPage.Album import Album
from tkinter import font
from PIL import ImageTk, Image


class IconButton(tk.Button):
    def __init__(self, master, controller, text, image, page, *args, **kwargs):
        tk.Button.__init__(self, master, *args, **kwargs)

        self.appHighlightFont = font.Font(family='lineto circular', size=11, weight='bold')
        self['foreground'] = '#a8a8a8'
        self['background'] = '#121212'
        self['border'] = 0
        self['activebackground'] = '#121212'
        self['activeforeground'] = 'white'
        self['padx'] = 10
        self['pady'] = 5
        self['image'] = image
        self['compound'] = tk.LEFT
        self['text'] = text
        self['anchor'] = tk.W
        self['font'] = self.appHighlightFont
        self['command'] = lambda: controller.show_frame(page)


class NormalButton(tk.Button):
    def __init__(self, master, text, *args, **kwargs):
        tk.Button.__init__(self, master, *args, **kwargs)

        self.appHighlightFont = font.Font(family='lineto circular', size=11, weight='bold')

        self['foreground'] = '#a8a8a8'
        self['background'] = '#121212'
        self['border'] = 0
        self['activebackground'] = '#121212'
        self['activeforeground'] = 'white'
        self['padx'] = 10
        self['pady'] = 5
        self['text'] = text
        self['anchor'] = tk.W
        self['font'] = self.appHighlightFont


class TopLeft(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = '#121212'
        self.master = master

        self.string1 = 	"Copyright "u"\u00A9 2020"

        # font
        self.appHighlightFont = font.Font(family='lineto circular', size=12, weight='bold')
        self.appHighlightFont2 = font.Font(family='lineto circular', size=10)
        self.appHighlightFont3 = font.Font(family='lineto circular', size=9)

        # images
        self.home_icon = tk.PhotoImage(file=r".\Images\home.png")
        self.browse_icon = tk.PhotoImage(file=r".\Images\browse2.png")
        self.menu_icon = tk.PhotoImage(file=r".\Images\menu2.png")
        self.liked_image = Image.open(r".\Images\purple_heart.png")

        # frames
        self.frame1 = tk.Frame(self, bg='#121212', padx=10, pady=10)
        self.frame2 = tk.Frame(self, bg='#121212', padx=10)
        self.frame3 = tk.Frame(self, bg='#121212', padx=10)
        self.frame4 = tk.Frame(self, bg='#000000', padx=10)
        self.frame5 = tk.Frame(self, bg='#000000', padx=10)
        self.line = tk.Frame(self, bg="#2c2c2c", padx=10)

        # frame1
        self.menu2 = tk.Menubutton(self.frame1, image=self.menu_icon, background='#121212', activebackground='#121212',
                                   bd=0)
        self.menu2.menu = tk.Menu(self.menu2,
                                  tearoff=0,
                                  background='#404040', activebackground='#404040',
                                  foreground='white', activeforeground='white',
                                  font=self.appHighlightFont2,
                                  bd=0
                                  )
        self.menu2['menu'] = self.menu2.menu
        self.menu2.menu.add_command(label='AMPLIFY')
        self.menu2.menu.add_command(label=self.string1)
        self.menu2.menu.add_command(label='Contact us:')
        self.menu2.menu.add_command(label='amplifyteam1234@gmail.com')

        # frame2
        self.home = IconButton(self.frame2, master, text='Home', image=self.home_icon, page=Home)
        self.browse = IconButton(self.frame2, master, text='About Us', image=self.browse_icon, page=Browse)

        # frame3
        self.appHighlightFont = font.Font(family='lineto circular', size=9, weight='bold')
        self.label = tk.Label(self.frame3,
                              text='YOUR LIBRARY',
                              background='#121212',
                              foreground='#a8a8a8',
                              anchor=tk.W,
                              padx=5,
                              font=self.appHighlightFont
                              )
        #self.madeForYou = NormalButton(self.frame3, text='Made For You')
        #self.recentlyPlayed = NormalButton(self.frame3, text='Recently Played')
        self.likedSongs = NormalButton(self.frame3,
                                       text='Liked Songs',
                                       command=lambda data=self.get_liked_song(): self.master.show_frame_liked(
                                           data=self.get_liked_song(),
                                           text='Liked Song',
                                           image=self.liked_image))
        self.albums = NormalButton(self.frame3,
                                   text='Albums',
                                   command=lambda: self.master.show_frame(Album))
        self.artists = NormalButton(self.frame3,
                                    text='Artists',
                                    command=lambda: self.master.show_frame(Artist))

        # frame4
        self.label2 = tk.Label(self.frame4,
                               text='AMPLIFY',
                               background='#000000',
                               foreground='#a8a8a8',
                               anchor=tk.W,
                               padx=5,
                               font=self.appHighlightFont
                               )
        self.copyright = tk.Label(self.frame4,
                               text=self.string1,
                               background='#000000',
                               foreground='#a8a8a8',
                               anchor=tk.W,
                               padx=5,
                               font=self.appHighlightFont
                               )
        # frame5
        self.label4 = tk.Label(
                            self.frame5,
                            text='CONTACT US',
                            background="#000000",
                            foreground="#a8a8a8",
                            anchor=tk.W,
                            padx=5,
                            font=self.appHighlightFont
                        )
        self.label3 = tk.Label(
                            self.frame5,
                            text='amplifyteam1234@gmail.com',
                            background="#000000",
                            foreground="#a8a8a8",
                            anchor=tk.W,
                            padx=5,
                            font=self.appHighlightFont2
                        )

        # grid - components
        self.menu2.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
        self.home.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.browse.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.label.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        #self.madeForYou.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        #self.recentlyPlayed.grid(row=2, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.likedSongs.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.albums.grid(row=2, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.artists.grid(row=3, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.copyright.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W, pady=5)        
        self.label2.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W, pady=5)
        self.label3.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W, pady=0)
        self.label4.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W, pady=0)

        # grid - frames
        self.frame1.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.frame2.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.frame3.grid(row=2, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.frame4.grid(row=4, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.frame5.grid(row=5, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.line.grid(row=3, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        # grid - row/column
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=9)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)

        self.frame5.grid_columnconfigure(0, weight=1)
        self.frame5.grid_rowconfigure((0,1), weight=1)

    def logout(self):
        import os
        from Database.Database import sign_out
        from Pages.UserAuthentication.AuthBase import AuthBase
        sign_out()
       
        self.master.master.master.destroy()
        login = AuthBase()
        login.mainloop()

    def get_liked_song(self):
        f = open('user')
    
        x = f.readlines()[0]
        from Database.Database import get_all_liked_songs
       
        
        return get_all_liked_songs(x)

