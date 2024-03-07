import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

def plot_spectrum(y, sr, title="Spectrum"):
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(librosa.amplitude_to_db(librosa.stft(y), ref=np.max), y_axis='log', x_axis='time')
    plt.title(title)
    plt.colorbar(format='%+2.0f dB')
    plt.show()

def analyze_frequency_range(audio_file_path):
    # Load the audio file
    y, sr = librosa.load(audio_file_path)

    # Plot the spectrum
    plot_spectrum(y, sr, title="Original Spectrum")

    # Zoom in on the low-frequency range
    y_lowpass = librosa.effects.preemphasis(y)
    plot_spectrum(y_lowpass, sr, title="Low-pass Filtered Spectrum")

    # Analyze frequency range statistics
    mean_frequency = np.mean(librosa.feature.spectral_centroid(y))
    median_frequency = np.median(librosa.feature.spectral_centroid(y))

    print(f"Mean Frequency: {mean_frequency} Hz")
    print(f"Median Frequency: {median_frequency} Hz")

# Provide the path to your audio file
audio_file_path = "Recording-_2_.wav"
analyze_frequency_range(audio_file_path)
