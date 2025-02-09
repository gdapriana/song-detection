import streamlit as st
from resources.database import database__
from resources.mfcc import load_audio__, emphasis__, framing__, windowing__, fft__, melbank__, dct__
from resources.matching import matching__
import pandas as pd

if __name__ == '__main__':
  st.title("WHIPLASH")
  database = database__(csv_path="csv/train.csv", npy_path="npy/train/10")

  predict_tab, testing_tab, database_tab = st.tabs(["Predict", "Testing", "Database"])

  with predict_tab:
    st.header("SONG DETECTION")
    audio = st.file_uploader("Upload an audio file", type=["mp3"])

    # do mfcc
    if audio is not None:
      signal, sampling_rate = load_audio__(audio)
      signal = emphasis__(signal, coef=0.97)
      signal = framing__(signal, sampling_rate=sampling_rate, frame_size=1, frame_stride=0.5)
      signal = windowing__(signal, sampling_rate=sampling_rate, frame_size=1)
      signal = fft__(signal, NFFT=512)
      signal, _ = melbank__(signal, nfilt=40, sr=sampling_rate, NFFT=512)
      signal = dct__(signal, coef=13)

      min_distance, results, exec_time = matching__(database=database, new_data=signal)
      st.code(f"predicted {min_distance}")
      st.table(pd.DataFrame(results).drop(columns="path").sort_values(by="distance"))

  with testing_tab:
    st.header("Testing")

  with database_tab:
    st.header("Database")
    database = pd.DataFrame(database).drop(columns="features")
    st.table(database)