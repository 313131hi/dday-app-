import datetime
import streamlit as st

# 웹 앱 제목
st.title("📅 실생활 문제 해결: D-Day 계산기")
st.write("시험, 과제, 이벤트 등 중요한 날까지 남은 기간을 계산해 줍니다.")

# 날짜 입력받기
target_date = st.date_input("목표 날짜를 선택하세요")
today = datetime.date.today()

# 계산 버튼 클릭 시 실행
if st.button("남은 날짜 계산하기"):
    days_left = (target_date - today).days

    if days_left > 0:
        st.info(f"🎉 목표일까지 **{days_left}일** 남았습니다!")
    elif days_left == 0:
        st.balloons()
        st.success("✨ 오늘이 바로 D-Day입니다!")
    else:
        st.warning(f"⚠️ 목표일로부터 **{abs(days_left)}일** 지났습니다.")
