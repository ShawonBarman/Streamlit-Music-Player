# Streamlit-Music-Player-with-Dynamic-Playlist-and-Language-Selection

<p>This project is a Streamlit-based web application that serves as a music player. It allows users to select between Chinese and English audio files, create a playlist of their choice, play audio files individually, and toggle between loop and shuffle playback modes.</p>

<p>Here's a breakdown of the key functionalities and components in the music_player.py file:</p>

<ol>
  <li><strong>Imports: </strong>The code of music_player.py file imports necessary libraries, including Streamlit for building the web interface, os for file system operations, random for shuffling audio files, and pydub for audio file manipulation.</li>
  <li><strong>load_audio_files(language): </strong>This function loads audio files based on the selected language (Chinese or English) from the "music_folder" directory. It filters and organizes the files accordingly and returns a dictionary mapping article IDs to their corresponding audio file names.</li>
  <li><strong>play_audio(file): </strong>This function plays the selected audio file using Streamlit's st.audio function. It opens the audio file from the "music_folder" directory and streams it to the user's browser.</li>
  <li><strong>create_playlist(language, playlist_size, cn_audio_files, en_audio_files): </strong>This function creates a playlist of the specified size by randomly selecting audio files based on the selected language. It concatenates the selected audio files into a single playlist and exports it as "playlist.wav" in the "music_folder" directory. The path to the generated playlist is returned.</li>
  <li><strong>main(): </strong>The main function sets up the Streamlit web application. It includes:
  <ul>
    <li>Language selection: Users can choose between Chinese and English audio files.</li>
    <li>Playback Mode selection: Users can choose between Loop and Shuffle playback modes.</li>
    <li>Playlist Size selection: Users can specify the number of audio files in the playlist.</li>
    <li>Create Playlist button: When clicked, this button generates a playlist based on the selected parameters and plays it for the user.</li>
    <li>Toggle between Chinese and English audio files: Users can switch between languages and browse and play available audio files.</li>
    <li>Display of audio files: Audio files are displayed as buttons, and users can click on them to play the selected file.</li>
  </ul>
  </li>
</ol>

<p>The code of music_player.py file also handles URL query parameters (e.g., "article_id") to maintain state and keep track of the selected audio file.</p>
<p>The application warns the user if there are no audio files available for playback or if the requested audio file is not found.</p>
<p>Overall, the code of music_player.py file creates a user-friendly web application for playing and managing audio files, with options for playlist creation and language selection. Users can easily navigate and enjoy their selected audio content.</p>
