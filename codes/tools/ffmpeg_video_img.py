import os
from subprocess import call
from tqdm import tqdm


def extract_frames(src_path, target_path):
    for video_name in tqdm(os.listdir(src_path)):
        filename = src_path + '/' + video_name
        pic_path = target_path + '/'
        # pic_path = target_path + video_name.split('.')[0] + '/'
        if not os.path.exists(pic_path):
            os.mkdir(pic_path)
        pic_name = pic_path + video_name.split('.')[0] + '-%04d.jpg'
        call(["ffmpeg", "-i", filename, "-r", "1", pic_name])


if __name__ == '__main__':
    extract_frames("D:/Workspace/python/ML/book-spine-recognition/data/raw_data/video/", "D:/Workspace/python/ML/book-spine-recognition/data/raw_data/image/")