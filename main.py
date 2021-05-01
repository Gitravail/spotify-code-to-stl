import stlotipy.stlotipy as stlotipy
import matplotlib.pyplot as plt

url = 'https://open.spotify.com/album/2Cv2mrKMRyYuXJTlQmY4hj?si=-bzPyrJ6QxeO-oUaGDXjyA'

if __name__ == '__main__':
    sizes = stlotipy.Sizes
    image = stlotipy.get_spotify_code_image(url, stlotipy.Sizes.MEDIUM)
    if image:
        plt.imshow(image)
        plt.show()
