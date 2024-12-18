import os
# from groq import Groq
import configparser
import base64
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
import configparser
from groq import Groq

# Read configuration file for API key
config = configparser.ConfigParser()
config.read('config.ini')

# Ensure that you have your API key set in environment variables or replace with actual key
groq_ai_key = config.get('GROQ', 'groq_api_key')
os.environ['GROQ_API_KEY'] = groq_ai_key

groq_model = "llama-3.1-70b-versatile"  # Specify your Groq model name

# Define your prompt
prompt = """
Are you alive?
"""

# Initialize the Groq LLM model
g_llm = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Prepare the messages (system message and user prompt)
messages = [
    {"role": "system", "content": "You are an expert in Software Development."},
    {"role": "user", "content": prompt}  # Replace this with your dynamic user input
]

# Send the messages to the Groq model via Langchain's method
response = g_llm.chat.completions.create(
    model=groq_model,
    messages=messages
)

# Correct way to extract the response content
response_content = response.choices[0].message.content  # Access using the attribute, not dictionary

print(response_content)
