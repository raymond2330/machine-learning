import pandas as pd

# Example CSV-like data
data = {
    "Time": [
        "09:01:02", "09:01:03", "09:01:04", "09:01:05", "09:01:06", 
        "09:01:07", "09:01:08", "09:01:09", "09:01:10", "09:01:11", 
        "09:01:12", "09:01:13", "09:01:14", "09:01:15", "09:01:16", 
        "09:01:17", "09:01:18", "09:01:19", "09:01:20", "09:01:21", 
        "09:01:22", "09:01:23", "09:01:24", "09:01:25", "09:01:26", 
        "09:01:27", "09:01:28", "09:01:29", "09:01:30", "09:01:31", 
        "09:01:32", "09:01:33", "09:01:34", "09:01:35", "09:01:36", 
        "09:01:37", "09:01:38", "09:01:39", "09:01:40", "09:01:41", 
        "09:01:42", "09:01:43", "09:01:44", "09:01:45", "09:01:46", 
        "09:01:47", "09:01:48"
    ],
    "E Value": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "H Value": [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

df = pd.DataFrame(data)

# Compute logical OR (E Value or H Value)
df["Active"] = df["E Value"] | df["H Value"]

results = []
streak_start = None

for i, row in df.iterrows():
    if row["Active"]:
        if streak_start is None:
            streak_start = row["Time"]
    else:
        if streak_start is not None:
            streak_end = df.loc[i - 1, "Time"]
            streak_length = i - df.index[df["Time"] == streak_start][0]
            results.append([f"{streak_start} - {streak_end}", streak_length])
            streak_start = None

# Final streak
if streak_start is not None:
    streak_end = df.iloc[-1]["Time"]
    streak_length = len(df) - df.index[df["Time"] == streak_start][0]
    results.append([f"{streak_start} - {streak_end}", streak_length])

# Convert results to DataFrame
output_df = pd.DataFrame(results, columns=["Time", "Total"])
print(output_df)
