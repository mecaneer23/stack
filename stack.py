#!/usr/bin/env python3

import curses


def main(stdscr):
    curses.curs_set(0)
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)
    curses.init_pair(2, curses.COLOR_RED, -1)
    colors = {
        "horizontal": 1,
        "vertical": 2,
    }
    stdscr.nodelay(True)
    stdscr.timeout(100)
    vertical_char = "*"
    horizontal_char = "#"
    score = 0
    screen_size = min(stdscr.getmaxyx()) - 1
    tower_y, tower_x = screen_size * 2 // 3, screen_size * 4 // 3
    last_tower_y, last_tower_x = tower_y, tower_x
    game_win = curses.newwin(
        screen_size,
        int(screen_size * 2),
        stdscr.getmaxyx()[0] // 2 - screen_size // 2,
        stdscr.getmaxyx()[1] // 2 - screen_size,
    )
    game_win.box()
    # while True:
    for i in range(tower_y):
        game_win.addstr(
            (screen_size - tower_y) // 2 + i,
            screen_size - tower_x // 2,
            horizontal_char * tower_x,
            curses.color_pair(colors["horizontal"])
        )
    stdscr.refresh()
    game_win.refresh()
    game_win.getch()


if __name__ == "__main__":
    curses.wrapper(main)
