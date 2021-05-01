import stlotipy.stlotipy as stlotipy

if __name__ == '__main__':
    json = stlotipy.get_spotify_code_image('https://open.spotify.com/track/1Mf27cnAF1Q6Ko83XTM5d1?si=0d057061461d4203')
    print(json)
