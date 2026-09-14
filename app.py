import streamlit as st
import numpy as np

DIGITS = {
    '1': np.array([[0,0,0,1],[0,0,0,1],[0,0,1,1],[0,0,0,1],[0,0,0,1],[0,0,0,1]]),
    '2': np.array([[1,1,1,1],[0,0,0,1],[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,1,1,1]]),
    '3': np.array([[1,1,1,1],[0,0,0,1],[1,1,1,1],[0,0,0,1],[0,0,0,1],[1,1,1,1]]),
    '4': np.array([[1,0,0,1],[1,0,0,1],[1,1,1,1],[0,0,0,1],[0,0,0,1],[0,0,0,1]]),
    '5': np.array([[1,1,1,1],[1,0,0,0],[1,1,1,1],[0,0,0,1],[0,0,0,1],[1,1,1,1]]),
    '6': np.array([[1,1,1,1],[1,0,0,0],[1,1,1,1],[1,0,0,1],[1,0,0,1],[1,1,1,1]]),
    '7': np.array([[1,1,1,1],[0,0,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,1]]),
    '8': np.array([[1,1,1,1],[1,0,0,1],[1,1,1,1],[1,0,0,1],[1,0,0,1],[1,1,1,1]]),
    '9': np.array([[1,1,1,1],[1,0,0,1],[1,1,1,1],[0,0,0,1],[0,0,0,1],[1,1,1,1]]),
    '0': np.array([[1,1,1,1],[1,0,0,1],[1,0,0,1],[1,0,0,1],[1,0,0,1],[1,1,1,1]])
}

PIECES = [
    np.array([[0,0,1,1],[0,0,1,1],[0,0,1,1],[1,1,1,1],[0,1,1,0],[0,1,1,0]]),
    np.array([[0,1,1,0],[0,1,1,0],[0,1,1,1],[1,1,0,0],[0,1,0,0],[0,1,0,0]]),
    np.array([[1,1,1,1],[0,1,0,0],[0,1,1,1],[1,1,1,0],[0,1,1,0],[0,1,1,0]]),
    np.array([[1,1,1,1],[0,0,0,0],[1,1,1,1],[0,0,1,1],[0,0,1,0],[0,0,1,0]]),
    np.array([[0,1,1,0],[0,1,1,0],[0,1,1,1],[1,1,1,1],[0,1,0,0],[1,1,0,0]]),
    np.array([[0,0,1,1],[0,0,1,0],[1,1,1,0],[1,1,1,1],[0,0,1,0],[0,0,1,0]]),
    np.array([[0,0,1,0],[0,0,1,0],[1,1,1,1],[1,1,0,0],[0,1,0,0],[0,1,0,0]]),
    np.array([[1,1,1,1],[0,1,1,0],[0,1,1,1],[0,0,1,1],[0,0,1,0],[0,0,1,0]]),
    np.array([[0,1,1,1],[0,1,1,0],[1,1,1,0],[1,1,1,1],[1,1,0,0],[1,1,0,0]]),
    np.array([[0,1,1,1],[0,1,1,1],[1,1,1,1],[0,1,1,1],[0,1,0,0],[1,1,1,1]]),
    np.array([[0,1,1,1],[0,1,1,1],[1,1,1,1],[1,1,0,0],[0,1,0,0],[0,1,0,0]]),
    np.array([[1,1,1,1],[0,1,1,0],[1,1,1,0],[1,1,1,1],[0,1,0,0],[0,1,0,0]]),
    np.array([[0,1,1,1],[0,1,1,1],[1,1,1,1],[1,1,1,0],[0,0,1,0],[0,0,1,0]]),
    np.array([[1,1,1,1],[0,1,1,0],[1,1,1,1],[1,1,1,0],[1,1,1,0],[1,1,1,0]]),
    np.array([[1,1,1,0],[0,0,1,0],[1,1,1,1],[0,0,1,1],[0,0,1,1],[0,0,1,1]]),
    np.array([[0,1,1,1],[0,1,1,0],[1,1,1,1],[0,0,1,1],[0,0,1,0],[0,0,1,0]])
]

OPPOSITE_QUARTER = {
    'TL': 'BR',
    'TR': 'BL',
    'BL': 'TR',
    'BR': 'TL'
}

def split_digit(digit_matrix):
    return {
        'TL': digit_matrix[0:3, 0:2],
        'TR': digit_matrix[0:3, 2:4],
        'BL': digit_matrix[3:6, 0:2],
        'BR': digit_matrix[3:6, 2:4]
    }

def extract_piece_quarters(piece_matrix):
    return {
        'TL': piece_matrix[0:3, 0:2],
        'TR': piece_matrix[0:3, 2:4],
        'BL': piece_matrix[3:6, 0:2],
        'BR': piece_matrix[3:6, 2:4]
    }

def date_to_2x8_grid(date_str):
    day, month = date_str.split('/')
    digits = list(day + month)
    quarters = [split_digit(DIGITS[d]) for d in digits]
    
    flat_targets = []
    
    for row_idx in [0, 1]:
        q_types = ['TL', 'TR'] if row_idx == 0 else ['BL', 'BR']
        for d_idx, q in enumerate(quarters):
            for qt in q_types:
                flat_targets.append({
                    'digit_idx': d_idx,
                    'target_type': qt,
                    'matrix': q[qt]
                })
    return flat_targets

def solve_recursive(date_str):
    targets = date_to_2x8_grid(date_str)
    used_pieces = set()
    placed_board = [None] * 16 

    def backtrack(slot_idx):
        if slot_idx == 16:
            return True

        target_info = targets[slot_idx]
        required_target_matrix = target_info['matrix']
        target_type = target_info['target_type']
        
        needed_piece_quarter = OPPOSITE_QUARTER[target_type]

        for p_idx, piece in enumerate(PIECES):
            if p_idx in used_pieces:
                continue

            orientations = [piece, np.rot90(piece, 2)]

            for ori in orientations:
                piece_q = extract_piece_quarters(ori)
                candidate_matrix = piece_q[needed_piece_quarter]

                if np.array_equal(candidate_matrix, required_target_matrix):
                    used_pieces.add(p_idx)
                    placed_board[slot_idx] = ori

                    if backtrack(slot_idx + 1):
                        return True

                    used_pieces.remove(p_idx)
                    placed_board[slot_idx] = None

        return False

    success = backtrack(0)
    return success, placed_board

st.set_page_config(page_title="Calendarium puzzle (with rotation) solver", layout="wide")
st.title("Calendarium puzzle (with rotation) solver")

selected_date = st.date_input("Choose a date:")
date_str = selected_date.strftime("%d/%m")

if st.button("Solve the puzzle"):
    st.info(f"Solving the puzzle for: {date_str}...")
    success, solution = solve_recursive(date_str)

    if success:
        st.success("Found a consistent arrangement of blocks!")
        
        full_grid = np.zeros((12, 32), dtype=int)
        for idx in range(16):
            r = (idx // 8) * 6
            c = (idx % 8) * 4
            full_grid[r:r+6, c:c+4] = solution[idx]

        st.subheader("Resulting grid (12x32):")
        scaled_board = np.repeat(np.repeat(full_grid, 15, axis=0), 15, axis=1)
        st.image(scaled_board * 255, width=950)

        st.subheader("Arrangement of blocks in a 2x8 grid:")
        for r in range(2):
            cols = st.columns(8)
            for c in range(8):
                slot_idx = r * 8 + c
                with cols[c]:
                    st.caption(f"Slot #{slot_idx + 1}")
                    scaled_piece = np.repeat(np.repeat(solution[slot_idx], 20, axis=0), 20, axis=1)
                    st.image(scaled_piece * 255, width=100)
    else:
        st.error(f"No solution found for {date_str} with rotation constraints of 0°/180°.")