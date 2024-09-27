import requests
import json
import time

# Fetch top 100 games from SteamSpy with retries
def fetch_top_games(retries=5):
    url = "https://steamspy.com/api.php?request=top100in2weeks"
    for attempt in range(retries):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                top_games = response.json()

                # Extract the top 100 app IDs
                top_100_app_ids = [int(app_id) for app_id in top_games.keys()][:100]

                # Save the top games to a file
                with open('steam_top_100_games.json', 'w') as f:
                    json.dump(top_100_app_ids, f)

                return top_100_app_ids

        except requests.ConnectionError as e:
            print(f"Connection error: {e}. Retrying {attempt + 1}/{retries}...")
            time.sleep(5)

    raise Exception("Failed to fetch data after multiple attempts.")


# Function to fetch game details from SteamSpy for multiple games
def fetch_multiple_game_details(app_ids):
    all_game_data = []
    failed_app_ids = []

    for i, app_id in enumerate(app_ids):
        try:
            steamspy_url = f"https://steamspy.com/api.php?request=appdetails&appid={app_id}"
            response = requests.get(steamspy_url)
            game_data = response.json()
            all_game_data.append(game_data)

            # Print progress
            print(f"Fetched data for game {i + 1}/{len(app_ids)}: App ID {app_id}")

            # Save data periodically every 50 games
            if (i + 1) % 50 == 0:
                with open('steam_top_100_game_details.json', 'w') as f:
                    json.dump(all_game_data, f)
                print(f"Saved batch of {i + 1} games to file.")

            # Avoid rate-limiting by sleeping between requests
            time.sleep(1)

        except Exception as e:
            print(f"Error fetching data for app ID {app_id}: {e}")
            failed_app_ids.append(app_id)

    # Final save after all games are processed
    with open('steam_top_100_game_details.json', 'w') as f:
        json.dump(all_game_data, f)
    print(f"Final save complete: {len(all_game_data)} games fetched.")

    if failed_app_ids:
        print(f"Retrying failed app IDs: {len(failed_app_ids)} failures.")
        for app_id in failed_app_ids:
            try:
                steamspy_url = f"https://steamspy.com/api.php?request=appdetails&appid={app_id}"
                response = requests.get(steamspy_url)
                game_data = response.json()
                all_game_data.append(game_data)
                time.sleep(1)

            except Exception as e:
                print(f"Failed again for app ID {app_id}: {e}")

    with open('steam_top_100_game_details.json', 'w') as f:
        json.dump(all_game_data, f)
    print(f"Retry save complete: {len(all_game_data)} games fetched after retries.")

    return all_game_data


if __name__ == '__main__':
    app_ids = fetch_top_games()
    fetch_multiple_game_details(app_ids)
