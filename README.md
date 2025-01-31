# song-detection

Discover the magic of music with **Song Detection**, your ultimate tool for recognizing songs in seconds. Whether it’s a catchy tune playing in the background, a forgotten melody, or a new track you’ve just heard, **Song Detection** uses advanced audio fingerprinting technology to quickly and accurately identify the song title and artist.

## Dataset
Dataset got from `NoCopyRight Sound` with 150 audio with detail below:

- **Sample Rate: **44.1 Khz (44100 sample)
- **Channel: **2 (Stereo)
- **Precission: **16bit
- **Bitrate**: 320k
csv for train dataset:[﻿dataset train](https://docs.google.com/spreadsheets/d/1-JBYn8MiLIcnJwqT2j33H7iEbVIgCUDNdG68yBDW5zc/export?format=csv&id=1-JBYn8MiLIcnJwqT2j33H7iEbVIgCUDNdG68yBDW5zc&gid=1280949540)  

csv for test dataset:[﻿dataset test](https://docs.google.com/spreadsheets/d/1-JBYn8MiLIcnJwqT2j33H7iEbVIgCUDNdG68yBDW5zc/export?format=csv&id=1-JBYn8MiLIcnJwqT2j33H7iEbVIgCUDNdG68yBDW5zc&gid=328562984) 

**Schema:**

| title | artist | copyright |
| ----- | ----- | ----- |
| ... | ... | ... |
| ... | ... | ... |


## Folder Structures
```markdown
├─ mfcc.ipynb
├─ dtw.ipynb
├─ evaluation.ipynb
├─ ceremony.ipynb
├─ csv
│  ├─ train.csv
│  └─ test.csv
├─ audio             # store all dataset (.mp3)
│  ├─ train          # store all train dataset (.mp3)
│  └─ test           # store all test dataset (.mp3)_
_│_     _├─ normal      # no noise
│     │  ├─ 100      # no noise and 100% duration
│     │  └─ 50       # no noise and 50% duration
│     └─ noise       # with noise
│        ├─ 100      # with noise and 100% duration
│        └─ 50       # with noise and 50% duration
├─ npy
│  ├─ train          # store all train features (.npy)
│  │  ├─ 05          # store all train features (0.5s frame) (.npy)
│  │  ├─ 10
│  │  └─ 15
│  └─ test           # store all test features (.npy)
│     ├─ normal      # store all test features (no noise) (.npy)
│     │  ├─ 100      # store all test features (no noise, 100% duration) (.npy)     
│     │  │  ├─ 05    # store all test features (no noise, 100% duration, 0.5s frame) (.npy)
│     │  │  ├─ 10
│     │  │  └─ 15
│     │  └─ 50
│     │     ├─ 05
│     │     ├─ 10
│     │     └─ 15
│     └─ noise
│        ├─ 100
│        │  ├─ 05
│        │  ├─ 10
│        │  └─ 15
│        └─ 50
│           ├─ 05
│           ├─ 10
│           └─ 15
└ results            # evaluation result
```


## Evaluation Result
| Train | Test_Type | Test_Duration | Test_frame | Accuracy | Average Exec Time |
| ----- | ----- | ----- | ----- | ----- | ----- |
| frame 0.5s | normal | 50% | frame 0.5s | ... | ... |
| frame 0.5s | normal | 100% | frame 0.5s | ... | ... |
| frame 0.5s | noise | 50% | frame 0.5s | ... | ... |
| frame 0.5s | noise | 100% | frame 0.5s | ... | ... |
| frame 1.0s | normal | 50% | frame 1.0s | ... | ... |
| frame 1.0s | normal | 100% | frame 1.0s | ... | ... |
| frame 1.0s | noise | 50% | frame 1.0s | ... | ... |
| frame 1.0s | noise | 100% | frame 1.0s | ... | ... |
| frame 1.5s | normal | 50% | frame 1.5s | ... | ... |
| frame 1.5s | normal | 100% | frame 1.5s | ... | ... |
| frame 1.5s | noise | 50% | frame 1.5s | ... | ... |
| frame 1.5s | noise | 100% | frame 1.5s | ... | ... |


