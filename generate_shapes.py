import random
from PIL import Image, ImageDraw

from check_intersection import check_intersection
from generate_background_color import generate_background_color


def generate_shapes(emotion_dict, width, height):

    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    background_color = generate_background_color(emotion_dict)
    draw.rectangle([0, 0, width, height], fill=background_color)

    shapes = []
    num_shapes = random.randint(1, 10)

    for _ in range(num_shapes):
        shape_type = random.choice(
            ["rectangle", "ellipse", "triangle", "line", "star"])
        color = (
            random.randint(0, 255), random.randint(0, 255),
            random.randint(0, 255))

        if shape_type == "rectangle":
            x1, y1, x2, y2 = sorted(
                [random.randint(0, width - 1) for _ in range(4)])
            new_shape = {"type": shape_type, "x1": x1, "y1": y1, "x2": x2,
                         "y2": y2}
            if not check_intersection(shapes, new_shape):
                shapes.append(new_shape)
                draw.rectangle([x1, y1, x2, y2], fill=color)
        elif shape_type == "ellipse":
            x1, y1, x2, y2 = sorted(
                [random.randint(0, width - 1) for _ in range(4)])
            new_shape = {"type": shape_type, "x1": x1, "y1": y1, "x2": x2,
                         "y2": y2}
            if not check_intersection(shapes, new_shape):
                shapes.append(new_shape)
                draw.ellipse([x1, y1, x2, y2], fill=color)
        elif shape_type == "triangle":
            x1, y1, x2, y2, x3, y3 = [random.randint(0, width - 1) for _ in
                                      range(6)]
            new_shape = {"type": shape_type, "x1": x1, "y1": y1, "x2": x2,
                         "y2": y2, "x3": x3, "y3": y3}
            if not check_intersection(shapes, new_shape):
                shapes.append(new_shape)
                draw.polygon([x1, y1, x2, y2, x3, y3], fill=color)
        elif shape_type == "line":
            x1, y1, x2, y2 = [random.randint(0, width - 1) for _ in range(4)]
            new_shape = {"type": shape_type, "x1": x1, "y1": y1, "x2": x2,
                         "y2": y2}
            if not check_intersection(shapes, new_shape):
                shapes.append(new_shape)
                draw.line([(x1, y1), (x2, y2)], fill=color, width=3)
        elif shape_type == "star":
            x, y = random.randint(0, width - 1), random.randint(0, height - 1)
            size = random.randint(10, 50)
            new_shape = {"type": shape_type, "x": x, "y": y, "size": size}
            if not check_intersection(shapes, new_shape):
                shapes.append(new_shape)
                draw.line([(x, y - size), (x, y + size)], fill=color, width=2)
                draw.line([(x - size, y), (x + size, y)], fill=color, width=2)

    return image