# 인공지는 PDF Q&A 챗봇 만들기 1
# pip install gradio
import gradio as gr

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 📄 인공지는 PDF Q&A 챗봇
    **PDF 파일을 업로드하고 질문을 입력하면 AI가 답변을 제공합니다.**
""")
    with gr.Row():
        with gr.Column(scale=1):
            file_input = gr.File(label="PDF 파일 업로드")
            upload_button = gr.Button("📤 업로드 및 처리")

        with gr.Column(scale=2):
            status_output = gr.Textbox(label="📢 상태 메시지")
            question_input = gr.Textbox(label="💬 질문 입력", placeholder="궁금한 내용을 적어주세요.")
            submit_button = gr.Button("🤖 답변 받기")
            answer_output = gr.Textbox(label="📝 AI 답변")

demo.launch()