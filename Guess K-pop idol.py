import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# ====================================================
# 1. กำหนดค่าเริ่มต้นใน session_state
# ====================================================
for i in range(1, 7):
    if f"ans{i}_val" not in st.session_state:
        st.session_state[f"ans{i}_val"] = ""

if "hearts" not in st.session_state:
    st.session_state.hearts = 3

if "score" not in st.session_state:
    st.session_state.score = 0

if "wrong_count" not in st.session_state:
    st.session_state.wrong_count = 0

if "is_ended" not in st.session_state:
    st.session_state.is_ended = False

if "start" not in st.session_state:
    st.session_state.start = None


# ====================================================
# 2. ฟังก์ชันเริ่มเกมใหม่
# ====================================================
def reset_game():
    for i in range(1, 7):
        st.session_state[f"ans{i}_val"] = ""

    st.session_state.start = time.time()
    st.session_state.is_ended = False
    st.session_state.hearts = 3
    st.session_state.score = 0
    st.session_state.wrong_count = 0


# ====================================================
# 3. ฟังก์ชันตรวจคำตอบ
# ====================================================
def check_answers():
    answers = [
        ("LISA", st.session_state.ans1_val),
        ("JUNGKOOK", st.session_state.ans2_val),
        ("JEMIN", st.session_state.ans3_val),
        ("WINTER", st.session_state.ans4_val),
        ("MARTIN", st.session_state.ans5_val),
        ("MINJI", st.session_state.ans6_val),
    ]

    score = 0
    wrong = 0

    for correct, user_answer in answers:
        if user_answer.strip().upper() == correct:
            score += 1
        else:
            wrong += 1

    st.session_state.score = score
    st.session_state.wrong_count = wrong
    st.session_state.hearts = max(0, 3 - wrong)
    st.session_state.is_ended = True


# ====================================================
# 4. Dialog แสดงผล
# ====================================================
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog():

    st.balloons()

    score = st.session_state.score
    wrong = st.session_state.wrong_count

    st.subheader("📋 ผลการเล่น")

    # แสดงคะแนน
    st.info(f"🏆 คะแนนที่ได้: {score}/6")

    # แสดงหัวใจ
    hearts = "❤️" * st.session_state.hearts
    empty_hearts = "🖤" * (3 - st.session_state.hearts)

    st.write(f"❤️ หัวใจ: {hearts}{empty_hearts}")

    # แสดงผลแต่ละข้อ
    correct_answers = [
        "LISA",
        "JUNGKOOK",
        "JEMIN",
        "WINTER",
        "MARTIN",
        "MINJI",
    ]

    for i in range(1, 7):
        user_answer = st.session_state[f"ans{i}_val"].strip().upper()
        correct_answer = correct_answers[i - 1]

        if user_answer == correct_answer:
            st.success(
                f"✅ ข้อ {i}: ถูกต้อง — {correct_answer}"
            )
        else:
            st.error(
                f"❌ ข้อ {i}: ตอบ {user_answer or '(ไม่ได้ตอบ)'} "
                f"→ เฉลย: {correct_answer}"
            )

    st.divider()

    # =================================================
    # กำหนดยศ
    # =================================================

    # ถ้าถูกครบ 6 ข้อ และทำภายใน 30 วินาที
    if score == 6:
        elapsed_time = time.time() - st.session_state.start

        if elapsed_time <= 30:
            st.success("👑 ติ่งระดับตำนาน")
            st.write("🎉 ตอบถูกครบ 6 ข้อภายใน 30 วินาที!")
        else:
            st.success("🔥 ติ่งระดับเทพ")
            st.write("ตอบถูกครบทุกข้อ แต่ใช้เวลาเกิน 30 วินาที")

    elif score >= 1:
        st.warning("⭐ ติ่งธรรมดา")

    else:
        st.error("🫠 ไส้ติ่ง")

    # Game Over เมื่อหัวใจหมด
    if st.session_state.hearts == 0:
        st.error("💀 GAME OVER — หัวใจหมดแล้ว!")


# ====================================================
# 5. ปุ่มเริ่มเกม
# ====================================================
st.button(
    "🎮 เริ่มเล่นเกม",
    on_click=reset_game
)


# ====================================================
# 6. แสดงเวลาและหัวใจ
# ====================================================
if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):

    time_left = int(
        30 - (time.time() - st.session_state.start)
    )

    # แสดงหัวใจ
    st.write(
        f"❤️ หัวใจ: "
        f"{'❤️' * st.session_state.hearts}"
        f"{'🖤' * (3 - st.session_state.hearts)}"
    )

    # แสดงเวลา
    if time_left > 0:
        st.error(
            f"⏳ เหลือเวลา: {time_left} วินาที"
        )
    else:
        st.session_state.is_ended = True
        st.rerun()


st.divider()


# ====================================================
# 7. ช่องเติมคำศัพท์
# ====================================================
ans1 = st.text_input(
    "ข้อ 1: L _ S_",
    value=st.session_state.ans1_val
)

ans2 = st.text_input(
    "ข้อ 2: J _ _GKO_K",
    value=st.session_state.ans2_val
)

ans3 = st.text_input(
    "ข้อ 3: JE_I_N",
    value=st.session_state.ans3_val
)

ans4 = st.text_input(
    "ข้อ 4: W__TE_",
    value=st.session_state.ans4_val
)

ans5 = st.text_input(
    "ข้อ 5: _AR_IN",
    value=st.session_state.ans5_val
)

ans6 = st.text_input(
    "ข้อ 6: M_N_I",
    value=st.session_state.ans6_val
)


# ====================================================
# 8. เก็บคำตอบลง session_state
# ====================================================
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5
st.session_state.ans6_val = ans6


# ====================================================
# 9. ปุ่มส่งคำตอบ
# ====================================================
if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):

    if st.button("📥 ส่งคำตอบ"):

        check_answers()

        # ถ้าตอบผิดครบ 3 ข้อ → Game Over
        if st.session_state.hearts <= 0:
            st.session_state.is_ended = True

        st.rerun()

    # อัปเดตเวลาอัตโนมัติ
    time.sleep(1)
    st.rerun()


# ====================================================
# 10. แสดง Dialog เมื่อจบเกม
# ====================================================
if st.session_state.is_ended:
    show_result_dialog()


st.divider()
