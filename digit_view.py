import numpy as np
import streamlit as st

from digit_solver import solve_recursive


def render():
    st.header("Digit Calendar Puzzle")
    st.caption("A 16-piece puzzle matching digit quarters. Allowed rotations: 0° and 180°.")
    selected_date = st.date_input("Choose a date", key="digit_date")
    date_str = selected_date.strftime("%d/%m")

    if not st.button("Solve the digit puzzle", type="primary", key="solve_digits"):
        return

    with st.spinner(f"Solving the puzzle for {date_str}..."):
        success, solution = solve_recursive(date_str)

    if not success:
        st.error(f"No solution found for {date_str}.")
        return

    st.success("A valid arrangement was found.")
    full_grid = np.zeros((12, 32), dtype=int)
    for index, piece in enumerate(solution):
        row = (index // 8) * 6
        col = (index % 8) * 4
        full_grid[row:row + 6, col:col + 4] = piece

    st.subheader("Piece arrangement")
    for row in range(2):
        columns = st.columns(8)
        for col in range(8):
            index = row * 8 + col
            with columns[col]:
                st.caption(f"Piece {index + 1}")
                scaled_piece = np.repeat(np.repeat(solution[index], 20, axis=0), 20, axis=1)
                st.image(scaled_piece * 255, width=100)
