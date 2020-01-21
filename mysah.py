import webbrowser
import shutil

"""
Configures basic settings to make yourself at home

## Features
- Opens websites
- Sets custom wallpaper

## Future Features
- Opens websites depending on the class



"""


WEBSITES = ['https://mail.google.com/mail/u/0/#inbox', 
'https://calendar.google.com/calendar/r?pli=1',
'https://drive.google.com/drive/my-drive',
'https://catcourses.ucmerced.edu/',
'https://my.ucmerced.edu/uPortal/f/u25l1s4/normal/render.uP']

GASP036 = ['https://www.federicollach.com/music-for-media',
'https://app.slack.com/client/TSFEWL3BK/learning-slack',

]

WALLPAPER_PATH = 'C:/UC_Merced_at_night.png'

def main():
    open_websites()

    
def open_websites():
    for site in WEBSITES:
        webbrowser.open_new(site)

def set_wallpaper():
    dest = shutil.move(WALLPAPER_PATH, WALLPAPER_PATH + '.old')  
    copyfile('./assets/UC_Merced_at_night.png', WALLPAPER_PATH)



if __name__ == "__main__":
    main()


