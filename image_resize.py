from PIL import Image
import argparse
import sys
import os


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
        type=float,
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


def get_new_size_by_dimension(image_width, image_height, height, width):
    if height and width:
        return height, width
    elif height:
        aspect_ratio = height / image_height
        return int(image_width * aspect_ratio), height
    elif width:
        aspect_ratio = width / image_width
        return width, int(image_height * aspect_ratio)


def get_new_size(image, arguments):
    if arguments.scale:
        width, height = map(lambda x: int(x * arguments.scale), image.size)
    else:
        image_width, image_height = image.size
        width, height = get_new_size_by_dimension(
            image_width,
            image_height,
            arguments.height,
            arguments.width
        )
    return width, height


def resize_image(image, width, height):
    return image.resize(size=(width, height))


def get_new_name(file_path, width, heigth):
    name_of_image, extension = os.path.splitext(file_path)
    size = '{}x{}'.format(width, height)
    new_name = '{}__{}{}'.format(name_of_image, size, extension)
    return new_name


def output_image(image, output_file_path):
    image.save(output_file_path)


if __name__ == '__main__':
    arguments = parse_arguments()
    image = get_image(arguments.input_path)
    if (arguments.height or arguments.width) and arguments.scale:
        sys.exit('You can not set both size and scale')
    elif not (arguments.height or arguments.width or arguments.scale):
        sys.exit('You did not write enough arguments')
    else:
        width, height = get_new_size(image, arguments)
        if arguments.width and arguments.height:
            allowed_error = 10 ** -6
            change_dimension = abs(width / image.width - height / image.height)
            if change_dimension > allowed_error:
                print('Warning: change of dimension')
    new_name = get_new_name(arguments.input_path, width, height)
    output_path = arguments.output_path + new_name
    output_image(resize_image(image, width, height), output_path)
