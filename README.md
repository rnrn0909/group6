# Study Project 21/22 - Audio Fingerprinting: Group 6

The main goal of this project is
  1. learning new songs by fingerprinting them, and
  2. recognizing unknown songs by searching for them in a database of learned songs.

To put it concretely, this project collects random audio which is free to use from Youtube and freemusicarchive.org, processes collected audio, and generates hash from collection to train the classification model. (~ 26. Nov)

## Task 1
- download random audio files and process to get features from it
- show features with spectrogram and histogram
- provide toolbox
- Options for toolbox:
  ```sh
    -h or -help : provides a guide to use this toolbox 
    -s [KEYWORD] : execute depending on provided keyword
    KEYWORD
      collect : start to collect random audio files
      spec : show spectrogram from FFT result
      pitch : show peaks on spectrogram
      histo : show histogram
  ```

## Util
- [youtube_dl]
- [librosa]
- [scipy]


## Task 2
 - extract peaks as discrete pairs
 - generate hashes from pairs
 - build classification models implementing k-fold cross validation
 
