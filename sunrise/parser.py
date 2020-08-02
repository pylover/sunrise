from sunrise.actions import Calculator
import re

def parse(user_command) :
 
    Regex_Match_List=[
                      ("[-+]?[0-9]+\.?[0-9]*\s*[-+*\/]\s*[-+]?[0-9]+\.?[0-9]*",Calculator()) # Match calqulator
                    ]

    for x in range(len(Regex_Match_List)):
        if (bool(re.search(Regex_Match_List[x][0], user_command))==True): 
		return Regex_Match_List[x][1]

    return not_matched
