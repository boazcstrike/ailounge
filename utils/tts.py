from transformers import pipeline
from datasets import load_dataset
import soundfile as sf
import torch
import os

synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts")

embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)
directory = "dump/"
file_list = []
i = 0
counter = 0

with open("dump/response_092724180949.txt", "r") as file:
    content = file.read()
speech = synthesiser(
    content[:600], forward_params={"speaker_embeddings": speaker_embedding}
)
sf.write(f"speech_{counter}.wav", speech["audio"], samplerate=speech["sampling_rate"])

# while True:
# for filename in os.listdir(directory):
#   if os.path.isfile(os.path.join(directory, filename)):
#     file_list.append(os.path.join(directory, filename))
# for file_i in file_list:
#   paired_chats = read_file(f"{file_i}")
#   speech = synthesiser(paired_chats, forward_params={"speaker_embeddings": speaker_embedding})
#   print(speech)
#   sf.write(f"speech_{counter}.wav", speech["audio"], samplerate=speech["sampling_rate"])
