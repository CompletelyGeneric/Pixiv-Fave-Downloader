Pixiv Fave Downloader
=====================

This script downloads your Pixiv saves to a given directory, remembers where it left off and only
downloads the difference. Additionally, this script also supports multiple users.


Setup
-----

    pip install pixivpy

Modify config.json with your username, password, and desired save directory.  
subdir_threshold (Default: 0) determines how many pages a work must have before it creates a subdirectory for that work.  
Each user can set this value independantly with a value of 0 disabling this feature    
The directory naming structure for created subdirectories is: "artist name - artist's profile ID"  


Run
---
	chmod +x pixiv-fave-dl.py
    ./pixiv-fave-dl.py

