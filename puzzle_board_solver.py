import sys
import time
from datetime import date

from board_solver import BOARD, ROW_LENS, WEEKDAYS, find_target_cells, solve_puzzle, weekday_index


def run_cli(day):
    target_cells = find_target_cells(day.day, day.month - 1, weekday_index(day))
    started = time.perf_counter()
    placements = solve_puzzle(target_cells)
    elapsed = (time.perf_counter() - started) * 1000

    if placements is None:
        print("No solution found for this date.")
        sys.exit(1)

    target_set = set(target_cells)
    cell_piece = {}
    for piece_index, placement in enumerate(placements):
        for cell in placement["cells"]:
            cell_piece[cell] = piece_index

    print(f"{day.isoformat()} ({WEEKDAYS[weekday_index(day)]}) - solved in {elapsed:.0f} ms\n")
    for row in range(6):
        values = []
        for col in range(ROW_LENS[row]):
            cell = (row, col)
            if cell in target_set:
                values.append(f"[{BOARD[row][col][1]:>3}]")
            elif cell in cell_piece:
                values.append(f" {cell_piece[cell] + 1:>2} ")
            else:
                values.append("  ·  ")
        print("".join(values))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Enter a date in YYYY-MM-DD format.")
        sys.exit(1)
    try:
        year, month, day = (int(value) for value in sys.argv[1].split("-"))
        run_cli(date(year, month, day))
    except ValueError as error:
        print(f"Error: {error}")
        sys.exit(1)
