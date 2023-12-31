#!/usr/bin/env python3
# pylint: disable=missing-module-docstring, missing-class-docstring
# pylint: disable=missing-function-docstring, no-member

import curses
from enum import Enum
from typing import Any


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Character(Enum):
    VERTICAL = "*"
    HORIZONTAL = "#"
    NONE = ""


def init(stdscr: Any) -> None:
    curses.curs_set(0)
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)
    curses.init_pair(2, curses.COLOR_RED, -1)
    stdscr.nodelay(True)
    stdscr.timeout(100)


def is_horizontal(direction: Direction) -> bool:
    return direction in (Direction.LEFT, Direction.RIGHT)


def is_vertical(direction: Direction) -> bool:
    return direction in (Direction.UP, Direction.DOWN)


def opposite(direction: Direction) -> Direction:
    return {
        Direction.UP: Direction.DOWN,
        Direction.DOWN: Direction.UP,
        Direction.RIGHT: Direction.LEFT,
        Direction.LEFT: Direction.RIGHT,
    }[direction]


def draw(
    game_win: Any,
    screen_size: int,
    begin_y: int,
    begin_x: int,
    height: int,
    width: int,
    char: Character,
) -> None:
    for i in range(width):
        game_win.addstr(
            (screen_size - width) // 2 + i,
            screen_size - height // 2,
            char.value * height,
            curses.color_pair(1),
        )


def get_char(direction: Direction) -> Character:
    if is_horizontal(direction):
        return Character.HORIZONTAL
    if is_vertical(direction):
        return Character.VERTICAL
    return Character.NONE


def get_start_pos(
    screen_yx: tuple[int, int], direction: Direction, start_pos: int
) -> tuple[int, Direction]:
    if is_horizontal(direction):
        if start_pos < 0:
            return 0, Direction.RIGHT
        if start_pos > screen_yx[1]:
            return screen_yx[1], Direction.LEFT
    if is_vertical(direction):
        if start_pos < 0:
            return 0, Direction.UP
        if start_pos > screen_yx[0]:
            return screen_yx[0], Direction.DOWN
    return start_pos, direction


def main(stdscr: Any) -> None:
    init(stdscr)
    score = 0
    direction = Direction.RIGHT
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
    draw(game_win, screen_size, 0, 0, tower_height, tower_width, Character.VERTICAL)
    while True:
        game_win.box()
        try:
            if game_win.getch() != -1:
                score += 1
                direction = opposite(direction)
        except KeyboardInterrupt:
            return
        draw(game_win, screen_size, 0, start_pos, tower_height, tower_width, get_char(direction))
        start_pos, direction = get_start_pos(game_win.getmaxyx(), direction, start_pos)
        stdscr.refresh()
        game_win.refresh()


if __name__ == "__main__":
    curses.wrapper(main)
