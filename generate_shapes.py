def generate_shapes(emotions, num_shapes):
    shapes = {'Happy': 'Circle',
              'Angry': 'Triangle',
              'Surprise': 'Ellipse',
              'Sad': 'Rectangle',
              'Fear': 'Line'}

    total_emotion = sum(emotions.values())
    normalized_emotions = {key: value / total_emotion
                           for key, value in emotions.items()}

    num_shapes_per_emotion = {key: round(value * num_shapes)
                              for key, value in normalized_emotions.items()}

    remaining_shapes = num_shapes - sum(num_shapes_per_emotion.values())
    for i in range(remaining_shapes):
        max_emotion = max(num_shapes_per_emotion,
                          key=num_shapes_per_emotion.get)
        num_shapes_per_emotion[max_emotion] += 1

    shapes_list = []
    for emotion, count in num_shapes_per_emotion.items():
        shapes_list.extend([shapes[emotion]] * count)

    return shapes_list
