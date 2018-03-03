""" Update the package data from google sheets URL """

from ctlookup.config import SHEET_URL
import pandas as pd

LOCAL_COPY = "ctlookup/data/ctnamecleaner.csv"

df = pd.read_csv(SHEET_URL)
df.to_csv(LOCAL_COPY, index=False)

print ("Updated sheet has " + str(len(df)) + " rows.")


