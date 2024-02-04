from pydub import AudioSegment
import numpy as np


your_byte_array = b'\x00\x01\x02\x03\x04\x05'
def convert_audio_segment(your_byte_array):
    audio_array = np.frombuffer(your_byte_array, dtype=np.int16)
# Create an AudioSegment from the numpy array
    audio_segment = AudioSegment(
        audio_array.tobytes(),
        frame_rate=44100,  # Adjust frame rate based on your audio specifications
        sample_width=audio_array.dtype.itemsize,
        channels=1  # Adjust the number of channels based on your audio specifications
    )
    # Export the audio segment to a file (replace 'output_file.wav' with your desired output file name)
    output_file = "output_file.wav"
    audio_segment.export(output_file, format="wav")