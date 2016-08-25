import pandas as pd

class Lookup:
    # Default CSV for resolving CT place names
    def __init__(self, raw_name_col="name", clean_name_col="real.town.name",
                 csv_url="https://docs.google.com/spreadsheets/d/1WqZIGk2AkHXKYvd4uXy5a2nwyg529e7mMU5610Ale0g/pub?gid=0&single=true&output=csv"):
        self.csv_url = csv_url
        self.lookup_table = pd.read_csv(self.csv_url)
        self.raw_name_col=raw_name_col
        
    def clean(self, raw_name,
              raw_name_col="name",
              clean_name_col="real.town.name"):
        results = self.lookup_table[self.lookup_table[self.raw_name_col]\
                                    .str.upper() == raw_name.upper()]
        if len(results.index) < 1:
            raise Exception("LookupError: No results found")
        elif len(results.index) > 1:
            raise Exception("LookupError: More than one result found")
        else:
            return results[clean_name_col].unique()[0]

    def clean_dataframe(df, town_col):
         return df.join(lookup_table,rsuffix="_clean")["real.town.name_clean"]
