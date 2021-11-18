# group6
Study Project - Audio Fingerprinting

The main goal of this project is
  1. learning new songs by fingerprinting them, and
  2. recognizing unknown songs by searching for them in a database of learned songs.

To put it concretely, this project collects random audio which is free to use from Youtube and freemusicarchive.org, processes collected audio, and generates hash from collection to train the classification model. 


Task 1:
We will download random audio files and process to get features from it. 
Spectrogram and histogram show those features. With toolbox, we can use all functions freely.
Options for toolbox:
  -h or -help: provides a guide to use this toolbox
  -s [KEYWORD]
      KEYWORD:
        collect start to collect random audio files
        spec    show spectrogram from FFT result
        pitch   show peaks on spectrogram
        histo   show histogram

Task 2:
We will extract peaks of the audio file and generate hash of it. 
The classification models will be built with implementation of k-fold validation. 
