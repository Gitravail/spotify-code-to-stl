import stlotipy.stlotipy as stlotipy
import matplotlib.pyplot as plt

url = 'https://open.spotify.com/track/5YTJXAM6j8jEQ5vC8Q67GL?si=b52d2587487a49fe'

if __name__ == '__main__':
    sizes = stlotipy.Sizes
    image = stlotipy.get_spotify_code_image(url, stlotipy.Sizes.MEDIUM)
    if image:
        plt.imshow(image)
        plt.show()
