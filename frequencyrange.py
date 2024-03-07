import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

# Load the audio file
audio_file = 'Recording-_2_.wav'
data, samplerate = sf.read(audio_file)

# Compute the Fourier Transform of the audio data
fft_data = np.fft.fft(data)

# Compute the frequencies corresponding to the FFT bins
freqs = np.fft.fftfreq(len(fft_data), 1/samplerate)

# Plot the magnitude spectrum
plt.figure(figsize=(10, 4))
plt.plot(freqs[:len(freqs)//2], np.abs(fft_data[:len(freqs)//2]))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Magnitude Spectrum of Audio File')
plt.show()