import os
from dotenv import load_dotenv
from openai import OpenAI

# 加载当前目录或父目录下的 .env 文件
load_dotenv()

# 初始化客户端，从环境变量中读取 Key
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"), 
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 读取本地文本数据
with open("data/raw/paper1.txt", encoding="utf-8") as f:
    paper = f.read()

# 设置提问
question = "这篇论文使用了什么具体型号的显卡进行训练？"

# 拼接 Prompt
messages = [
    {"role": "system", "content": "只根据下面提供的论文内容回答问题，不要使用你自己的知识。如果内容里没有答案，直接回答不知道。"},
    {"role": "user", "content": f"论文内容：\n{paper}\n\n问题：{question}"},
]

# 调用大模型生成回答
resp = client.chat.completions.create(
    model="qwen-plus",
    messages=messages,
)

# 打印输出结果
print(resp.choices[0].message.content)