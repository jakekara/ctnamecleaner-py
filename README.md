# CT Name Cleaner

Resolve village and coloquial Connecticut town names, as well as common
misspellings of Connecticut town names to their official town names.

This is based on an R package of the same name by my colleague Andrew Ba Tran.

This installs a command line script, ctclean,  as well as a library 

by Jake Kara, jake@jakekara.com

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