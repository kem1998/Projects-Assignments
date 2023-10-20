import requests
import pandas as pd
import time

CLIENT_ID = 'ff85dfa9bf4f4ab0b354385b1c7a25e9'
CLIENT_SECRET = '20b26e359b8e47838701997fee8d6bba'

def get_token(client_id, client_secret):
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    })
    auth_response_data = auth_response.json()
    return auth_response_data['access_token']

def get_album_cover(track_name, artist_name, token):
    base_url = 'https://api.spotify.com/v1/search'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    query = f'track:{track_name} artist:{artist_name}'
    response = requests.get(base_url, headers=headers, params={
        'q': query,
        'type': 'track',
    })
    response_data = response.json()
    tracks = response_data['tracks']['items']
    if not tracks:
        return None
    album_cover_url = tracks[0]['album']['images'][0]['url']
    return album_cover_url

def add_album_cover_to_csv(input_csv, output_csv):
    df = pd.read_csv(input_csv, encoding='ISO-8859-1')
    token = get_token(CLIENT_ID, CLIENT_SECRET)
    
    # Create a new column for album cover URLs and initialize with None
    df['album_cover_url'] = None
    
    for index, row in df.iterrows():
        print(f"Fetching album cover for {row['track_name']} by {row['artist(s)_name']}...")
        cover_url = get_album_cover(row['track_name'], row['artist(s)_name'], token)
        df.at[index, 'album_cover_url'] = cover_url
        time.sleep(1)  # Introducing a delay to avoid hitting rate limits

    df.to_csv(output_csv, index=False, encoding='ISO-8859-1')
    print(f"Updated CSV saved to {output_csv}")

input_csv = 'spotify-2023.csv'
output_csv = 'Transformed_spotify_2023.csv'
add_album_cover_to_csv(input_csv, output_csv)



