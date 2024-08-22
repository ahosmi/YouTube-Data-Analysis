#main.py
from youtube_statistics import YTstats

API_KEY="AIzaSyBmnKWC5gTLXm0Vny2CBQOE9gQw4TIM9o4"
channel_id ="UCqECaJ8Gagnn7YCbPEzWH6g"

yt = YTstats(API_KEY,channel_id)
yt.get_channel_statistics()
yt.get_channel_video_data()
yt.dump()

