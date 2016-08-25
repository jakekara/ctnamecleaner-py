# CT Name Cleaner

Resolve village and coloquial Connecticut town names, as well as common
misspellings of Connecticut town names to their official town names.

This is based on an R package of the same name by my colleague Andrew Ba Tran.

This installs a command line script, ctclean,  as well as a library 

by Jake Kara, jake@jakekara.com

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

See the demo/ folder in this repo for an example of translating an entire
column with the Lookup.clean_dataframe() method. It uses pandas'
DataFrame.join() method, so it's faster than using the Lookup.cean() method
and applying it with a lambda function yourself.