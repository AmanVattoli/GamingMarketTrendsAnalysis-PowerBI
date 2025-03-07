# Steam Analytics: Game Ownership, Sales, and User Reviews

### Overview  
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

### Key Features:

- **Distribution of Games by Price Range**
- **Top Games by Ownership/Sales**
- **Games Ranked by Positive Review Percentage**
- **Top Publishers by Game Ownership/Sales**

## Dashboard Overview

![Steam Analytics Dashboard](https://github.com/user-attachments/assets/e22e5583-a39d-4f10-abf1-419d3abc9db7)


### 1. **Distribution of Games by Price Range**
   - **Insight**: The majority of games fall within the $0–$10 price range, indicating that most popular titles on Steam are affordably priced. This is reflective of sales strategies favoring lower price points for mass market adoption.

### 2. **Top Games by Ownership/Sales**
   - **Insight**: Games like *Dota 2* and *PUBG* lead the chart in terms of ownership, with over 500 million owners combined. These free-to-play or massively multiplayer online (MMO) games dominate the platform in terms of engagement and popularity.

### 3. **Games Ranked by Lowest to Highest Positive Review Percentage**
   - **Insight**: Games like *Battlefield 2042* and *NBA 2K20* received some of the lowest positive review percentages, indicating dissatisfaction among the player base.

### 4. **Top Publishers by Game Ownership/Sales**
   - **Insight**: Valve dominates the publisher category with the highest number of game owners, largely due to their highly popular games like *Dota 2*. Other key publishers include KRAFTON, Electronic Arts, and Rockstar, all contributing significant sales across their portfolios.
