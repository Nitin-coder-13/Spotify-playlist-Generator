import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Authentication with playlist modification scope
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="Your client-id",
    client_secret="Your client-secret",
    redirect_uri="Your redirect_uri",
    scope="playlist-modify-public playlist-modify-private user-top-read"
))

# Get current user ID
user_id = sp.current_user()['id']

print("🎵 Spotify Playlist Generator 🎵\n")
print("Choose an option:")
print("1. Create playlist from your top tracks")
print("2. Create playlist based on an artist")
print("3. Create playlist based on a genre/mood")

choice = input("\nEnter your choice (1-3): ")

if choice == "1":
    # Generate playlist from user's top tracks
    playlist_name = input("Enter playlist name: ")
    limit = int(input("How many songs? (max 50): "))

    # Get top tracks2
    top_tracks = sp.current_user_top_tracks(limit=limit, time_range='short_term')
    track_uris = [track['uri'] for track in top_tracks['items']]

    # Create playlist
    playlist = sp.user_playlist_create(user_id, playlist_name, public=True,
                                       description="Generated from my top tracks")
    sp.playlist_add_items(playlist['id'], track_uris)

    print(f"\n✅ Playlist '{playlist_name}' created with {len(track_uris)} songs!")
    print(f"🔗 Link: {playlist['external_urls']['spotify']}")

elif choice == "2":
    # Generate playlist based on artist
    artist_name = input("Enter artist name: ")

    # Search for artist
    results = sp.search(q=f"artist:{artist_name}", type='artist', limit=1)

    if results['artists']['items']:
        artist = results['artists']['items'][0]
        artist_id = artist['id']
        print(f"\n🎤 Found: {artist['name']}")

        # Get artist's top tracks(api call)
        top_tracks = sp.artist_top_tracks(artist_id)
        track_uris = [track['uri'] for track in top_tracks['tracks'][:10]]

        # Get related artists and their tracks (with error handling)
        try:
            related = sp.artist_related_artists(artist_id)
            for related_artist in related['artists'][:3]:
                try:
                    related_tracks = sp.artist_top_tracks(related_artist['id'])
                    track_uris.extend([track['uri'] for track in related_tracks['tracks'][:5]])
                except:
                    continue
        except Exception as e:
            print(f"⚠️ Couldn't fetch related artists, using only {artist['name']}'s tracks")

        # Create playlist
        playlist_name = f"{artist['name']} & Similar Artists"
        playlist = sp.user_playlist_create(user_id, playlist_name, public=True,
                                           description=f"Based on {artist['name']}")
        sp.playlist_add_items(playlist['id'], track_uris[:50])

        print(f"\n✅ Playlist '{playlist_name}' created with {len(track_uris[:50])} songs!")
        print(f"🔗 Link: {playlist['external_urls']['spotify']}")
    else:
        print("❌ Artist not found!")

elif choice == "3":
    # Generate playlist based on genre/mood
    seed = input("Enter genre or mood (e.g., rock, chill, happy, workout): ")
    num_songs = int(input("How many songs? (max 100): "))

    # Get recommendations based on seed
    # Try as genre first
    try:
        recommendations = sp.recommendations(seed_genres=[seed], limit=min(num_songs, 100))
        track_uris = [track['uri'] for track in recommendations['tracks']]

        if track_uris:
            playlist_name = f"{seed.capitalize()} Vibes"
            playlist = sp.user_playlist_create(user_id, playlist_name, public=True,
                                               description=f"Generated for {seed} mood")
            sp.playlist_add_items(playlist['id'], track_uris)

            print(f"\n✅ Playlist '{playlist_name}' created with {len(track_uris)} songs!")
            print(f"🔗 Link: {playlist['external_urls']['spotify']}")
        else:
            print("❌ Couldn't generate playlist for that genre/mood")
    except:
        # If genre doesn't work, search for tracks matching the keyword
        results = sp.search(q=seed, type='track', limit=min(num_songs, 50))
        track_uris = [track['uri'] for track in results['tracks']['items']]

        if track_uris:
            playlist_name = f"{seed.capitalize()} Mix"
            playlist = sp.user_playlist_create(user_id, playlist_name, public=True,
                                               description=f"Songs matching {seed}")
            sp.playlist_add_items(playlist['id'], track_uris)

            print(f"\n✅ Playlist '{playlist_name}' created with {len(track_uris)} songs!")
            print(f"🔗 Link: {playlist['external_urls']['spotify']}")
        else:
            print("❌ Couldn't find tracks for that search")

else:
    print("❌ Invalid choice!")

print("\n🎧 Check your Spotify app to see your new playlist!")
