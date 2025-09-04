from dotenv import load_dotenv

load_dotenv()
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

# Webアプリの概要・操作方法
st.title("専門家LLMチャットアプリ")
st.write("""
このアプリは、入力したテキストに対して、選択した専門家の視点でLLMが回答します。\n
1. 専門家の種類を選択してください。\n2. 質問や相談内容を入力し、送信ボタンを押してください。\n3. LLMからの回答が画面に表示されます。
""")

# 専門家の種類を定義
experts = {
	"医療の専門家": "あなたは優秀な医療の専門家です。専門的かつ分かりやすく回答してください。",
	"法律の専門家": "あなたは信頼できる法律の専門家です。法律的な観点から丁寧に回答してください。",
	"ITコンサルタント": "あなたは経験豊富なITコンサルタントです。技術的な観点から分かりやすく回答してください。"
}

# ラジオボタンで専門家選択
selected_expert = st.radio("専門家を選択してください", list(experts.keys()))

# 入力フォーム
user_input = st.text_area("質問や相談内容を入力してください")

# LLMに問い合わせる関数
def ask_llm(user_text: str, expert_key: str) -> str:
	system_message = experts[expert_key]
	messages = [
		SystemMessage(content=system_message),
		HumanMessage(content=user_text)
	]
	llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
	result = llm(messages)
	return result.content

# 送信ボタン
if st.button("送信"):
	if user_input.strip() == "":
		st.warning("テキストを入力してください。")
	else:
		with st.spinner("LLMが回答中..."):
			response = ask_llm(user_input, selected_expert)
		st.markdown("#### 回答")
		st.write(response)