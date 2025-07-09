# 인공지는 PDF Q&A 챗봇 만들기 1
# pip install gradio
import gradio as gr
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader

# 환경변수 로드
load_dotenv()

# llm 설정
llm = ChatOpenAI(model="gpt-4o-mini")

# 텍스트 분리
text_splitter = CharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

# 임배딩 모델 설정
hf_embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-m3")

# 프롬포트 템플릿
message = """
당신은 사용자의 질문에 답변을 하는 친절한 AI 어시스턴트입니다.
당신의 입무는 주어진 문맥을 토대로 사용자 질문에 답하는 것입니다.
만약, 문맥에서 답변을 위한 정보를 찾을 수 없다면 '주어진 정보에서 질문에 대한 정보를 찾을 수 없습니다' 라고 답하세요.
정보를 찾을 수 있다면 한글로 답변해 주세요.

## 주어진 문맥:
{context}

## 사용자 질문:
{input}
"""

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("human", message)
    ]
)

# 출력 파서
parser = StrOutputParser()

# 전역변수
db = None
retriever = None
rag_chain = None

def load_pdf(file):
    pass

def answer_question(question):
    pass

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

    upload_button.click(load_pdf, inputs=file_input, outputs=status_output)
    submit_button.click(answer_question, inputs=question_input, outputs=answer_output)

demo.launch()