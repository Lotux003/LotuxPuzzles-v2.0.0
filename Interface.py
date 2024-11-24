import os, sys, time, subprocess, webbrowser
from Assets import Common

system = os.name

def clear():
    os.system('cls')

def spawn_program_and_die(program, exit_code=0):
    subprocess.run(program)
    #sys.exit(exit_code)


def main():
    os.system('cls')
    Common.setTitle(f"Lotux Puzzles v{Common.THIS_VERSION}")
    Common.transition()
    Common.lotuxhometitle()
    Common.LineSep()
    Common.lotuxhometree()
    choice = int(input("[#] Choice: "))
    if choice == 1:
        Common.transition()
        #spawn_program_and_die(['python', 'Games/Maze.py'])
        subprocess.run('python Games/Maze.py')
    if choice == 2:
        Common.transition()
        #spawn_program_and_die(['python', 'Games/TicTacToe.py'])
        subprocess.run('python Games/TicTacToe.py')
    if choice == 3:
        Common.transition()
        webbrowser.open('https://github.com/Lotux003')
    if choice == 4:
        Common.transition()
        webbrowser.open('https://github.com/lxrdpharoah')
    if choice == 5:
        Common.transition()
        webbrowser.open('https://github.com/Lotux003/LotuxPuzzles')
main()
