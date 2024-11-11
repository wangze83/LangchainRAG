import os
import json
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import  StrOutputParser
from dotenv import load_dotenv

load_dotenv()

def load_config():
    config_path = './config/config.json'
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path, 'r') as f:
        config = json.load(f)

    return config

config = load_config()

# os.environ['http_proxy'] = config.get("proxy_http")
# os.environ['https_proxy'] = config.get("proxy_https")

openai_api_key = os.getenv("OPENAI_API_KEY")
model  = ChatOpenAI(api_key=openai_api_key, model='gpt-4-turbo')


msg = [
    SystemMessage(content='Please translate these words below into Italy'),
    HumanMessage(content='Hello, where are you going?')
]

result = model.invoke(msg)
print(result)

parser = StrOutputParser()
return_str = parser.Invoke(result)
print(return_str)


chain = model | parser
print(chain.invoke(msg))
