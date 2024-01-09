def check_intersection(shapes, new_shape):
    for shape in shapes:
        if new_shape["type"] == shape["type"]:
            if new_shape["type"] in ["rectangle", "ellipse", "triangle"]:
                if (
                    (new_shape["x2"] > shape["x1"])
                    and (new_shape["x1"] < shape["x2"])
                    and (new_shape["y2"] > shape["y1"])
                    and (new_shape["y1"] < shape["y2"])
                ):
                    return True
            elif new_shape["type"] == "line":
                if (
                    (new_shape["x2"] > shape["x1"])
                    and (new_shape["x1"] < shape["x2"])
                    and (new_shape["y2"] > shape["y1"])
                    and (new_shape["y1"] < shape["y2"])
                ):
                    return True
            elif new_shape["type"] == "star":
                return False
    return False
