#imports packages
import os
import openai
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi

#Reads .env file and adds variables to environment so we can access them securely
load_dotenv()

#Accessing api key from .env file
openai.api_key = os.getenv("API_KEY")

#stand in, hardcoded youtube link (Will later update to be input by a user via a chrome extension)
youtube_video = "https://www.youtube.com/watch?v=eJkwnS5ZkAI"

#splits given url into only obtaining the video ID (the string after "v=")
video_id = youtube_video.split("=") [1]

#returns the transcript as a "JSON" object list
transcript = YouTubeTranscriptApi.get_transcript(video_id)

#need to iterate through json list and only grab the "text" objects
result = " "
for i in transcript:
    result += " " + i['text']

#split the transcript result into 2 halves in order to pass in smaller batches to summarize, add both halves to a list in order to use in a loop
result_one = result[:len(result)//2]
result_two = result[len(result)//2:]
result_list = [result_one, result_two]

#For loop in order to pass in the result list in batches, that way the prompt doesn's exceed the maximum token limit in this gpt engine (4058 tokens)
for i in range(len(result_list)):
    gpt_prompt = "The following paragraph is a transcript of a youtube video, read through and return a detailed summary of the transcript and key points: " + result_list[i]
    response = openai.Completion.create(engine="text-davinci-002", prompt = gpt_prompt, max_tokens = 2000, temperature = 0)
    print(response["choices"][0]["text"])
