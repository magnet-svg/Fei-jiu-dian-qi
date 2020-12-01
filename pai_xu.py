import os

folder_path ='E:/PyCharm/mu_biao_jian_ce/YOLOV4/yolov4-keras-master/VOCdevkit/VOC2007/Image_strong'
num = 1694

if __name__ == '__main__':
    for file in os.listdir(folder_path):
        s = '%06d' % num  # 前面补零占位
        os.rename(os.path.join(folder_path, file), os.path.join(folder_path,  str(s) + '.jpg'))
        num += 1