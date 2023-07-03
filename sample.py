import curses


def main(stdscr):
    # Set up the window
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)  # Non-blocking input
    stdscr.timeout(100)  # Refresh rate in milliseconds

    # Main loop
    while True:
        key = stdscr.getch()  # Get a keypress event

        if key == curses.KEY_UP:
            print("Up arrow key pressed")
            #return 'u'
        elif key == curses.KEY_DOWN:
            print("Down arrow key pressed")
            #return 'd'
        elif key == curses.KEY_LEFT:
            print("Left arrow key pressed")
            #return 'l'
        elif key == curses.KEY_RIGHT:
            print("Right arrow key pressed")
            #return 'r'
        elif key == ord('q'):
            break  # Quit the program if 'q' is pressed

if __name__ == '__main__':
    curses.wrapper(main)