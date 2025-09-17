from datetime import datetime
import pandas as pd

start_date = datetime(2023, 1, 1)
end_date = datetime(2027, 1, 1)

date_range = pd.date_range(start_date, end_date)

date_df = pd.DataFrame(date_range, columns=["Date"])

date_df["year"] = date_df["Date"].dt.year
date_df["month"] = date_df["Date"].dt.month
date_df["day"] = date_df["Date"].dt.day
date_df["day_of_week"] = date_df["Date"].dt.dayofweek + 1
date_df["is_weekend"] = date_df["day_of_week"].isin([6.7])

print(date_df)

date_df.to_csv("date_dimension.csv", index=False)