# 丑图秀秀（choutuxiuxiu）

### 数字图像处理 第一次作业

如有疑问，请联系：guoyb17@mails.tsinghua.edu.cn

程序接受形如以下指令用法的参数：

```shell
python3 choutuxiuxiu.py -i experiment.jpg -o experiment.gamma.compression.png -m gamma -p 0.5
```

其中：-i为输入图片文件；-o为保存的图片文件；-m是点处理方式，目前接受"brightness"（亮度）、"contrast"（对比度）、"gamma"（Gamma校正)、"equalization"（灰度直方图均衡）；-p为处理参数，对于亮度，表示像素点值平移量（正表示增加亮度，负表示降低亮度），对于对比度，表示倍数/斜率（大于1表示增加对比度，小于1表示减少对比度），对于Gamma校正，表示Gamma系数（大于1表示压缩，小于1表示展开），对于直方图均衡，不需要该参数，但程序设定是必须输入，因此输入任意值即可。

程序通过Python 3实现，基本思路是借助pillow包载入图片，然后对每个像素的每个颜色通道分别进行变换，例如：

```python
for iter_x in range(height):
    for iter_y in range(width):
        tmp0 = bitmap[iter_x][iter_y][0] + round(param)
        tmp1 = bitmap[iter_x][iter_y][1] + round(param)
        tmp2 = bitmap[iter_x][iter_y][2] + round(param)
        if tmp0 > 255:
            bitmap[iter_x][iter_y][0] = 255
        elif tmp0 < 0:
            bitmap[iter_x][iter_y][0] = 0
        else:
            bitmap[iter_x][iter_y][0] = tmp0
        if tmp1 > 255:
            bitmap[iter_x][iter_y][1] = 255
        elif tmp1 < 1:
            bitmap[iter_x][iter_y][1] = 0
        else:
            bitmap[iter_x][iter_y][1] = tmp1
        if tmp2 > 255:
            bitmap[iter_x][iter_y][2] = 255
        elif tmp2 < 0:
            bitmap[iter_x][iter_y][2] = 0
        else:
            bitmap[iter_x][iter_y][2] = tmp2
```

以上代码片段是对亮度变换的部分处理过程，其他基本同理。

特别地，对于灰度直方图均衡，要将图片以灰度模式打开（PIL.Image中打开为'L'模式），然后利用numpy.histogram统计像素，然后累加得到CDF，作为使用的LUT。

## 特别声明

程序作者，即本人，不对代码二次使用者的一切学术或非学术行为负责。对本人开源的代码的一切包括但不限于复制、参考、修改、运行等的使用行为，由此产生的一切包括但不限于学术、经济、法律等的后果，本人概不负责，且由此对本人造成的一切损害，保留追究责任权利。（ 在法律允许的范围内， ）一切解释权归本人所有。
