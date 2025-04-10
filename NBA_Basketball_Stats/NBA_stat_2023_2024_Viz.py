"""This script visualizes the stats of 2 players"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# initialize filename
FILENAME = "NBA_Basketball_Stats/NBA_stat_2023_2024.csv"
# read the CSV file
df = pd.read_csv(FILENAME, encoding="latin-1")
# print the first 5 row of the dataset
# print(df.head())
# attributes needed
df = df[["Player", "PTS", "AST", "3P%", "FG%", "TRB", "STL", "BLK", "TOV"]]
df2 = df[["Player", "PTS", "AST"]].copy()
df3 = df[["Player", "TRB", "TOV"]].copy()
df4 = df[["Player", "STL", "BLK"]].copy()
df5 = df[["Player", "3P%", "FG%"]].copy()
# remove Nan
df.dropna(inplace=True)
# make the player names in lower columns
df2["Player"] = df2["Player"].str.lower()
df3["Player"] = df3["Player"].str.lower()
df4["Player"] = df4["Player"].str.lower()
df5["Player"] = df5["Player"].str.lower()
# set player as index
df2.set_index("Player", inplace=True)
df3.set_index("Player", inplace=True)
df4.set_index("Player", inplace=True)
df5.set_index("Player", inplace=True)


def player_prompt():
    """This is a function that prompts the user for the player names"""
    print("NBA Player Stat Comparison Tool for The 2023/2024 Season")
    player1 = input("Enter the name of the first player: ").lower().strip()
    player2 = input("Enter the name of the second player: ").lower().strip()
    if (
        player1 in df2.index
        and player2 in df2.index
        and player1 in df3.index
        and player2 in df3.index
        and player1 in df4.index
        and player2 in df4.index
        and player1 in df5.index
        and player2 in df5.index
    ):
        print(f"You want to compare {player1.title()} to {player2.title()}")
        return player1, player2
    else:
        print("Player's name is incorrect or does not exist in this dataset")
        return None, None


def plot_stat_comparison_chart(player1, player2):
    # get the stats of each players
    stats_of_player1 = df2.loc[player1]
    stats_of_player2 = df2.loc[player2]
    efficiency_stats_of_player1 = df3.loc[player1]
    efficiency_stats_of_player2 = df3.loc[player2]
    defensive_stats_of_player1 = df4.loc[player1]
    defensive_stats_of_player2 = df4.loc[player2]
    shooting_efficiency_of_player1 = [
        df5.loc[player1, "3P%"],
        df5.loc[player1, "FG%"],
    ]
    shooting_efficiency_of_player2 = [
        df5.loc[player2, "3P%"],
        df5.loc[player2, "FG%"],
    ]
    # labels we would be plotting on the x axis
    labels = ["PTS", "AST"]
    labels1 = ["TRB", "TOV"]
    labels2 = ["STL", "BLK"]
    labels3 = ["3P%", "FG%"]
    # extracts the values of the stats of the labels
    player1_stats = stats_of_player1[labels].values
    player2_stats = stats_of_player2[labels].values
    player1_efficiency_stats = efficiency_stats_of_player1[labels1].values
    player2_eficiency_stats = efficiency_stats_of_player2[labels1].values
    player1_defensive_stats = defensive_stats_of_player1[labels2].values
    player2_defensive_stats = defensive_stats_of_player2[labels2].values
    # flatten the shooting efficiency stats to avoid nested lists
    combined_stats = shooting_efficiency_of_player1 + shooting_efficiency_of_player2
    # Create a combined labels for both players
    combined_labels = [f"{stat} ({player1.title()})" for stat in labels3] + [
        f"{stat} ({player2.title()})" for stat in labels3
    ]
    
    comparison_df = pd.DataFrame(
        {
            "stats": labels * 2,
            "values": np.concatenate([player1_stats, player2_stats]),
            "player": [player1] * len(labels) + [player2] * len(labels),
        }
    )
    # 2nd data frame
    efficiency_comparison_df = pd.DataFrame(
        {
            "stats": labels1 * 2,
            "values": np.concatenate(
                [player1_efficiency_stats, player2_eficiency_stats]
            ),
            "player": [player1] * len(labels) + [player2] * len(labels),
        }
    )

    # 3rd data frame
    defensive_stats_comparison_df = pd.DataFrame(
        {
            "stats": labels2 * 2,
            "values": np.concatenate(
                [player1_defensive_stats, player2_defensive_stats]
            ),
            "player": [player1] * len(labels) + [player2] * len(labels),
        }
    )

    # visualizing a barchart for the Points Vs Assists
    # figure of width 10 and height 6
    fig, ax = plt.subplots(2, 2, figsize=(10, 6))
    sns.barplot(
        data=comparison_df,
        x="stats",
        y="values",
        hue="player",
        ax=ax[0, 0],
    )
    # adding labels
    ax[0, 0].set_xlabel("Stat Categories", fontfamily="DejaVu Serif")
    ax[0, 0].set_ylabel("Values", fontfamily="DejaVu Serif")
    ax[0, 0].set_title(
        f"{player1.title()} vs {player2.title()} \n (Points vs Assists)",
        fontfamily="DejaVu Serif",
    )
    ax[0, 0].legend()
    ax[0, 0].grid(
        axis="y",
        linestyle="--",
        alpha=0.6,
    )
    # visualizing a barchart of Total Rebounds vs Turnovers
    sns.barplot(
        data=efficiency_comparison_df, x="stats", y="values", hue="player", ax=ax[0, 1]
    )

    # adding labels
    ax[0, 1].set_xlabel("Stat Categories", fontfamily="DejaVu Serif")
    ax[0, 1].set_ylabel("Values", fontfamily="DejaVu Serif")
    ax[0, 1].set_title(
        f"{player1.title()} vs {player2.title()} \n (Total Rebounds vs Turnovers)",
        fontfamily="DejaVu Serif",
    )

    ax[0, 1].legend()
    ax[0, 1].grid(
        axis="y",
        linestyle="--",
        alpha=0.6,
    )

    # visualizing a barchart of Blocks vs Steals
    sns.barplot(
        data=defensive_stats_comparison_df,
        x="stats",
        y="values",
        hue="player",
        ax=ax[1, 0],
    )
    # adding labels
    ax[1, 0].set_xlabel("Stat Categories", fontfamily="DejaVu Serif")
    ax[1, 0].set_ylabel("Values", fontfamily="DejaVu Serif")
    ax[1, 0].set_title(
        f"{player1.title()} vs {player2.title()} \n (Steals vs Blocks)",
        fontfamily="DejaVu Serif",
    )

    ax[1, 0].legend()
    ax[1, 0].grid(
        axis="y",
        linestyle="--",
        alpha=0.6,
    )
    # plotting a pie chart
    # Define color palette for distinguishing the two players
    colors = sns.color_palette("icefire", len(labels3) * 2)

    # Create the pie chart
    ax[1, 1].pie(
        combined_stats,
        labels=combined_labels,
        autopct="%1.1f%%",
        startangle=90,
        colors=colors,
    )

    # Title
    ax[1, 1].set_title(
        f"{player1.title()} vs {player2.title()}\n (3-Pointers vs Field Goals)",
        fontfamily="DejaVu Serif",
    )

    # overall layout
    plt.suptitle("NBA 2033/2024 Season Stats", fontfamily="DejaVu Serif", fontsize=15)
    plt.tight_layout()
    plt.show()



player1, player2 = player_prompt()

# check if they exist
if player1 and player2:
    # plots the comparison chart
    plot_stat_comparison_chart(player1, player2)
    print(
        f"The comparison chart for {player1} and {player2} has been \
          successfully visualized!!"
    )
