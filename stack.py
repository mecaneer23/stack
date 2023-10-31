#!/usr/bin/env python3
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring, no-member, invalid-name

import curses
from typing import Any


def init(stdscr: Any) -> None:
    curses.curs_set(0)
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)
    curses.init_pair(2, curses.COLOR_RED, -1)
    stdscr.nodelay(True)
    stdscr.timeout(100)


def draw_vertical() -> None:
    CHAR = "*"
    raise NotImplementedError("draw_vertical")


def draw_horizontal(
    game_win: Any, screen_size: int, begin_y: int, begin_x: int, height: int, width: int
) -> None:
    CHAR = "#"
    for i in range(width):
        game_win.addstr(
            (screen_size - width) // 2 + i,
            screen_size - height // 2,
            CHAR * height,
            curses.color_pair(1),
        )


def clamp(counter: int, minimum: int, maximum: int) -> int:
    return min(max(counter, minimum), maximum - 1)


def get_start_pos(screen_yx: tuple[int, int], direction_is_horizontal: bool, heading_is_positive: bool, start_pos: int) -> int:
    if direction_is_horizontal:
        return clamp(start_pos, 0, screen_yx[1])
    raise NotImplementedError()
    # return clamp()


def main(stdscr: Any) -> None:
    init(stdscr)
    score = 0
    direction_is_horizontal = True
    screen_size = min(stdscr.getmaxyx()) - 1
    tower_width, tower_height = screen_size * 2 // 3, screen_size * 4 // 3
    last_width, last_height = tower_width, tower_height
    game_win = curses.newwin(
        screen_size,
        int(screen_size * 2),
        stdscr.getmaxyx()[0] // 2 - screen_size // 2,
        stdscr.getmaxyx()[1] // 2 - screen_size,
    )
    start_pos = 0
    while True:
        game_win.box()
        try:
            if game_win.getch() != -1:
                score += 1
                direction_is_horizontal = not direction_is_horizontal
        except KeyboardInterrupt:
            return
        if direction_is_horizontal:
            draw_horizontal(game_win, screen_size, 0, 0, tower_height, tower_width)
        # else:
        #     draw_vertical(game_win, screen_size, _, _, tower_height, tower_width)
        start_pos = get_start_pos(game_win.getmaxyx(), direction_is_horizontal, heading_is_positive, start_pos)
        stdscr.refresh()
        game_win.refresh()


if __name__ == "__main__":
    curses.wrapper(main)
