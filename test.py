from main import game

import cProfile
import pstats

if __name__ == '__main__':
    with cProfile.Profile() as pr:
        game(2)

    stats = pstats.Stats(pr)

    stats.sort_stats(pstats.SortKey.TIME)

    stats.dump_stats('profile.prof')
