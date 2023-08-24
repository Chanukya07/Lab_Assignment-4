class Match:
    def __init__(self, location, team_1, team_2, timing):
        self.location = location
        self.team_1 = team_1
        self.team_2 = team_2
        self.timing = timing


class MatchSearcher:
    def __init__(self, match_list):
        self.match_list = match_list

    def search_by_team(self, team_name):
        matches = []
        for match in self.match_list:
            if match.team_1 == team_name or match.team_2 == team_name:
                matches.append(match)
        return matches

    def search_by_location(self, location):
        matches = []
        for match in self.match_list:
            if match.location == location:
                matches.append(match)
        return matches

    def search_by_timing(self, timing):
        matches = []
        for match in self.match_list:
            if match.timing == timing:
                matches.append(match)
        return matches


def main():
    match_list = [
        Match("Mumbai", "India", "Sri Lanka", "DAY"),
        Match("Delhi", "England", "Australia", "DAY-NIGHT"),
        Match("Chennai", "India", "South Africa", "DAY"),
        Match("Indore", "England", "Sri Lanka", "DAY-NIGHT"),
        Match("Mohali", "Australia", "South Africa", "DAY-NIGHT"),
        Match("Delhi", "India", "Australia", "DAY"),
    ]

    match_searcher = MatchSearcher(match_list)

    while True:
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            team_name = input("Enter the team name: ")
            matches = match_searcher.search_by_team(team_name)
            if matches:
                for match in matches:
                    print(match)
            else:
                print("No matches found for the team")

        elif choice == "2":
            location = input("Enter the location: ")
            matches = match_searcher.search_by_location(location)
            if matches:
                for match in matches:
                    print(match)
            else:
                print("No matches found for the location")

        elif choice == "3":
            timing = input("Enter the timing: ")
            matches = match_searcher.search_by_timing(timing)
            if matches:
                for match in matches:
                    print(match)
            else:
                print("No matches found for the timing")

        elif choice == "4":
            break

        else:
            print("Invalid choice")