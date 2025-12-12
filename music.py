import streamlit as st

# 页面配置：音乐播放器主题
st.set_page_config(page_title="简易音乐播放器", page_icon="🎵")
st.title("简易音乐播放器")
st.caption("使用Streamlit制作的音乐播放器，支持切换与基础信息展示")

# 1. 初始化状态：存储当前音乐索引
if 'music_ind' not in st.session_state:
    st.session_state['music_ind'] = 0

# 2. 音乐数据：包含封面、歌曲名、歌手、时长、音乐链接（注：需用可公开访问的音频URL）
music_list = [
   {
        "cover": "http://p2.music.126.net/wRDGhwhhzJuUkWMrjrPwKw==/109951172137146717.jpg?param=130y130",
        "title": "Blue Valentine",
        "singer": "NMIXX",
        "duration": "03：06",
        "audio_url": "https://music.163.com/song/media/outer/url?id=8499257255.mp3"  # 替换为实际可访问的音频URL
    },
    {
        "cover": "http://p1.music.126.net/srse1pR1hPtnBIrGcqHvNA==/109951169939972270.jpg?param=130y130",
        "title": "ONCE AGAIN",
        "singer": "WINTER / NINGNING",
        "duration": "02：49",
        "audio_url": "https://music.163.com/song/media/outer/url?id=1949928569.mp3"  # 替换为实际可访问的音频URL
    },
    
    {
        "cover": "http://p2.music.126.net/FTzl-oT9JIKFvQzkDibibw==/109951169721143692.jpg?param=130y130",
        "title": "BAHAMA",
        "singer": "aespa",
        "duration": "03:10",
        "audio_url": "https://music.163.com/song/media/outer/url?id=2160419150.mp3"  # 替换为实际可访问的音频URL
    }
]

# 3. 获取当前播放的音乐信息
current_music = music_list[st.session_state['music_ind']]

# 4. 布局：封面+歌曲信息（左右排列）
col_cover, col_info = st.columns([1, 2])
with col_cover:
    st.image(current_music["cover"], caption="专辑封面", width=150)
with col_info:
    st.subheader(current_music["title"])
    st.write(f"歌手: {current_music['singer']}")
    st.write(f"时长: {current_music['duration']}")

# 5. 音乐播放组件（Streamlit原生audio组件）
st.audio(current_music["audio_url"], format="audio/mp3")

# 6. 切换函数：上一首/下一首（循环切换）
def prev_music():
    st.session_state['music_ind'] = (st.session_state['music_ind'] - 1) % len(music_list)

def next_music():
    st.session_state['music_ind'] = (st.session_state['music_ind'] + 1) % len(music_list)

# 7. 切换按钮
col_prev, col_next = st.columns(2)
with col_prev:
    st.button("◀️ 上一首", on_click=prev_music)
with col_next:
    st.button("下一首 ▶️", on_click=next_music)
