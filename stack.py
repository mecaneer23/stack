#!/usr/bin/env python3
#pylint: disable=missing-module-docstring
#pylint: disable=missing-function-docstring, no-member, invalid-name

import curses
from typing import Any


def init(stdscr: Any) -> None:
    curses.curs_set(0)
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)
    curses.init_pair(2, curses.COLOR_RED, -1)
    stdscr.nodelay(True)
    stdscr.timeout(100)


def main(stdscr: Any) -> None:
    init(stdscr)
    colors = {
        "horizontal": 1,
        "vertical": 2,
    }
    vertical_char = "*"
    horizontal_char = "#"
    score = 0
    SCREEN_SIZE = min(stdscr.getmaxyx()) - 1
    tower_y, tower_x = SCREEN_SIZE * 2 // 3, SCREEN_SIZE * 4 // 3
    last_tower_y, last_tower_x = tower_y, tower_x
    game_win = curses.newwin(
        SCREEN_SIZE,
        int(SCREEN_SIZE * 2),
        stdscr.getmaxyx()[0] // 2 - SCREEN_SIZE // 2,
        stdscr.getmaxyx()[1] // 2 - SCREEN_SIZE,
    )
    game_win.box()
    # while True:
    for i in range(tower_y):
        game_win.addstr(
            (SCREEN_SIZE - tower_y) // 2 + i,
            SCREEN_SIZE - tower_x // 2,
            horizontal_char * tower_x,
            curses.color_pair(colors["horizontal"])
        )
    stdscr.refresh()
    game_win.refresh()
    game_win.getch()


if __name__ == "__main__":
    curses.wrapper(main)
