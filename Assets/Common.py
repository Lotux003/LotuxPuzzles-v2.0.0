import os, sys, time, ctypes

THIS_VERSION = "1.0.0"

def setTitle(_str):
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} - Made By Lotux")
    elif system == 'posix':
        sys.stdout.write(f"\x1b]0;{_str} - Made By Lotux\x07")
    else:
        pass

def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write(f"""\rLoading... {i}""")
		sys.stdout.flush()
		time.sleep(0.2)
		
def transition():
    os.system('cls')
    Spinner()
    os.system('cls')

def lotuxhometitle():
    print(f"""\n\n                            
                            _          _                ____                _            
                           | |    ___ | |_ _   ___  __ |  _ \ _   _ _______| | ___  ___  
                           | |   / _ \| __| | | \ \/ / | |_) | | | |_  /_  / |/ _ \/ __| 
                           | |__| (_) | |_| |_| |>  <  |  __/| |_| |/ / / /| |  __/\__ \ 
                           |_____\___/ \__|\__,_/_/\_\ |_|    \__,_/___/___|_|\___||___/  \n""")
    
def lotuxhometree():
    print(f"""                            
                           .\n
                           └── Puzzles\n
                           │   ├── Maze [01]\n
                           │   └── TicTacToe [02]\n
                           ├── Creators\n
                           │   ├── Lotux [03]\n
                           │   └── Pharoh [04]\n
                           └── Github\n
                               └── github.com/Lotux003/LotuxPuzzles [05]\n\n""")
    
def LineSep():
    print(f"""------------------------------------------------------------------------------------------------------------------------\nLotux | https://github.com/Lotux003 | github.com/Lotux003/LotuxPuzzles | https://github.com/lxrdpharoah | lxrdpharoah\n------------------------------------------------------------------------------------------------------------------------\n""")
