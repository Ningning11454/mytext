import streamlit as st

# -------------------- 0. 页面配置 --------------------
st.set_page_config(
    page_title="还珠格格 · 少女心专场",
    page_icon="💗",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -------------------- 1. 全局少女风 CSS --------------------
st.markdown("""
<style>
/* 1. 马卡龙渐变背景 + 云朵纹理 */
body, .main {
    background: linear-gradient(135deg, #fff0f8 0%, #ffeaf4 50%, #fff5f9 100%);
    background-image:
        radial-gradient(circle at 10% 20%, rgba(255,255,255,0.8) 0%, transparent 20%),
        radial-gradient(circle at 90% 80%, rgba(255,255,255,0.6) 0%, transparent 25%);
    font-family: "Quicksand", "PingFang SC", sans-serif;
}

/* 2. 闪光软萌标题 */
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

/* 3. 视频奶油卡片 */
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
/* 四角小桃心 */
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

/* 4. 糖果胶囊按钮 */
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

/* 5. 当前集跳动闪耀 */
div.stButton > button[kind="secondary"]:disabled {
    background: linear-gradient(45deg, #ff85a2, #ffb6c1);
    animation: bounce 1s ease infinite;
    cursor: not-allowed;
}
@keyframes bounce {
    0%,100%{transform:translateY(0)}
    50%{transform:translateY(-5px)}
}

/* 6. 樱花瓣漂浮彩蛋 */
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

# -------------------- 2. 数据 & session_state --------------------
video_arr = [
    {"url": "https://www.w3school.com.cn/example/html5/mov_bbb.mp4", "title": "第 1 集"},
    {"url": "https://www.w3schools.com/html/movie.mp4",               "title": "第 2 集"},
    {"url": "https://media.w3.org/2010/05/sintel/trailer.mp4",        "title": "第 3 集"},
]

if "ind" not in st.session_state:
    st.session_state.ind = 0

# -------------------- 3. 标题 --------------------
st.markdown('<div class="main-title">还珠格格 第一部</div>', unsafe_allow_html=True)

# -------------------- 4. 视频播放区（奶油卡片） --------------------
with st.container():
    st.markdown('<div class="video-card">', unsafe_allow_html=True)
    st.video(video_arr[st.session_state.ind]["url"], autoplay=True)
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------- 5. 选集按钮（原列布局不动） --------------------
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

# -------------------- 6. 随机樱花瓣彩蛋（纯 CSS） --------------------
# 随机生成 3~5 片花瓣，延迟飘落
import random
for _ in range(random.randint(3, 5)):
    left = random.randint(0, 100)
    delay = random.randint(0, 5)
    st.markdown(f'<div class="sakura" style="left:{left}%; animation-delay:{delay}s;">🌸</div>',
                unsafe_allow_html=True)
