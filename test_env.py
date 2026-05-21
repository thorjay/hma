import os
from dotenv import load_dotenv
try:
    from openai import OpenAI
except Exception:
    # Fallback import name for older/newer packages may differ; we'll import and handle at runtime
    OpenAI = None

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key or "your-actual-api-key" in api_key:
    print("❌ 错误：请先在 .env 文件中配置真实的 OPENAI_API_KEY！")
    exit(1)

print("✅ 环境检查：.env 配置文件读取正常。")

try:
    if OpenAI is None:
        # try dynamic import
        import importlib
        openai_mod = importlib.import_module('openai')
        client = openai_mod.OpenAI()
    else:
        client = OpenAI()

    print("⏳ 正在尝试连接大模型后端...")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": "Hello, Hermes!"}],
        max_tokens=10
    )
    print("✅ 网络与鉴权检查：大模型响应成功！")
    # Try to extract content safely
    try:
        content = response.choices[0].message.content.strip()
    except Exception:
        content = str(response)
    print(f"🤖 回应内容: {content}")
except Exception as e:
    print(f"❌ 连接模型失败，请检查网络或 API Key。错误信息:\n{e}")
