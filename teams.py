from enum import Enum


class Team(Enum):  # source: https://github.com/jaebradley/basketball_reference_web_scraper
    ATLANTA_HAWKS = "ATLANTA HAWKS"
    BOSTON_CELTICS = "BOSTON CELTICS"
    BROOKLYN_NETS = "BROOKLYN NETS"
    CHARLOTTE_HORNETS = "CHARLOTTE HORNETS"
    CHICAGO_BULLS = "CHICAGO BULLS"
    CLEVELAND_CAVALIERS = "CLEVELAND CAVALIERS"
    DALLAS_MAVERICKS = "DALLAS MAVERICKS"
    DENVER_NUGGETS = "DENVER NUGGETS"
    DETROIT_PISTONS = "DETROIT PISTONS"
    GOLDEN_STATE_WARRIORS = "GOLDEN STATE WARRIORS"
    HOUSTON_ROCKETS = "HOUSTON ROCKETS"
    INDIANA_PACERS = "INDIANA PACERS"
    LOS_ANGELES_CLIPPERS = "LOS ANGELES CLIPPERS"
    LOS_ANGELES_LAKERS = "LOS ANGELES LAKERS"
    MEMPHIS_GRIZZLIES = "MEMPHIS GRIZZLIES"
    MIAMI_HEAT = "MIAMI HEAT"
    MILWAUKEE_BUCKS = "MILWAUKEE BUCKS"
    MINNESOTA_TIMBERWOLVES = "MINNESOTA TIMBERWOLVES"
    NEW_ORLEANS_PELICANS = "NEW ORLEANS PELICANS"
    NEW_YORK_KNICKS = "NEW YORK KNICKS"
    OKLAHOMA_CITY_THUNDER = "OKLAHOMA CITY THUNDER"
    ORLANDO_MAGIC = "ORLANDO MAGIC"
    PHILADELPHIA_76ERS = "PHILADELPHIA 76ERS"
    PHOENIX_SUNS = "PHOENIX SUNS"
    PORTLAND_TRAIL_BLAZERS = "PORTLAND TRAIL BLAZERS"
    SACRAMENTO_KINGS = "SACRAMENTO KINGS"
    SAN_ANTONIO_SPURS = "SAN ANTONIO SPURS"
    TORONTO_RAPTORS = "TORONTO RAPTORS"
    UTAH_JAZZ = "UTAH JAZZ"
    WASHINGTON_WIZARDS = "WASHINGTON WIZARDS"

    # DEPRECATED TEAMS
    CHARLOTTE_BOBCATS = "CHARLOTTE BOBCATS"
    NEW_JERSEY_NETS = "NEW JERSEY NETS"
    NEW_ORLEANS_HORNETS = "NEW ORLEANS HORNETS"
    NEW_ORLEANS_OKLAHOMA_CITY_HORNETS = "NEW ORLEANS/OKLAHOMA CITY HORNETS"
    SEATTLE_SUPERSONICS = "SEATTLE SUPERSONICS"
    VANCOUVER_GRIZZLIES = "VANCOUVER GRIZZLIES"


TEAM_NAME_TO_TEAM = {
    "ATLANTA_HAWKS": Team.ATLANTA_HAWKS,
    "BOSTON_CELTICS": Team.BOSTON_CELTICS,
    "BROOKLYN_NETS": Team.BROOKLYN_NETS,
    "CHARLOTTE_HORNETS": Team.CHARLOTTE_HORNETS,
    "CHICAGO_BULLS": Team.CHICAGO_BULLS,
    "CLEVELAND_CAVALIERS": Team.CLEVELAND_CAVALIERS,
    "DALLAS_MAVERICKS": Team.DALLAS_MAVERICKS,
    "DENVER_NUGGETS": Team.DENVER_NUGGETS,
    "DETROIT_PISTONS": Team.DETROIT_PISTONS,
    "GOLDEN_STATE_WARRIORS": Team.GOLDEN_STATE_WARRIORS,
    "HOUSTON_ROCKETS": Team.HOUSTON_ROCKETS,
    "INDIANA_PACERS": Team.INDIANA_PACERS,
    "LOS_ANGELES_CLIPPERS": Team.LOS_ANGELES_CLIPPERS,
    "LOS_ANGELES_LAKERS": Team.LOS_ANGELES_LAKERS,
    "MEMPHIS_GRIZZLIES": Team.MEMPHIS_GRIZZLIES,
    "MIAMI_HEAT": Team.MIAMI_HEAT,
    "MILWAUKEE_BUCKS": Team.MILWAUKEE_BUCKS,
    "MINNESOTA_TIMBERWOLVES": Team.MINNESOTA_TIMBERWOLVES,
    "NEW_ORLEANS_PELICANS": Team.NEW_ORLEANS_PELICANS,
    "NEW_YORK_KNICKS": Team.NEW_YORK_KNICKS,
    "OKLAHOMA_CITY_THUNDER": Team.OKLAHOMA_CITY_THUNDER,
    "ORLANDO_MAGIC": Team.ORLANDO_MAGIC,
    "PHILADELPHIA_76ERS": Team.PHILADELPHIA_76ERS,
    "PHOENIX_SUNS": Team.PHOENIX_SUNS,
    "PORTLAND_TRAIL_BLAZERS": Team.PORTLAND_TRAIL_BLAZERS,
    "SACRAMENTO_KINGS": Team.SACRAMENTO_KINGS,
    "SAN_ANTONIO_SPURS": Team.SAN_ANTONIO_SPURS,
    "TORONTO_RAPTORS": Team.TORONTO_RAPTORS,
    "UTAH_JAZZ": Team.UTAH_JAZZ,
    "WASHINGTON_WIZARDS": Team.WASHINGTON_WIZARDS,

    # DEPRECATED TEAMS
    "CHARLOTTE_BOBCATS": Team.CHARLOTTE_BOBCATS,
    "NEW_JERSEY_NETS": Team.NEW_JERSEY_NETS,
    "NEW_ORLEANS_HORNETS": Team.NEW_ORLEANS_HORNETS,
    "NEW_ORLEANS_OKLAHOMA_CITY_HORNETS": Team.NEW_ORLEANS_OKLAHOMA_CITY_HORNETS,
    "SEATTLE_SUPERSONICS": Team.SEATTLE_SUPERSONICS,
    "VANCOUVER_GRIZZLIES": Team.VANCOUVER_GRIZZLIES,
}

TEAM_TO_TEAM_ABBREVIATIONS = {
    Team.ATLANTA_HAWKS: 'ATL',
    Team.BOSTON_CELTICS: 'BOS',
    Team.BROOKLYN_NETS: 'BRK',
    Team.CHICAGO_BULLS: 'CHI',
    Team.CHARLOTTE_HORNETS: 'CHO',
    Team.CLEVELAND_CAVALIERS: 'CLE',
    Team.DALLAS_MAVERICKS: 'DAL',
    Team.DENVER_NUGGETS: 'DEN',
    Team.DETROIT_PISTONS: 'DET',
    Team.GOLDEN_STATE_WARRIORS: 'GSW',
    Team.HOUSTON_ROCKETS: 'HOU',
    Team.INDIANA_PACERS: 'IND',
    Team.LOS_ANGELES_CLIPPERS: 'LAC',
    Team.LOS_ANGELES_LAKERS: 'LAL',
    Team.MEMPHIS_GRIZZLIES: 'MEM',
    Team.MIAMI_HEAT: 'MIA',
    Team.MILWAUKEE_BUCKS: 'MIL',
    Team.MINNESOTA_TIMBERWOLVES: 'MIN',
    Team.NEW_ORLEANS_PELICANS: 'NOP',
    Team.NEW_YORK_KNICKS: 'NYK',
    Team.OKLAHOMA_CITY_THUNDER: 'OKC',
    Team.ORLANDO_MAGIC: 'ORL',
    Team.PHILADELPHIA_76ERS: 'PHI',
    Team.PHOENIX_SUNS: 'PHO',
    Team.PORTLAND_TRAIL_BLAZERS: 'POR',
    Team.SACRAMENTO_KINGS: 'SAC',
    Team.SAN_ANTONIO_SPURS: 'SAS',
    Team.TORONTO_RAPTORS: 'TOR',
    Team.UTAH_JAZZ: 'UTA',
    Team.WASHINGTON_WIZARDS: 'WAS',

    # DEPRECATED TEAMS
    Team.NEW_JERSEY_NETS: 'NJN',
    Team.NEW_ORLEANS_HORNETS: 'NOH',
    Team.NEW_ORLEANS_OKLAHOMA_CITY_HORNETS: 'NOK',
    Team.CHARLOTTE_BOBCATS: 'CHA',
    Team.SEATTLE_SUPERSONICS: 'SEA',
    Team.VANCOUVER_GRIZZLIES: 'VAN',
}
