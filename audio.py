import librosa
import numpy as np
import pandas as pd
import os

def extract_features(file_name):
    y, sr = librosa.load(file_name)
    mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13).T, axis=0)
    chroma = np.mean(librosa.feature.chroma_stft(y=y, sr=sr).T, axis=0)
    zcr = np.mean(librosa.feature.zero_crossing_rate(y).T, axis=0)
    spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr).T, axis=0)
    return mfcc, chroma, zcr, spectral_centroid

features_list = []
selected_audio_files = [
    r'archive\Emotions\Angry\YAF_young_angry.wav',
    r'archive\Emotions\Angry\\YAF_witch_angry.wav',
    r'archive/Emotions/Disgusted/03-01-07-01-01-02-21.wav',
    r'archive\Emotions\Disgusted\03-01-07-01-02-02-16.wav',
    r'archive\Emotions\Fearful\03-01-06-01-02-01-02.wav',
    r'archive\Emotions\Fearful\1084_TSI_FEA_XX.wav',
    r'archive\Emotions\Happy\1003_IEO_HAP_HI.wav',
    r'archive\Emotions\Happy\1013_ITS_HAP_XX.wav',
    r'archive\Emotions\Neutral\YAF_wag_neutral.wav',
    r'archive\Emotions\Neutral\YAF_base_neutral.wav',
    r'archive\Emotions\Sad\1002_IWW_SAD_XX.wav',
    r'archive\Emotions\Sad\1011_ITH_SAD_XX.wav',
    r'archive\Emotions\Suprised\YAF_goose_ps.wav',
    r'archive\Emotions\Suprised\YAF_yearn_ps.wav'
]

for audio_file in selected_audio_files:
    # file_name = os.path.basename(audio_file)
    emotion = os.path.basename(os.path.dirname(audio_file))  # Extract emotion from the directory name
    mfcc, chroma, zcr, spectral_centroid = extract_features(audio_file)
    features_list.append([emotion] + list(mfcc) + list(chroma) + [zcr] + [spectral_centroid])

columns = ['Emotion'] + [f'MFCC_{i}' for i in range(13)] + [f'Chroma_{i}' for i in range(12)] + ['Zero-Crossing Rate', 'Spectral Centroid']

df = pd.DataFrame(features_list, columns=columns)
df.to_csv('audio.csv', index=False)
