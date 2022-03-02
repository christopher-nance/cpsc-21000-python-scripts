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
            THANKS. SEE YOU AT THE BALLPARK (if they ever decide to play).
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
    print("Calculating Batting Average...")
    try: int(hits)
    except ValueError: print("ERROR: Passed argument <hits> must be an integer for function <batting_avg>."); return 1
    try: int(atBats)
    except ValueError: print("ERROR: Passed argument <atBats> must be an integer for function <batting_avg>."); return 1
    return (hits/atBats)
    
def onBase_pct(hits, walks, HbP, atBats, sacrafices):
    print("Calculating On Base Percentage...")
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
    return ((hits+walks+HbP)/(atBats+walks+HbP+sacrafices))

def hr_ratio(atBats, homeRuns):
    print("Calculating Home Run Ratio...")
    try: int(atBats)
    except ValueError: print("ERROR: Passed argument <atBats> must be an integer for function <hr_ratio>."); return 1
    try: int(homeRuns)
    except ValueError: print("ERROR: Passed argument <homeRuns> must be an integer for function <hr_ratio>."); return 1
    return (atBats/homeRuns)

def slug_pct(hits, doubles, triples, homeRuns, atBats):
    print("Calculating Slugging Percentage...")
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
    return ((hits+2*doubles+3*triples+4*homeRuns)/atBats)

def isolated_pwr(sluggingPct, battingAvg):
    print("Calculating Isolated Power...")
    try: float(sluggingPct)
    except ValueError:  print("ERROR: Passed argument <sluggingPct> must be an integer for function <isolated_pwr>."); return 1
    try: float(battingAvg)
    except ValueError:  print("ERROR: Passed argument <battingAvg> must be an integer for function <isolated_pwr>."); return 1
    return (sluggingPct-battingAvg)


def onBase_per_slug(onBasePct, sluggingPct):
    print("Calculating On Base per Slugging...")
    try: float(sluggingPct)
    except ValueError:  print("ERROR: Passed argument <sluggingPct> must be an integer for function <onBase_per_slug>."); return 1
    try: float(onBasePct)
    except ValueError:  print("ERROR: Passed argument <onBasePct> must be an integer for function <onBase_per_slug>."); return 1
    return (onBasePct + sluggingPct)

def earnedRun_avg(earnedRunsAllowed, inningsPitched):
    print("Calculating Earned Run Average...")
    try: int(earnedRunsAllowed)
    except ValueError: print("ERROR: Passed argument <earnedRunsAllowed> must be an integer for function <earnedRun_avg>."); return 1
    try: int(inningsPitched)
    except ValueError: print("ERROR: Passed argument <inningsPitched> must be an integer for function <earnedRun_avg>."); return 1
    return (9*(earnedRunsAllowed/inningsPitched))

def walks_hits_innings_pitched(walks, hits, inningsPitched):
    print("Calculating Walks & Hits per Innings Pitched...")
    try: int(walks)
    except ValueError: print("ERROR: Passed argument <earnedRunsAllowed> must be an integer for function <walks_hits_innings_pitched>."); return 1
    try: int(inningsPitched)
    except ValueError: print("ERROR: Passed argument <inningsPitched> must be an integer for function <walks_hits_innings_pitched>."); return 1
    try: int(hits)
    except ValueError: print("ERROR: Passed argument <earnedRunsAllowed> must be an integer for function <walks_hits_innings_pitched>."); return 1
    return ((walks+hits)/inningsPitched)