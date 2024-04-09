from fastapi import FastAPI, Request
from emailData import EmailData
from transformers import pipeline
import google.generativeai as genai

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

tempData = []

@app.get("/getemaildetails")
async def get_data(request: Request):
    data = await request.json()
    return {"Data": data}

#nlp = pipeline(task='sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')

text = 'Hi Nikunj, Following up on this issue. Please let us know of the status. Sincerely, Nikunj'
#print(f'{nlp(text)}')

genai.configure(api_key="AIzaSyBwKOUT0DaLHUaqdtWyCNRqU8zgeBwGiT4")

defaults = {
 'model': 'models/text-bison-001',
 'temperature': 0.5,
 'candidate_count': 1,
 'top_k': 40,
 'top_p': 0.95,
 'max_output_tokens': 1024,
}
prompt =f"""What is the sentiment of the following sentence, which is delimited with triple backticks? Just give the sentiment in one word if it is positive, very positive, negative, very negative or neutral
Review text: '''{text}'''"""
response = genai.generate_text(**defaults, prompt=prompt)
tempData.append(response.result)
output = tempData[0]
print(output)

@app.get("/SentimentAnalysis")
async def get_analysis():
    return {"Sentiment": output}
