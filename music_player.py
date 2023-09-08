import streamlit as st
import os
import random
from pydub import AudioSegment

def load_audio_files(language):
    audio_files = {}
    for file in os.listdir("music_folder"):
        if file.endswith(".wav"):
            if language == "Chinese" and file.startswith("cn_"):
                article_id = file.split(".")[0]
                audio_files[article_id] = file
            elif language == "English" and file.startswith("en_"):
                article_id = file.split(".")[0]
                audio_files[article_id] = file
    return audio_files

def play_audio(file):
    audio_bytes = open("music_folder/" + file, "rb").read()
    st.audio(audio_bytes, format="audio/wav")

def create_playlist(language, playlist_size, cn_audio_files, en_audio_files):
    if language == "Chinese":
        audio_files = list(cn_audio_files.values())
    elif language == "English":
        audio_files = list(en_audio_files.values())

    random.shuffle(audio_files)
    playlist_files = audio_files[:playlist_size]

    playlist = AudioSegment.empty()
    for file in playlist_files:
        audio = AudioSegment.from_wav("music_folder/" + file)
        playlist += audio

    output_path = "music_folder/playlist.wav"
    playlist.export(output_path, format="wav")

    return output_path

def main():
    st.title("Music Player")

    # Retrieve query parameters
    query_params = st.experimental_get_query_params()
    article_id = query_params.get("article_id", [None])[0]

    # Language selection
    language = st.selectbox("Language", ("Chinese", "English"))

    # Load audio files based on language selection
    audio_files = load_audio_files(language)

    # Loop/Shuffle mode selection
    mode = st.radio("Playback Mode", ("Loop", "Shuffle"), key="mode")

    # Playlist size selection
    playlist_size = st.slider("Playlist Size", min_value=5, max_value=20, value=10)

    # Create Playlist button
    if st.button("Create Playlist"):
        cn_audio_files = {k: v for k, v in audio_files.items() if v.startswith("cn_")}
        en_audio_files = {k: v for k, v in audio_files.items() if v.startswith("en_")}
        playlist_path = create_playlist(language, playlist_size, cn_audio_files, en_audio_files)
        st.audio(open(playlist_path, "rb").read(), format="audio/wav")

    # Toggle between Chinese and English audio files
    cn_audio_files = {k: v for k, v in audio_files.items() if v.startswith("cn_")}
    en_audio_files = {k: v for k, v in audio_files.items() if v.startswith("en_")}

    # Find matching audio file based on query parameter "article_id"
    current_file = None
    if article_id:
        if language == "Chinese" and article_id in cn_audio_files:
            current_file = cn_audio_files[article_id]
        elif language == "English" and article_id in en_audio_files:
            current_file = en_audio_files[article_id]

    # Shuffle audio files if shuffle mode is selected
    if mode == "Shuffle":
        if language == "Chinese":
            audio_files = list(cn_audio_files.values())
            random.shuffle(audio_files)
        elif language == "English":
            audio_files = list(en_audio_files.values())
            random.shuffle(audio_files)
    else:
        if language == "Chinese":
            audio_files = list(cn_audio_files.values())
        elif language == "English":
            audio_files = list(en_audio_files.values())

    # Display audio files
    if len(audio_files) > 0:
        for i, file in enumerate(audio_files):
            if st.button(f"Play {file}", key=file):
                query_params["article_id"] = [file.split(".")[0]]
                st.experimental_set_query_params(**query_params)
                play_audio(file)
    else:
        st.warning("No audio files available.")

    # If requested file is not available, display a warning message
    if not current_file and article_id:
        st.warning(f"Warning: Audio file for article ID '{article_id}' not found.")

if __name__ == "__main__":
    main()
