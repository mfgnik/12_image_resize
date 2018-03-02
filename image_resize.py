from PIL import Image
import argparse
import sys


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input_path',
        type=str,
        help='path to the image',
        required=True
    )
    parser.add_argument(
        '--height',
        type=int,
        help='height of the result image'
    )
    parser.add_argument(
        '--width',
        type=int,
        help='width of the result image'
    )
    parser.add_argument(
        '--scale',
        type=int,
        help='scale of the result image'
    )
    parser.add_argument(
        '--output_path',
        type=str,
        help='path, where we should save image',
        default=''
    )
    return parser.parse_args()


def get_image(input_file_path):
    return Image.open(input_file_path)


def get_new_size(image, arguments):
    if arguments.scale and (arguments.width or arguments.height):
        print('You can not set both size and scale')
        sys.exit()
    elif arguments.scale:
        width, height = map(lambda x: x * arguments.scale, image.size)
    elif arguments.height and arguments.width:
        width, height = arguments.width, arguments.height
        if width / image.size[0] != height / image.size[1]:
            print('Warning: change of scale')
    elif arguments.height:
        scale = arguments.height / image.size[1]
        width, height = image.size[0] * scale, arguments.height
    elif arguments.width:
        scale = arguments.width / image.size[0]
        width, height = arguments.width, image.size[1] * scale
    else:
        print('You did not write enough arguments')
        sys.exit()
    return map(int, (width, height))


def resize_image(image, width, height):
    return image.resize(size=(width, height))


def get_old_name(file_path):
    return file_path[file_path.rfind('/') + 1:]


def get_new_name(file_path, width, heigth):
    old_name = get_old_name(file_path)
    name = old_name[:old_name.rfind('.')]
    extension = old_name[old_name.rfind('.'):]
    new_name = name + '__' + str(width) + 'x' + str(height) + extension
    return new_name


def output_image(image, output_file_path):
    image.save(output_file_path)


if __name__ == '__main__':
    arguments = parse_arguments()
    image = get_image(arguments.input_path)
    width, height = get_new_size(image, arguments)
    new_name = get_new_name(arguments.input_path, width, height)
    output_path = arguments.output_path + new_name
    output_image(resize_image(image, width, height), output_path)
