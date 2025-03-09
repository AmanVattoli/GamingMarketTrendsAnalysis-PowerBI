# Steam Analytics: Game Ownership, Sales, and User Reviews

## Dashboard

![Steam Analytics Dashboard](https://github.com/user-attachments/assets/91824be0-d0d5-4f30-8c88-9f6a35660c58)

### Project Overview  
This project focuses on analyzing and visualizing data from Steam's game library, specifically focusing on the **top 100 games in the past 2 weeks**. The data provides insights into game ownership, sales trends, price distributions, and user reviews. The Power BI dashboard helps stakeholders in the gaming industry make informed decisions based on the sales performance of games, user feedback, and market trends.

### Data Extraction

The data used in this analysis was extracted using a Python script, `fetchTopGames.py`, which pulls the top 100 games from SteamSpy and retrieves detailed game information. The script stores the data in a JSON format that is then processed and stored in Azure Blob Storage for further analysis.

#### How the Script Works:

1. **Fetching Top 100 Games**:  
   The script first calls SteamSpy’s API to fetch the top 100 most-played games in the past two weeks. It retries up to 5 times in case of connection errors and saves the game IDs into a file (`steam_top_100_games.json`).

   - **`fetch_top_games()`**:  
   This function makes an API request to SteamSpy, extracts the top 100 game app IDs, and stores them in a JSON file for later use.

2. **Fetching Detailed Game Information**:  
   Once the app IDs are saved, the script proceeds to fetch detailed data for each game (including ownership, reviews, and price) from SteamSpy’s app details API.

   - **`fetch_multiple_game_details()`**:  
   This function iterates over the list of game app IDs and fetches detailed information about each game. It handles API rate limits by introducing delays between requests and saves game details periodically (in batches of 50). If any app fails to fetch its data, the script retries failed app IDs after the initial run.

3. **Saving and Storing Data**:  
   After gathering the data for all 100 games, the script saves the information in a JSON file (`steam_top_100_game_details.json`). This data is then cleaned and processed before being stored in Azure Blob Storage for use in Power BI.

### **Key Features:**
- **KPIs:** Total Games, Average Price, Total Developers, and Total Publishers.
- **Price Distribution:** Breakdown of games by price range.
- **Positive Review Analysis:** Relationship between game price and review sentiment.
- **Game Performance:** Top games ranked by ownership and review percentage.
- **Publisher & Developer Impact:** Largest publishers and developers by total game ownership.
- **Interactive Filtering:** Users can filter by **Developer** and **Publisher** to refine insights.
