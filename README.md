# CT Name Cleaner

Resolve village and coloquial Connecticut town names, as well as common
misspellings of Connecticut town names to their official town names.

This is based on an R package of the same name by my colleague Andrew Ba Tran.

This installs a command line script, ctclean,  as well as a library
particularly meant for use within Jupyter notebooks.

by Jake Kara, jake@jakekara.com

### Latest version

0.10.1
     
### Installation

    pip install ctnamecleaner

### Command line util

Usage:

	$ ctclean New\ Preston
	WASHINGTON
	$ ctclean "New Preston"
	WASHINGTON

When nothing is found, return None:

	$ ctclean NotGonnaFindItsVille
	None

Set a custom value to return on error with the --error or -e flag:

    $ ctclean NotGonnaFindItsVille --error "Ruh Roh"
    Ruh Roh

### Use with Pandas dataframes

See HELP.txt in this directory and the Notebook in the demo/ folder in this
repo for an example of translating an entire column with the clean,
clean_col and the clean_dataframe() method. clean_dataframe uses pandas'
DataFrame.join() method, so it's faster than using the cean() method
and applying it with a lambda function yourself. 

### Extending with other data

Not in CT? Want to map other things? Just make a spreadsheet and put it
anywhere, online or locally, that Pandas .read_csv() can open, and then use
the constructor to customize the lookup class.

     >>> l = lookup.Lookup(csv_url="http://path/to/your/sheet",
			   raw_name_col="something",
			   clean_name_col="something_else")

### Contents of HELP.txt

Below this point is auto documentation from the lookup class generated from
help.py:

Help on module ctlookup.lookup in ctlookup:

NAME
    ctlookup.lookup - Main module for CT Name Cleaner

FILE
    /Applications/MAMP/htdocs/tdev/pyctnamecleaner/package/ctlookup/lookup.py

CLASSES
    Lookup
    
    class Lookup
     |  Lookup class for CT place names, or any other DF for that matter
     |  
     |  Methods defined here:
     |  
     |  __init__(self, raw_name_col='name', clean_name_col='real.town.name', csv_url=None, use_inet_csv=False)
     |      Constructor for Lookup 
     |      
     |      No need to use parameters unless you are specifying a different
     |      source URL.
     |      
     |      Parameters
     |      -----------
     |      raw_name_col : string, optional
     |          The name of the column with input names, like "New Preston"
     |      
     |          Only use if you're using a different source spreadsheet.
     |      
     |      clean_name_col : string, optional
     |          The name of the column with out names, like "Washington"
     |      
     |          Only use if you're using a different source spreadsheet.
     |      
     |      csv_url : string, optional
     |          A valid local file or remote url to use as an alternative
     |          source spreadsheet.
     |      
     |      use_inet_csv : boolean, optional
     |          Force a reload of the spreadsheet from the web to reflect any
     |          new additions since it was bundled with this python package.
     |      
     |          Defaults to False. The list doesn't change too much anymore.
     |  
     |  clean(self, raw_name, error=None)
     |      Get a clean place name (e.g. input "New Preston" and get
     |      "Washington")
     |      
     |      Parameters
     |      ----------
     |      raw_name : string
     |          The input name of the place, such as a village or a
     |          common misspelling of a town name
     |      
     |      error : obj, optional
     |          The default to return if no match is found
     |      
     |          Defaults to None
     |      
     |      Returns
     |      -------
     |      String or the value of None (or anything specified with the error
     |      parameter) if no match is found
     |  
     |  clean_col(self, series, error=None)
     |      Clean a Pandas Series of place names
     |      
     |      Parameters
     |      ----------
     |      series : Pandas Series
     |          A series containing place names that need to be cleaned
     |      
     |      error : obj, optional
     |          Value to use if no match is found for a given place.
     |      
     |          Defaults to None
     |      
     |      Notes
     |      -----
     |      Meant as a less opinionated version of clean_dataframe
     |  
     |  clean_dataframe(self, df, town_col, error=None)
     |      Clean an entire column of place names
     |      
     |      Parameters
     |      ----------
     |      
     |      df : Pandas DataFrame
     |          Dataframe containing to clean
     |      
     |      town_col : valid column label
     |          Label of column containing town names to clean
     |      
     |      error : obj, optional
     |          Default value to use when no match is found.
     |      
     |          Defaults to None
     |      
     |      Notes
     |      -----
     |      I plan to deprecate this but leave it in place for
     |      backward-compatibility. Use clean_col instead.


