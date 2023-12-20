import random
    
N_SONGS = 7

MAX_POSITIVES = 3
MAX_NEGATIVES = 2

TOTAL_POSITIVES = 7
TOTAL_NEGATIVES = 3

TOTAL_VOTES = TOTAL_POSITIVES - TOTAL_NEGATIVES

def is_result_valid(results):
    if sum(results.values()) != TOTAL_VOTES:
        return False

    if TOTAL_POSITIVES != sum([x for x in results.values() if x > 0]):
        return False

    if (0 - TOTAL_NEGATIVES) != sum([x for x in results.values() if x < 0]):
        return False
    
    return True

def main():
    posible_values = list(range(0 - MAX_NEGATIVES, MAX_POSITIVES + 1))
    songs = list(range(1, N_SONGS + 1))
    results = {}

    while True:
        for song in songs:
            results[song] = random.choice(posible_values)

        if (is_result_valid(results)):
            break

    for song in results:
        print(str(song) + ":\t" + str(results[song]))

if __name__ == "__main__":
    main()
