import numpy as np

DIGITS = {
    "1": np.array([[0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1]]),
    "2": np.array([[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 1, 1, 1]]),
    "3": np.array([[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1], [1, 1, 1, 1]]),
    "4": np.array([[1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1]]),
    "5": np.array([[1, 1, 1, 1], [1, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1], [1, 1, 1, 1]]),
    "6": np.array([[1, 1, 1, 1], [1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]]),
    "7": np.array([[1, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1]]),
    "8": np.array([[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]]),
    "9": np.array([[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1], [1, 1, 1, 1]]),
    "0": np.array([[1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]]),
}

PIECES = [
    np.array([[0, 0, 1, 1], [0, 0, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 1, 1, 0], [0, 1, 1, 0]]),
    np.array([[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]]),
    np.array([[1, 1, 1, 1], [0, 1, 0, 0], [0, 1, 1, 1], [1, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]]),
    np.array([[1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 1, 1], [0, 0, 1, 0], [0, 0, 1, 0]]),
    np.array([[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 0, 0], [1, 1, 0, 0]]),
    np.array([[0, 0, 1, 1], [0, 0, 1, 0], [1, 1, 1, 0], [1, 1, 1, 1], [0, 0, 1, 0], [0, 0, 1, 0]]),
    np.array([[0, 0, 1, 0], [0, 0, 1, 0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]]),
    np.array([[1, 1, 1, 1], [0, 1, 1, 0], [0, 1, 1, 1], [0, 0, 1, 1], [0, 0, 1, 0], [0, 0, 1, 0]]),
    np.array([[0, 1, 1, 1], [0, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 1], [1, 1, 0, 0], [1, 1, 0, 0]]),
    np.array([[0, 1, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 0, 0], [1, 1, 1, 1]]),
    np.array([[0, 1, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]]),
    np.array([[1, 1, 1, 1], [0, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 1], [0, 1, 0, 0], [0, 1, 0, 0]]),
    np.array([[0, 1, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]]),
    np.array([[1, 1, 1, 1], [0, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 0]]),
    np.array([[1, 1, 1, 0], [0, 0, 1, 0], [1, 1, 1, 1], [0, 0, 1, 1], [0, 0, 1, 1], [0, 0, 1, 1]]),
    np.array([[0, 1, 1, 1], [0, 1, 1, 0], [1, 1, 1, 1], [0, 0, 1, 1], [0, 0, 1, 0], [0, 0, 1, 0]]),
]

OPPOSITE_QUARTER = {"TL": "BR", "TR": "BL", "BL": "TR", "BR": "TL"}


def split_digit(digit_matrix):
    return {
        "TL": digit_matrix[0:3, 0:2],
        "TR": digit_matrix[0:3, 2:4],
        "BL": digit_matrix[3:6, 0:2],
        "BR": digit_matrix[3:6, 2:4],
    }


def extract_piece_quarters(piece_matrix):
    return {
        "TL": piece_matrix[0:3, 0:2],
        "TR": piece_matrix[0:3, 2:4],
        "BL": piece_matrix[3:6, 0:2],
        "BR": piece_matrix[3:6, 2:4],
    }


def date_to_targets(date_str):
    day, month = date_str.split("/")
    quarters = [split_digit(DIGITS[digit]) for digit in day + month]
    targets = []
    for row_idx in range(2):
        quarter_types = ["TL", "TR"] if row_idx == 0 else ["BL", "BR"]
        for digit_idx, quarters_by_type in enumerate(quarters):
            for target_type in quarter_types:
                targets.append({
                    "digit_idx": digit_idx,
                    "target_type": target_type,
                    "matrix": quarters_by_type[target_type],
                })
    return targets


def solve_recursive(date_str):
    targets = date_to_targets(date_str)
    used_pieces = set()
    placed_board = [None] * len(PIECES)

    def backtrack(slot_idx):
        if slot_idx == len(placed_board):
            return True
        target = targets[slot_idx]
        needed_quarter = OPPOSITE_QUARTER[target["target_type"]]
        for piece_idx, piece in enumerate(PIECES):
            if piece_idx in used_pieces:
                continue
            for orientation in (piece, np.rot90(piece, 2)):
                candidate = extract_piece_quarters(orientation)[needed_quarter]
                if not np.array_equal(candidate, target["matrix"]):
                    continue
                used_pieces.add(piece_idx)
                placed_board[slot_idx] = orientation
                if backtrack(slot_idx + 1):
                    return True
                used_pieces.remove(piece_idx)
                placed_board[slot_idx] = None
        return False

    return backtrack(0), placed_board
