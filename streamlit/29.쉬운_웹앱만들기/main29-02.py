"""
달력에서 날짜를 선택하는 코드 만들기
"""

import streamlit as st
import datetime

# 달력으로 날짜를 입력 받는다.
d = st.date_input(
    "날짜를 선택하세요",
    datetime.date.today()
)

# 선택한 날짜를 출력
st.write('선택한 날짜:', d)
