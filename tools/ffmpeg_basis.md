参考：https://www.jianshu.com/p/ddafe46827b7

1、视频转换格式

    ffmpeg -i test.avi test.mp4

2、视频截图保存为图片

    ffmpeg -i inputfile.avi -ss 00:00:20 -t 10 -r 1 -q:v 2 -f image2 image-%05d.jpg
    -i:输入流
    -r:指定抽取的帧  即从视频中每秒抽取图片的数量 1代表每秒抽取一帧
    -f:保存图片使用的格式  可省略
    -q:v表示存储jpeg的图像质量，一般2是高质量。
    -ss：表示开始切割的时间
    -t：表示要切多少时间
    Image-%05d.jpg:指定文件的输出名字

