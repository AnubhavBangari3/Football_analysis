from utils import read_videos,save_video
from trackers import Tracker
def main():
        video_frames=read_videos('Videos/08fd33_4.mp4')
        tracker=Tracker('models/yolov5xu.pt')
        tracks=tracker.get_object_trades(video_frames)
        save_video(video_frames,'output_videos/output_video.avi')
if __name__ == "__main__":
         main()