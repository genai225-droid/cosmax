import pathlib

import streamlit as st
import streamlit.components.v1 as components

APP_DIR = pathlib.Path(__file__).parent
ICON_PATH = APP_DIR / "main_ganadi_01.png"

st.set_page_config(
    page_title="가나디 패키징 업체 비교",
    page_icon=str(ICON_PATH),
    layout="wide",
)


def load_html(filename: str) -> str:
    """HTML 파일을 읽어오고, 원본에 있던 페이지 간 <a href> 이동 링크는
    Streamlit(iframe) 환경에서 오작동하지 않도록 무력화한다.
    실제 페이지 전환은 왼쪽 사이드바 메뉴에서만 이뤄진다."""
    html = (APP_DIR / filename).read_text(encoding="utf-8")

    disable_note = "onclick=\"alert('왼쪽 사이드바 메뉴에서 페이지를 전환해 주세요 🐾');return false;\""

    html = html.replace(
        '<a class="btn-cta" href="entry.html">',
        f'<a class="btn-cta" href="javascript:void(0)" {disable_note}>',
    )
    html = html.replace(
        '<a class="btn-skip" href="index.html">',
        f'<a class="btn-skip" href="javascript:void(0)" {disable_note}>',
    )
    # 결과 화면 안내 문구에 있는 대시보드 이동 링크도 동일하게 처리
    html = html.replace(
        '<a href="index.html">대시보드</a>',
        f'<a href="javascript:void(0)" {disable_note}>대시보드</a>',
    )

    return html


st.sidebar.image(str(ICON_PATH), use_container_width=True)
st.sidebar.title("가나디 🐾")
page = st.sidebar.radio(
    "메뉴",
    ["📊 업체 비교 대시보드", "💛 궁합으로 추천받기"],
    label_visibility="collapsed",
)

st.sidebar.markdown("---")
st.sidebar.caption(
    "데이터는 브라우저(localStorage)에 저장돼요.\n"
    "같은 브라우저로 다시 접속하면 데이터가 유지되지만, "
    "다른 기기·브라우저와는 공유되지 않아요."
)

if page == "📊 업체 비교 대시보드":
    html_content = load_html("index.html")
    height = 2200
else:
    html_content = load_html("entry.html")
    height = 1800

components.html(html_content, height=height, scrolling=True)
