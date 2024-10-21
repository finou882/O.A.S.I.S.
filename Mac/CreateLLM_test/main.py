from yt_dlp import YoutubeDL

#最高の画質と音質を動画をダウンロードする
ydl_opts = {'proxy': 'http://10.5.1.1:8080'}

#動画のURLを指定
with YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.iwara.tv/video/vqx8Nm5DN41bK9/mesmerizer'])