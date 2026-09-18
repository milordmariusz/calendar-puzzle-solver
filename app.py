import streamlit as st

from board_view import render as render_board
from digit_view import render as render_digits


st.set_page_config(page_title="Calendar Puzzle Solver", layout="wide")
st.title("Calendar Puzzle Solver")
st.write("Two related calendar puzzles in one application.")

digits_tab, board_tab = st.tabs(["Digit Puzzle", "Calendar Board"])
with digits_tab:
    render_digits()
with board_tab:
    render_board()
