def matches_and_results(clubA, clubB):
    results = []
    number_of_match = 0
    while True:
        match = [None] * (number_of_match + 1) * 2
        print(f"Match {number_of_match+1}\t: ", end="")
        match[number_of_match], match[number_of_match + 1] = input().split()
        match[number_of_match] = int(match[number_of_match])
        match[number_of_match + 1] = int(match[number_of_match + 1])
        if match[number_of_match] < 0 or match[number_of_match + 1] < 0:
            break
        elif match[number_of_match] > match[number_of_match + 1]:
            results.append(clubA)
        elif match[number_of_match] < match[number_of_match + 1]:
            results.append(clubB)
        elif match[number_of_match] == match[number_of_match + 1]:
            results.append("Draw")
        number_of_match = number_of_match + 1

    for number_of_match in range(0, len(results)):
        print(f"Result {number_of_match+1} : {results[number_of_match]}")
    print("The Competitions is Over")
