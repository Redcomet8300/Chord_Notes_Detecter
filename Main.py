import os
import json
from music21 import *

with open('setting.json', 'r') as config_file:
    config = json.load(config_file)

folder_path = "songs"

for filename in os.listdir(folder_path):
    if filename.endswith(".mid"):
        midi_file = converter.parse(os.path.join(folder_path, filename))

        notes = []
        chords = []

        for element in midi_file.flat.notes:
            if isinstance(element, note.Note):
                notes.append(element.nameWithOctave)
            elif isinstance(element, chord.Chord):
                chords.append(element.commonName)

        print("File:", filename)
        print("Detected Notes:", notes)
        print("Detected Chords:", chords)
        print("\n")

        output_filename = os.path.splitext(filename)[0] + "_output.txt"
        output_path = os.path.join(folder_path, output_filename)
        with open(output_path, "w") as output_file:
            output_file.write("Notes:\n")
            output_file.write("\n".join(notes))
            output_file.write("\n\nChords:\n")
            output_file.write("\n".join(chords))
