import os
from google.cloud import speech, texttospeech

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

def text_to_speech(text, output_filename='output.mp3'):
  os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'text_to_speech_key.json'
  client = texttospeech.TextToSpeechClient()
  synthesis_input = texttospeech.SynthesisInput(text=text)
  voice = texttospeech.VoiceSelectionParams(
    language_code='en-in',
    ssml_gender=texttospeech.SsmlVoiceGender.MALE
  )
  audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3

  )
  response = client.synthesize_speech(
    input=synthesis_input,
    voice=voice,
    audio_config=audio_config
  )
  with open(output_filename, 'wb') as output:
    output.write(response.audio_content)
  return response