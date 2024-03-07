import librosa

def get_sampling_rate_librosa(audio_file_path):
    # Load the audio file using librosa
    y, sr = librosa.load(audio_file_path, sr=None)
    
    # Print the sampling rate
    print(f"Sampling Rate: {sr} Hz")

# Provide the path to your audio file
audio_file_path = "Recording-_2_.wav"
get_sampling_rate_librosa(audio_file_path)
