import os
from yt_dlp import YoutubeDL

link_list = [
'https://youtu.be/XtY1zJh8b_0?si=gfJqud0ITAM_j42v',
'https://youtu.be/ixGv5oGjsPM?si=IJKP8fckv4rntkyy',
'https://youtu.be/9FRnpw_twjw?si=fBSetUEoWh4FYfZ9',
'https://youtu.be/AC4WWkFw970?si=215pB1VPbFqY1Jzm',
'https://youtu.be/pFEm5qbQWsY?si=RNXs3YzYbIi0FyYR',
'https://youtu.be/-PCfSm8kMaY?si=eQmY4NbJBavrYVa-',
'https://youtu.be/G1OXOTRTDi0?si=T_tR3Q1ID9hwvc-e'
]


save_path = r"C:\Users\MIQDAD\Documents\Nasheeds"

ydl_opts = {
    'format': 'bestaudio/best',  # Best quality video and audio
    'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),  # Save path
    'http_headers': {  # Add headers for YouTube access
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    },
}

with YoutubeDL(ydl_opts) as ydl:
    for link in link_list:
        try:
            ydl.download([link])
        except Exception as e:
            print(f"Failed to process {link}: {e}")