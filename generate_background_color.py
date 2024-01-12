def generate_background_color(emotions):
    base_palette = {
        'Happy': (255, 255, 0),
        'Angry': (255, 0, 0),
        'Surprise': (0, 255, 255),
        'Sad': (0, 0, 255),
        'Fear': (128, 0, 128)
    }
    combined_color = [0, 0, 0]

    for emotion, value in emotions.items():
        weight = value / sum(emotions.values())
        for i in range(3):
            combined_color[i] += int(weight * base_palette[emotion][i])

    return tuple(combined_color)
