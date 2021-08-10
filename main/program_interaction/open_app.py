import os

def open_app(app):
    shortcut = f'C:/Users/Josh/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/{app}.lnk'
    os.startfile(shortcut)


if __name__ == '__main__':
    open_app('Spotify')