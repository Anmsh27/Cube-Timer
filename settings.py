import ctypes

user32 = ctypes.windll.user32

SCREENSIZE = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))

SCREENWIDTH = SCREENSIZE[0]
SCREENHEIGHT = SCREENSIZE[1]