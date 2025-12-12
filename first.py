import streamlit as st
import pandas as pd

# 1. 标题/Header
st.title("学生 小八 数字档案")
st.header("基础信息", divider="rainbow")

# 2. 基础信息（text/markdown）
st.markdown("""
- 学生ID: N03-2023-001
- 注册时间: 2023-09-01 | 精神状态: ✅ 正常
- 当前教室: 实训楼108  | 安全等级：绝密
""")


# 3. 技能矩阵（metric组件）
st.header("技能矩阵", divider="rainbow")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Python", value="95%", delta="+3%")
with col2:
    st.metric(label="SQL", value="87%", delta="-2%")
with col3:
    st.metric(label="Vue", value="68%", delta="-10%")

#4.课程进度
st.header("📚 Streamlit课程进度", divider="rainbow")
with st.container():
    st.markdown('<div class="streamlit-progress">', unsafe_allow_html=True)
    
    # 1. 整体进度条
    total_progress = 82  # 整体进度82%
    st.markdown(f"""
        <div>
            <span>课程整体完成度：{total_progress}%</span>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {total_progress}%"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    


# 5. 任务日志（table组件）
st.header("任务日志", divider="rainbow")
task_data = {
    "日期": ["2023-10-01", "2023-10-12", "2023-10-20"],  # 补1个日期
    "任务": ["学生数字档案", "模型管理系统", "数据可视化展示"],
    "状态": ["✅ 已完成", "🔄 进行中", "❌ 未完成"],
    "难度": ["★★☆☆☆", "★★★☆☆", "★★★★☆"]
}
task_df = pd.DataFrame(task_data)
st.table(task_df)


# 6. 最新代码成果（code组件）
st.header("最新代码成果", divider="rainbow")
code = """
def detect_villain(identity):
    if identity == "Z":
        detect_villain.identity = "T-ACCESS GRANTED"
        return "ALERT"
    stevil_db.update()
"""
st.code(code, language="python")


# 7. 系统日志（markdown）
st.markdown("""
---
> **SYSTEM MESSAGE**: 下一个任务已解锁
> **SYSTEM**: 模型管理系统
> **CONTINUE**: 2025-03-01 12:42:48
> 系统状态: 在线 | 连接状态: 已加密
""")
