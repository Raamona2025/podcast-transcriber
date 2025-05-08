import whisper

model = whisper.load_model("base")
result = model.transcribe("podcast.mp3")

print(result["text"])
