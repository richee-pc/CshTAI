import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# Streamlit 페이지의 기본 설정을 구성합니다.
st.set_page_config(
    page_title="AI와 함께 스마트하게 일하기",
    page_icon="✨",
    layout="wide"
)

# 현재 파일의 위치를 기준으로 htmls/index.html 파일의 경로를 설정합니다.
# Path(__file__)는 현재 실행 중인 .py 파일의 경로를 나타냅니다.
# .parent는 해당 파일이 속한 디렉토리를 가리킵니다.
# / 'htmls' / 'index.html'는 하위 폴더와 파일을 순차적으로 연결합니다.
html_file_path = Path(__file__).parent / 'htmls' / 'index.html'

# HTML 파일이 존재하는지 확인합니다.
if html_file_path.exists():
    # 파일을 열고 내용을 읽어옵니다. 'rb'는 바이너리 읽기 모드입니다.
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Streamlit의 components.html 기능을 사용하여 HTML 콘텐츠를 렌더링합니다.
    # height를 넉넉하게 설정하여 스크롤 없이 전체 페이지가 잘 보이도록 합니다.
    # scrolling=True를 통해 내용이 길어질 경우에도 스크롤이 가능하게 합니다.
    components.html(html_content, height=2500, scrolling=True)
else:
    # 파일이 지정된 경로에 없을 경우, 에러 메시지를 표시합니다.
    st.error("오류: htmls/index.html 파일을 찾을 수 없습니다. 파일 경로를 확인해주세요.")
