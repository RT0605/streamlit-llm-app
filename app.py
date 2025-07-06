# 必要なパッケージのインポート
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import os

# .envから環境変数を読み込む
load_dotenv()

# 専門家の選択肢
EXPERTS = {
    "健康アドバイザー": "あなたは健康に関するアドバイザーです。安全なアドバイスを提供してください。",
    "キャリアコンサルタント": "あなたはキャリアに関する専門家です。前向きなキャリアアドバイスを提供してください。",
    "旅行プランナー": "あなたは旅行プランナーです。安全で楽しい旅行プランを提案してください。"
}

# LLMから回答を取得する関数
def get_llm_response(user_input: str, expert_type: str) -> str:
    system_prompt = EXPERTS.get(expert_type, "あなたは親切なアシスタントです。")
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_input)
    ]
    result = llm(messages)
    return result.content

# StreamlitアプリのUI
st.title("LLM専門家チャットアプリ")
st.write("""
このアプリは、選択した専門家になりきったAIがあなたの質問に回答します。\n
1. 専門家の種類を選択してください。\n2. 質問を入力して送信してください。\n3. AIからの回答が表示されます。
""")

expert_type = st.radio("専門家の種類を選択してください:", list(EXPERTS.keys()))
user_input = st.text_input("質問を入力してください:")

if st.button("送信") and user_input:
    with st.spinner("AIが回答中..."):
        response = get_llm_response(user_input, expert_type)
    st.markdown(f"**AI({expert_type})の回答:**")
    st.write(response)
