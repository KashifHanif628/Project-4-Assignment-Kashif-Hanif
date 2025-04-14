import streamlit as st
import time

st.title("⏳ Countdown Timer")

# Session state initialize karo
if 'running' not in st.session_state:
    st.session_state.running = False

# Sirf jab timer nahi chal raha, user input lein
if not st.session_state.running:
    seconds = st.number_input("Seconds daalein:", min_value=1, step=1, key="input_seconds")

# Button dabane pe timer shuru karo
if st.button("Shuru karein") and not st.session_state.running:
    st.session_state.running = True
    st.session_state.start_time = time.time()
    st.session_state.duration = st.session_state.input_seconds

# Timer logic
if st.session_state.running:
    guzra_hua = int(time.time() - st.session_state.start_time)
    baqi = int(st.session_state.duration - guzra_hua)

    if baqi > 0:
        st.info(f"⏳ {baqi} second are left")
        time.sleep(1)
        st.rerun()  # ✅ yahan pe pehle st.experimental_rerun() tha, ab ye hai
    else:
        st.session_state.running = False
        st.success("⏰ Time is up")
