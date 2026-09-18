from datetime import date

ROW_LENS = [9, 9, 9, 9, 9, 8]

BOARD = [
    [("month", "sty"), ("month", "lut"), ("month", "mar"), ("month", "kwi"), ("day", "1"), ("day", "2"), ("day", "3"), ("weekday", "pon"), ("weekday", "wt")],
    [("month", "maj"), ("day", "4"), ("day", "5"), ("day", "6"), ("day", "7"), ("day", "8"), ("day", "9"), ("weekday", "śr"), ("blank", "X")],
    [("month", "cze"), ("day", "10"), ("day", "11"), ("day", "12"), ("day", "13"), ("day", "14"), ("day", "15"), ("weekday", "czw"), ("blank", "X")],
    [("month", "lip"), ("day", "16"), ("day", "17"), ("day", "18"), ("day", "19"), ("day", "20"), ("day", "21"), ("weekday", "pt"), ("weekday", "sob")],
    [("month", "sie"), ("day", "22"), ("day", "23"), ("day", "24"), ("day", "25"), ("day", "26"), ("day", "27"), ("blank", "X"), ("weekday", "nd")],
    [("month", "wrz"), ("month", "paź"), ("month", "lis"), ("month", "gru"), ("day", "28"), ("day", "29"), ("day", "30"), ("day", "31")],
]

MONTHS = ["sty", "lut", "mar", "kwi", "maj", "cze", "lip", "sie", "wrz", "paź", "lis", "gru"]
WEEKDAYS = ["pon", "wt", "śr", "czw", "pt", "sob", "nd"]

PIECES = [
    [[0, 1], [1, 1], [0, 1], [0, 1]],
    [[0, 0, 1], [0, 0, 1], [1, 1, 1]],
    [[1, 0], [1, 0], [1, 0], [1, 1]],
    [[1, 0], [1, 1], [0, 1], [0, 1]],
    [[1, 1, 0], [0, 1, 0], [0, 1, 1]],
    [[1, 0], [1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1], [0, 1, 0]],
    [[0, 1, 0], [0, 1, 0], [1, 1, 1]],
    [[1, 1, 1, 1, 1]],
    [[1, 1], [0, 1], [1, 1]],
]

PIECE_COLORS = [
    "#c86b4f", "#4f7942", "#3c6e91", "#e11d48", "#c9a13b",
    "#5c8a89", "#a44a3f", "#06b6d4", "#8a9a3b", "#b5602f",
]


def rotate_cw(matrix):
    rows, cols = len(matrix), len(matrix[0])
    rotated = [[0] * rows for _ in range(cols)]
    for row in range(rows):
        for col in range(cols):
            rotated[col][rows - 1 - row] = matrix[row][col]
    return rotated


def unique_rotations(piece):
    variants = []
    seen = set()
    current = piece
    degrees = 0
    for _ in range(4):
        key = tuple(tuple(row) for row in current)
        if key not in seen:
            seen.add(key)
            variants.append((current, degrees))
        current = rotate_cw(current)
        degrees = (degrees + 90) % 360
    return variants


PIECE_VARIANTS = [unique_rotations(piece) for piece in PIECES]


def find_target_cells(day, month_idx, weekday_idx):
    wanted = {"month": MONTHS[month_idx], "day": str(day), "weekday": WEEKDAYS[weekday_idx]}
    found = {}
    cells = []
    for row in range(6):
        for col in range(ROW_LENS[row]):
            cell_type, label = BOARD[row][col]
            if cell_type in wanted and label == wanted[cell_type] and cell_type not in found:
                found[cell_type] = (row, col)
                cells.append((row, col))
    missing = [key for key in ("month", "day", "weekday") if key not in found]
    if missing:
        raise ValueError("The board is missing a cell for: " + ", ".join(wanted[key] for key in missing))
    return cells


def solve_puzzle(target_cells):
    covered = [[col >= ROW_LENS[row] for col in range(9)] for row in range(6)]
    for row, col in target_cells:
        covered[row][col] = True

    used = [False] * len(PIECES)
    placements = [None] * len(PIECES)

    def find_empty():
        for row in range(6):
            for col in range(ROW_LENS[row]):
                if not covered[row][col]:
                    return row, col
        return None

    def is_valid(variant, anchor_row, anchor_col):
        for row_idx, row in enumerate(variant):
            for col_idx, value in enumerate(row):
                if not value:
                    continue
                row_pos = anchor_row + row_idx
                col_pos = anchor_col + col_idx
                if row_pos < 0 or row_pos > 5 or col_pos < 0 or col_pos >= ROW_LENS[row_pos] or covered[row_pos][col_pos]:
                    return False
        return True

    def set_covered(variant, anchor_row, anchor_col, value):
        for row_idx, row in enumerate(variant):
            for col_idx, cell in enumerate(row):
                if cell:
                    covered[anchor_row + row_idx][anchor_col + col_idx] = value

    def backtrack():
        empty = find_empty()
        if empty is None:
            return all(used)
        target_row, target_col = empty
        for piece_idx, variants in enumerate(PIECE_VARIANTS):
            if used[piece_idx]:
                continue
            for variant, degrees in variants:
                for row_idx, row in enumerate(variant):
                    for col_idx, value in enumerate(row):
                        if not value:
                            continue
                        anchor_row = target_row - row_idx
                        anchor_col = target_col - col_idx
                        if not is_valid(variant, anchor_row, anchor_col):
                            continue
                        set_covered(variant, anchor_row, anchor_col, True)
                        used[piece_idx] = True
                        placements[piece_idx] = {
                            "cells": [
                                (anchor_row + item_row, anchor_col + item_col)
                                for item_row, variant_row in enumerate(variant)
                                for item_col, item in enumerate(variant_row)
                                if item
                            ],
                            "deg": degrees,
                        }
                        if backtrack():
                            return True
                        used[piece_idx] = False
                        placements[piece_idx] = None
                        set_covered(variant, anchor_row, anchor_col, False)
        return False

    return placements if backtrack() else None


def weekday_index(day: date):
    return day.weekday()
