import random
from PIL import Image, ImageDraw
from check_intersection import check_intersection
from generate_background_color import generate_background_color
from generate_shapes import generate_shapes


def generate_image(emotion_dict, width, height):
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    background_color = generate_background_color(emotion_dict)
    draw.rectangle([0, 0, width, height], fill=background_color)

    num_shapes = random.randint(1, 10)

    shapes = generate_shapes(emotion_dict, num_shapes)

    for shape_type in shapes:
        color = tuple(random.randint(0, 255) for _ in range(3))

        if shape_type == "Circle":
            x, y, radius = [random.randint(0, width - 1) for _ in range(3)]
            new_shape = {"type": shape_type, "x": x, "y": y, "radius": radius}

        elif shape_type == "Triangle":
            points = [(random.randint(0, width - 1), random.randint(0, height - 1)) for _ in range(3)]
            new_shape = {"type": shape_type, "points": points}

        elif shape_type == "Ellipse":
            x1, y1, x2, y2 = sorted([random.randint(0, width - 1) for _ in range(4)])
            new_shape = {"type": shape_type, "x1": x1, "y1": y1, "x2": x2, "y2": y2}

        elif shape_type == "Rectangle":
            x1, y1, x2, y2 = sorted([random.randint(0, width - 1) for _ in range(4)])
            new_shape = {"type": shape_type, "x1": x1, "y1": y1, "x2": x2, "y2": y2}

        elif shape_type == "Line":
            num_segments = random.randint(1, 3)
            points = [(random.randint(0, width - 1), random.randint(0, height - 1)) for _ in range(num_segments)]
            new_shape = {"type": shape_type, "points": points}

        if shape_type == "Circle":
            draw.ellipse([x - radius, y - radius, x + radius, y + radius], fill=color)
        elif shape_type == "Triangle":
            draw.polygon(points, fill=color)
        elif shape_type == "Ellipse":
            draw.ellipse([x1, y1, x2, y2], fill=color)
        elif shape_type == "Rectangle":
            draw.rectangle([x1, y1, x2, y2], fill=color)
        elif shape_type == "Line":
            for i in range(len(points) - 1):
                draw.line([points[i], points[i + 1]], fill=color, width=3)

    return image
