from .ElevatorConstants import *
SuitBuildingInfo = (
 ((1, 1), (1, 3), (4, 4), (8, 10), (1,)),  # 0
 ((1, 2), (2, 4), (5, 5), (8, 10), (1, 1.2)),  # 1
 ((1, 3), (3, 5), (6, 6), (8, 10), (1, 1.3, 1.6)),  # 2
 ((2, 3), (4, 6), (7, 7), (8, 10), (1, 1.4, 1.8)),  # 3
 ((2, 4), (5, 7), (8, 8), (8, 10), (1, 1.6, 1.8, 2)),  # 4
 ((3, 4), (6, 8), (9, 9), (10, 12), (1, 1.6, 2, 2.4)),  # 5
 ((3, 5), (7, 9), (10, 10), (10, 14), (1, 1.6, 1.8, 2.2, 2.4)),  # 6
 ((4, 5), (8, 11), (12, 12), (12, 16), (1, 1.8, 2.4, 3, 3.2)),  # 7
 ((5, 5), (9, 12), (13, 13), (14, 20), (1.4, 1.8, 2.6, 3.4, 4)),  # 8
 ((1, 1), (1, 8), (8, 8), (67, 67), (1, 1, 1, 1, 1)),  # 9 VP Round 1
 ((1, 1), (4, 8), (8, 8), (100, 100), (1, 1, 1, 1, 1)),  # 10 VP Round 2 Skelecogs
 ((1, 1), (1, 10), (10, 10), (100, 100), (1, 1, 1, 1, 1)),  # 11 CFO Round 1 NONSKELECOGS ONLY
 ((1, 1), (6, 10), (10, 10), (150, 150), (1, 1, 1, 1, 1)),  # 12 CFO Round 2 SKELECOGS ONLY
 ((1, 1), (8, 12), (12, 12), (275, 275), (1, 1, 1, 1, 1)),  # 13 CJ Round 1
 ((1, 1), (9, 14), (14, 14), (260, 260), (1, 1, 1, 1, 1), (0,)),  # 14 CEO Round 1
 ((1, 1), (1, 5), (5, 5), (33, 33), (1, 1, 1, 1, 1)),  # 15 Storm Sellbot Round 1
 ((1, 1), (4, 5), (5, 5), (50, 50), (1, 1, 1, 1, 1))  # 16 Storm Sellbot Round 2
)
SUIT_BLDG_INFO_FLOORS = 0
SUIT_BLDG_INFO_SUIT_LVLS = 1
SUIT_BLDG_INFO_BOSS_LVLS = 2
SUIT_BLDG_INFO_LVL_POOL = 3
SUIT_BLDG_INFO_LVL_POOL_MULTS = 4
SUIT_BLDG_INFO_REVIVES = 5
SUIT_BLDG_INFO_IMMUNE = 6
VICTORY_RUN_TIME = ElevatorData[ELEVATOR_NORMAL]['openTime'] + TOON_VICTORY_EXIT_TIME
TO_TOON_BLDG_TIME = 8
VICTORY_SEQUENCE_TIME = VICTORY_RUN_TIME + TO_TOON_BLDG_TIME
CLEAR_OUT_TOON_BLDG_TIME = 4
TO_SUIT_BLDG_TIME = 8
NUM_TOONS_TO_COGS_RATIO = {1: 0.2,
                           2: 0.35,
                           3: 0.45,
                           4: 0.6,
                           5: 0.65,
                           6: 0.75,
                           7: 0.9,
                           8: 1
                           }
