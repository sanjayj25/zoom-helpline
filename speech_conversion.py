import os
from google.cloud import speech

def speech_to_text(filename):
  os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'speech_to_text_key.json'

  with open(filename, 'rb') as f:
    byte_data = f.read()
  audio = speech.RecognitionAudio(content=byte_data)
  config = speech.RecognitionConfig(
    sample_rate_hertz=48000,
    enable_automatic_punctuation=True,
    language_code='en-US'
  )
  speech_client = speech.SpeechClient()
  response = speech_client.recognize(config=config, audio=audio)
  transcription = ''
  for result in response.results:
    transcription += result.alternatives[0].transcript
  return transcription