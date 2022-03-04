def banner(type):
    try:
        str(type)
        if type.lower() == 'intro': # A 'Not So Elegant' printing method...
            print('''******************************************************************************************
                                BASEBALL STATISTICS
******************************************************************************************

    Welcome to Baseball Statistics. This program reads a file that contains statistics for
    various players from the 2021 season. It will then calculate and print statistics for
    hitters and then for pitchers.\n''')
        elif type.lower() == 'closing':
            print('''******************************************************************************************
                THANKS. SEE YOU AT THE BALLPARK (if the lockout ends).
******************************************************************************************''')
        else:
            print("ERROR: Passed argument <type> must be either 'intro' or 'closing'. It was'", str(type) + "' for function <banner>.")
            return 2
        return 0
    except ValueError as error:
        print("ERROR: Passed argument <type> must be a string for function <banner>.")
        return 1
    except Exception as error:
        print("ERROR: There was an unknown error in function <banner>:", error)
        return 1

def batting_avg(hits, atBats):
    try: int(hits)
    except ValueError: print("ERROR: Passed argument <hits> must be an integer for function <batting_avg>."); return 1
    try: int(atBats)
    except ValueError: print("ERROR: Passed argument <atBats> must be an integer for function <batting_avg>."); return 1
    return round(hits/atBats, 3)
    
def onBase_pct(hits, walks, HbP, atBats, sacrafices):
    sacrafices = 0 # Hard Coded this variable to conform to assignment rubric.
    HbP = 0 # Hard Coded this variable to conform to assignment rubric.
    try: int(hits)
    except ValueError: print("ERROR: Passed argument <hits> must be an integer for function <onBase_pct>."); return 1
    try: int(atBats)
    except ValueError: print("ERROR: Passed argument <atBats> must be an integer for function <onBase_pct>."); return 1
    try: int(walks)
    except ValueError: print("ERROR: Passed argument <walks> must be an integer for function <onBase_pct>."); return 1
    try: int(sacrafices)
    except ValueError: print("ERROR: Passed argument <sacrafices> must be an integer for function <onBase_pct>."); return 1
    try: int(HbP)
    except ValueError: print("ERROR: Passed argument <HbP> must be an integer for function <onBase_pct>."); return 1
    return round((hits+walks+HbP)/(atBats+walks+HbP+sacrafices), 3)

def hr_ratio(atBats, homeRuns):
    try: int(atBats)
    except ValueError: print("ERROR: Passed argument <atBats> must be an integer for function <hr_ratio>."); return 1
    try: int(homeRuns)
    except ValueError: print("ERROR: Passed argument <homeRuns> must be an integer for function <hr_ratio>."); return 1
    return round((atBats/homeRuns), 2)

def slug_pct(hits, doubles, triples, homeRuns, atBats):
    try: int(hits)
    except ValueError: print("ERROR: Passed argument <hits> must be an integer for function <slug_pct>."); return 1
    try: int(doubles)
    except ValueError: print("ERROR: Passed argument <doubles> must be an integer for function <slug_pct>."); return 1
    try: int(triples)
    except ValueError: print("ERROR: Passed argument <triples> must be an integer for function <slug_pct>."); return 1
    try: int(atBats)
    except ValueError: print("ERROR: Passed argument <atBats> must be an integer for function <slug_pct>."); return 1
    try: int(homeRuns)
    except ValueError: print("ERROR: Passed argument <homeRuns> must be an integer for function <slug_pct>."); return 1
    return round(((hits-doubles-triples-homeRuns)+2*doubles+3*triples+4*homeRuns)/atBats, 3)

def isolated_pwr(sluggingPct, battingAvg):
    try: float(sluggingPct)
    except ValueError:  print("ERROR: Passed argument <sluggingPct> must be an integer for function <isolated_pwr>."); return 1
    try: float(battingAvg)
    except ValueError:  print("ERROR: Passed argument <battingAvg> must be an integer for function <isolated_pwr>."); return 1
    return round((sluggingPct-battingAvg), 3)


def onBase_per_slug(onBasePct, sluggingPct):
    try: float(sluggingPct)
    except ValueError:  print("ERROR: Passed argument <sluggingPct> must be an integer for function <onBase_per_slug>."); return 1
    try: float(onBasePct)
    except ValueError:  print("ERROR: Passed argument <onBasePct> must be an integer for function <onBase_per_slug>."); return 1
    return round((onBasePct + sluggingPct), 3)

def earnedRun_avg(earnedRunsAllowed, inningsPitched):
    try: int(earnedRunsAllowed)
    except ValueError: print("ERROR: Passed argument <earnedRunsAllowed> must be an integer for function <earnedRun_avg>."); return 1
    try: int(inningsPitched)
    except ValueError: print("ERROR: Passed argument <inningsPitched> must be an integer for function <earnedRun_avg>."); return 1
    return round((9*(earnedRunsAllowed/inningsPitched)), 2)

def walks_hits_innings_pitched(walks, hits, inningsPitched):
    try: int(walks)
    except ValueError: print("ERROR: Passed argument <earnedRunsAllowed> must be an integer for function <walks_hits_innings_pitched>."); return 1
    try: int(inningsPitched)
    except ValueError: print("ERROR: Passed argument <inningsPitched> must be an integer for function <walks_hits_innings_pitched>."); return 1
    try: int(hits)
    except ValueError: print("ERROR: Passed argument <earnedRunsAllowed> must be an integer for function <walks_hits_innings_pitched>."); return 1
    return round(((walks+hits)/inningsPitched), 2)