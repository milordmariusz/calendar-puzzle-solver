import streamlit as st

from board_solver import BOARD, PIECE_COLORS, ROW_LENS, find_target_cells, solve_puzzle, weekday_index


def render_board(placements, target_cells):
    target_set = set(target_cells)
    cell_piece = {}
    if placements:
        for piece_index, placement in enumerate(placements):
            for cell in placement["cells"]:
                cell_piece[cell] = piece_index

    rows = []
    for row in range(6):
        cells = []
        for col in range(9):
            if col >= ROW_LENS[row]:
                cells.append(" ")
                continue
            cell = (row, col)
            if cell in target_set:
                cells.append(f"<strong>{BOARD[row][col][1]}</strong>")
            elif cell in cell_piece:
                color = PIECE_COLORS[cell_piece[cell]]
                cells.append(
                    f"<span style='display:block;width:95%;height:95%;margin:auto;background:{color}'></span>"
                )
            else:
                cells.append("·")
        rows.append(cells)

    table = ["<table style='border-collapse:separate;border-spacing:4px;font-size:1.1rem;text-align:center'>"]
    for row in rows:
        cells = "".join(f"<td style='width:58px;height:48px;border:1px solid #d7c8b5'>{cell}</td>" for cell in row)
        table.append(f"<tr>{cells}</tr>")
    table.append("</table>")
    st.markdown("".join(table), unsafe_allow_html=True)


def render():
    st.header("Classic Calendar Board")
    st.caption("A 10-piece puzzle that leaves the selected day, month, and weekday visible.")
    selected_date = st.date_input("Choose a date", key="board_date")

    if not st.button("Solve the board", type="primary", key="solve_board"):
        return

    target_cells = find_target_cells(selected_date.day, selected_date.month - 1, weekday_index(selected_date))
    with st.spinner("Solving the board..."):
        placements = solve_puzzle(target_cells)

    if placements is None:
        st.error("No solution found for the selected date.")
        render_board(None, target_cells)
        return

    st.success("A valid board arrangement was found.")
    render_board(placements, target_cells)
