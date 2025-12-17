import streamlit as st


st.set_page_config(
    page_title="还珠格格",
    page_icon="💗",
    layout="centered",
    initial_sidebar_state="collapsed"
)


st.markdown("""
<style>

body, .main {
    background: linear-gradient(135deg, #fff0f8 0%, #ffeaf4 50%, #fff5f9 100%);
    background-image:
        radial-gradient(circle at 10% 20%, rgba(255,255,255,0.8) 0%, transparent 20%),
        radial-gradient(circle at 90% 80%, rgba(255,255,255,0.6) 0%, transparent 25%);
    font-family: "Quicksand", "PingFang SC", sans-serif;
}


.main-title {
    text-align: center;
    font-size: 2.6rem;
    font-weight: 700;
    letter-spacing: 3px;
    margin: 20px 0 10px 0;
    background: linear-gradient(45deg, #ff85a2, #ffc2d1, #ff85a2);
    background-size: 200% 200%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shine 3s ease infinite;
}
@keyframes shine {
    0%{background-position:0% 50%}
    50%{background-position:100% 50%}
    100%{background-position:0% 50%}
}

.video-card {
    display: flex;
    justify-content: center;
    margin: 0 auto 30px auto;
    position: relative;
    width: fit-content;
    border-radius: 18px;
    padding: 8px;
    background: white;
    box-shadow: 0 0 0 3px #ffe3f1, 0 8px 30px rgba(255, 182, 193, 0.35);
}
.stVideo {
    border-radius: 12px;
    overflow: hidden;
}

.video-card::before,
.video-card::after {
    content: "💗";
    position: absolute;
    font-size: 18px;
    animation: pulse 1.5s ease-in-out infinite;
}
.video-card::before { top: -10px; left: -10px; }
.video-card::after  { bottom: -10px; right: -10px; }
@keyframes pulse {
    0%,100%{transform:scale(1)}
    50%{transform:scale(1.2)}
}


div.stButton > button {
    height: 42px;
    border-radius: 21px;
    font-size: 15px;
    font-weight: 600;
    border: none;
    background: linear-gradient(45deg, #ffa6c9, #ffc2d1);
    color: #fff;
    box-shadow: 0 4px 15px rgba(255, 166, 201, 0.4);
    transition: all .3s ease;
}
div.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 20px rgba(255, 166, 201, 0.6);
}


div.stButton > button[kind="secondary"]:disabled {
    background: linear-gradient(45deg, #ff85a2, #ffb6c1);
    animation: bounce 1s ease infinite;
    cursor: not-allowed;
}
@keyframes bounce {
    0%,100%{transform:translateY(0)}
    50%{transform:translateY(-5px)}
}


.sakura {
    position: fixed;
    top: -20px;
    font-size: 20px;
    color: #ffb6c1;
    animation: fall 10s linear infinite;
    z-index: 9999;
}
@keyframes fall {
    to { transform: translateY(110vh) rotate(360deg); }
}
</style>
""", unsafe_allow_html=True)

video_arr = [
    {"url": "https://www.w3school.com.cn/example/html5/mov_bbb.mp4", "title": "第 1 集"},
    {"url": "https://www.w3schools.com/html/movie.mp4",               "title": "第 2 集"},
    {"url": "https://media.w3.org/2010/05/sintel/trailer.mp4",        "title": "第 3 集"},
]

if "ind" not in st.session_state:
    st.session_state.ind = 0


st.markdown('<div class="main-title">还珠格格 第一部</div>', unsafe_allow_html=True)


with st.container():
    st.markdown('<div class="video-card">', unsafe_allow_html=True)
    st.video(video_arr[st.session_state.ind]["url"], autoplay=True)
    st.markdown('</div>', unsafe_allow_html=True)


def play(i):
    st.session_state.ind = int(i)

cols = st.columns(len(video_arr))
for idx, col in enumerate(cols):
    with col:
        disabled = (idx == st.session_state.ind)
        st.button(
            f"第 {idx + 1} 集",
            use_container_width=True,
            on_click=None if disabled else play,
            args=(idx,) if not disabled else (),
            disabled=disabled
        )

import random
for _ in range(random.randint(3, 5)):
    left = random.randint(0, 100)
    delay = random.randint(0, 5)
    st.markdown(f'<div class="sakura" style="left:{left}%; animation-delay:{delay}s;">🌸</div>',
                unsafe_allow_html=True)
