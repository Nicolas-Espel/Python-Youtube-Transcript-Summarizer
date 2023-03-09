#imports api modules
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi

#stand in, hardcoded youtube link (Will later update to be input by a user via a chrome extension)
youtube_video = "https://www.youtube.com/watch?v=A4OmtyaBHFE"

#splits given url into only obtaining the video ID (the string after "v=")
video_id = youtube_video.split("=") [1]

#returns the transcript as a "JSON" object list
transcript = YouTubeTranscriptApi.get_transcript(video_id)

#need to iterate through json list and only grab the "text" objects
result = " "
for i in transcript:
    result += " " + i['text']

#process string of text in batches in order to summarize quicker
summarized_text = pipeline('summarization')

summarized_text(result)

