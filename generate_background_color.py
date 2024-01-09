import matplotlib.pyplot as plt


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


def visualize_color(color):
    plt.imshow([[color]])
    plt.axis('off')
    plt.show()


emotion_dict = {'Happy': 0.1,
                'Angry': 0.2,
                'Surprise': 0.3,
                'Sad': 0.5,
                'Fear': 0.0}
result_color = generate_background_color(emotion_dict)

