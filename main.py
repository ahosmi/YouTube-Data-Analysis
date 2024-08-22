#main.py
from youtube_statistics import YTstats

API_KEY="your-api-key"
channel_id ="channel_id of the youtube channel you want to analyze"

yt = YTstats(API_KEY,channel_id)
yt.get_channel_statistics()
yt.get_channel_video_data()
yt.dump()

