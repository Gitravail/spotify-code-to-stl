import stlotipy.stlotipy as stlotipy
import matplotlib.pyplot as plt

if __name__ == '__main__':
    image = stlotipy.get_spotify_code_image('https://open.spotify.com/album/2Cv2mrKMRyYuXJTlQmY4hj?si=-bzPyrJ6QxeO-oUaGDXjyA')
    plt.imshow(image)
    plt.show()
