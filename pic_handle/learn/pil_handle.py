from PIL import Image


FILE_PATH = './pic/test_pic.jpg'
PEOPLE_PIC = './pic/people.jpg'


def get_image(file_path):
    return Image.open(file_path)


def show_image(image):
    print(image.size, image.format, image.mode)


def transpose(image):
    # - Image.FLIP_LEFT_RIGHT, 表示将图像左右翻转
    # - Image.FLIP_TOP_BOTTOM, 表示将图像上下翻转
    # - Image.ROTATE_90, 表示将图像逆时针旋转90°
    # - Image.ROTATE_180, 表示将图像逆时针旋转180°
    # - Image.ROTATE_270, 表示将图像逆时针旋转270°
    # - Image.TRANSPOSE, 表示将图像进行转置(相当于顺时针旋转90°)
    # - Image.TRANSVERSE, 表示将图像进行转置, 再水平翻转
    image.transpose(Image.ROTATE_180).save('./pic/transpose.jpg')


def paste():
    image = get_image(FILE_PATH)
    region = get_image(PEOPLE_PIC)
    image.paste(region, (50, 50), None)
    image.save('./pic/new_people.jpg')


def screen_shot(image):
    box = (100, 0, 200, 100)
    image.crop(box).save('./pic/screen_shot.jpg')
    # 上面的代码在image图像上裁剪了一个box矩形区域，然后显示出来。
    # box是一个有四个数字的
    # 元组(upper_left_x, upper_left_y,lower_right_x,lower_right_y),
    # 分别表示裁剪矩形区域的左上角x, y坐标, 右下角的x, y坐标,
    # 规定图像的最左上角的坐标为原点(0, 0), 宽度的方向为x轴，高度的方向为y轴，
    # 每一个像素代表一个坐标单位。crop()返回的仍然是一个Image对象。


def thumbnail_pic(image):
    little_pic = image.thumbnail((50, 50), resample=Image.BICUBIC)
    little_pic.show()
    little_pic.save('./pic/little_pic.jpg')


def split(image):
    # 颜色通道分离
    r, g, b = image.split()
    r.save('./pic/r_pic.jpg')
    g.save('./pic/g_pic.jpg')
    b.save('./pic/b_pic.jpg')


def merge():
    r = Image.open('./pic/r_pic.jpg')
    g = Image.open('./pic/g_pic.jpg')
    b = Image.open('./pic/b_pic.jpg')
    rgb_pic = Image.merge('RGB', [r, g, b])
    rbg_pic = Image.merge('RGB', [r, b, g])
    gbr_pic = Image.merge('RGB', [g, b, r])
    grb_pic = Image.merge('RGB', [g, r, b])
    bgr_pic = Image.merge('RGB', [b, g, r])
    brg_pic = Image.merge('RGB', [b, r, g])
    rgb_pic.save('./pic/rgb_pic.jpg')
    rbg_pic.save('./pic/rbg_pic.jpg')
    gbr_pic.save('./pic/gbr_pic.jpg')
    grb_pic.save('./pic/grb_pic.jpg')
    bgr_pic.save('./pic/bgr_pic.jpg')
    brg_pic.save('./pic/brg_pic.jpg')


def main():
    image = get_image(FILE_PATH)
    # screen_shot(image)
    # show_image(image)
    # thumbnail_pic(image)
    # transpose(image)
    # paste()
    # split(image)
    merge()


if __name__ == '__main__':
    main()
