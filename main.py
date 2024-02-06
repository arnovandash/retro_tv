import vlc
import os
import time
import json

STATE_FILE = 'playback_state.json'
PATH = "./" # Update this path to your TV series directory


def get_series_episodes(series_path):
    series_folders = sorted([os.path.join(series_path, f) for f in os.listdir(series_path) if os.path.isdir(os.path.join(series_path, f))])
    series_episodes = {}
    for series_folder in series_folders:
        series_name = os.path.basename(series_folder)
        season_folders = sorted([os.path.join(series_folder, f) for f in os.listdir(series_folder) if os.path.isdir(os.path.join(series_folder, f))])
        for season_folder in season_folders:
            season_name = os.path.basename(season_folder)
            episodes = sorted([os.path.join(season_folder, f) for f in os.listdir(season_folder) if os.path.isfile(os.path.join(season_folder, f))])
            if episodes:  # Only add if there are episodes
                series_episodes.setdefault(series_name, []).extend(episodes)
    return series_episodes

def save_state(state):
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f)

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    return None

def play_episodes(series_episodes):
    # Create a VLC instance with specified video output module
    #instance = vlc.Instance('--vout=caopengllayer', '-vvv')
    instance = vlc.Instance('--vout=macosx')  # Try 'caopengllayer' if 'macosx' does not work

    player = instance.media_player_new()
    #player = vlc.MediaPlayer()

    state = load_state()

    # Ensure starting_position is initialized
    starting_path, starting_position = None, None

    if state:
        starting_path = state.get('episode')
        # Safely get 'position' with a default value of None if it's not found
        starting_position = state.get('position', None)

    for series_name, episodes in series_episodes.items():
        for episode in episodes:
            if starting_path and episode != starting_path:
                continue  # Skip episodes until we find the starting one
            print(f"Now playing: {episode}")
            player.set_media(vlc.Media(episode))
            player.play()
            time.sleep(1)  # Wait for it to start
            if starting_position:
                # Convert starting_position to int since VLC expects milliseconds as int
                player.set_time(int(starting_position))
                # Reset starting_position after seeking to ensure it's only used once
                starting_position = None
            while player.is_playing():
                time.sleep(1)  # Wait for the episode to finish
                current_position = player.get_time()
                # Save state with the current episode and position
                save_state({'episode': episode, 'position': current_position})
            if starting_path:
                # Reset starting_path after it's used to allow the script to continue normally
                starting_path = None
            # Break after one episode to simulate the '90s TV show experience
            break

if __name__ == "__main__":
    series_path = PATH  # Update this path to your TV series directory
    series_path = os.path.expanduser(series_path)  # Expand ~ to the user home directory
    series_episodes = get_series_episodes(series_path)
    play_episodes(series_episodes)
