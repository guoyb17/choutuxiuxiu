import os, argparse, math
from PIL import Image as image
import numpy as np


def get_cdf(cdf):
    for i in range(1, len(cdf)):
        cdf[i] += cdf[i - 1]
    return cdf

def main(ipt_img, opt_img, mode, param):
    src = image.open(ipt_img)
    width, height = src.size
    bitmap = np.array(src)
    if mode == "brightness":
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
    elif mode == "contrast":
        for iter_x in range(height):
            for iter_y in range(width):
                tmp0 = round(param * (bitmap[iter_x][iter_y][0] - 127)) + 127
                tmp1 = round(param * (bitmap[iter_x][iter_y][1] - 127)) + 127
                tmp2 = round(param * (bitmap[iter_x][iter_y][2] - 127)) + 127
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
    elif mode == "gamma":
        for iter_x in range(height):
            for iter_y in range(width):
                tmp0 = round(255 * pow((bitmap[iter_x][iter_y][0] / 255), param))
                tmp1 = round(255 * pow((bitmap[iter_x][iter_y][1] / 255), param))
                tmp2 = round(255 * pow((bitmap[iter_x][iter_y][2] / 255), param))
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
    elif mode == "equalization":
        gray = src.convert('L')
        bins = np.zeros(257)
        for i in range(257):
            bins[i] = i
        cdf = get_cdf(np.histogram(gray, bins, density=True)[0])
        for iter_x in range(height):
            for iter_y in range(width):
                tmp0 = round(255 * cdf[bitmap[iter_x][iter_y][0]])
                tmp1 = round(255 * cdf[bitmap[iter_x][iter_y][1]])
                tmp2 = round(255 * cdf[bitmap[iter_x][iter_y][2]])
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
    dst = image.fromarray(bitmap)
    dst.save(opt_img)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A script to modify 24-bit RGB pictures."
        )
    parser.add_argument("-i", "--input", type=str,
                        default=None,
                        help="input file",
                        required=True
                        )
    parser.add_argument("-o", "--output", type=str,
                        default="out",
                        help="output file"
                        )
    parser.add_argument("-m", "--mode", type=str,
                        help="mode: brightness, contrast, gamma, equalization",
                        required=True
                        )
    parser.add_argument("-p", "--param", type=float,
                        default=None, 
                        help="modify parameter (any value for equalization)",
                        required=True
                        )

    args = parser.parse_args()
    main(args.input, args.output, args.mode, args.param)
