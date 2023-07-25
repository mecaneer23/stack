#!/usr/bin/env python3

import curses


def main(stdscr):
    curses.curs_set(0)
    screen_size = min(stdscr.getmaxyx()) - 1
    game_win = curses.newwin(
        screen_size,
        int(screen_size * 2.11),
        stdscr.getmaxyx()[0] // 2 - screen_size // 2,
        stdscr.getmaxyx()[1] // 2 - screen_size,
    )
    game_win.box()
    while True:
        game_win.getch()
        stdscr.refresh()
        game_win.refresh()


if __name__ == "__main__":
    curses.wrapper(main)
