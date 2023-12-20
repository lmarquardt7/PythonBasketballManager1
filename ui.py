import db
from objects import Player, Lineup
from datetime import date, datetime

POSITIONS = ("PG", "SG", "SF", "PF", "C")

def add_player(players):    
    first_name = input("First name: ").title()
    last_name = input("Last name: ").title()

    position = get_player_position()

    points = get_points()
    rebounds = get_rebounds()
    assists = get_assists()
    blocks = get_blocks()
    steals = get_steals()
    turnovers = get_turnovers()
    three_pointers_made = get_three_pointers_made()
    free_throws_made = get_free_throws_made()

    starting_order = players.count + 1

    player = Player(first_name, last_name, position, points, rebounds, assists, blocks, steals, turnovers, three_pointers_made, free_throws_made, starting_order)
    players.add(player)
    db.add_player(player)
    print(f"{player.fullName} was added.\n")

def get_player_position():
    while True:
        position = input("Position: ").upper()
        if position in POSITIONS:
            return position
        else:
            print("Invalid position. Try again.")
            display_positions()

def get_points():
    while True:
        try:
            points = int(input("Points: "))
        except ValueError:
            print("Invalid integer. Try again.")
            continue

        if points < 0 or points > 100000:    
            print("Invalid entry. Must be from 0 to 100,000.")
        else:
            return points      

def get_rebounds():
    while True:
        try:
            rebounds = int(input("Rebounds: "))
        except ValueError:
            print("Invalid integer. Try again.")
            continue

        if rebounds < 0 or rebounds > 100000:        
            print(f"Invalid entry. Must be from 0 to 100,000.")
        else:
            return rebounds
        
def get_assists():
    while True:
        try:
            assists = int(input("Assists: "))
        except ValueError:
            print("Invalid integer. Try again.")
            continue

        if assists < 0 or assists > 100000:        
            print(f"Invalid entry. Must be from 0 to 100,000.")
        else:
            return assists
        
def get_blocks():
    while True:
        try:
            blocks = int(input("Blocks: "))
        except ValueError:
            print("Invalid integer. Try again.")
            continue

        if blocks < 0 or blocks > 100000:        
            print(f"Invalid entry. Must be from 0 to 100,000.")
        else:
            return blocks

def get_steals():
    while True:
        try:
            steals = int(input("Steals: "))
        except ValueError:
            print("Invalid integer. Try again.")
            continue

        if steals < 0 or steals > 100000:        
            print(f"Invalid entry. Must be from 0 to 100,000.")
        else:
            return steals
        
def get_turnovers():
    while True:
        try:
            turnovers = int(input("Turnovers: "))
        except ValueError:
            print("Invalid integer. Try again.")
            continue

        if turnovers < 0 or turnovers > 100000:        
            print(f"Invalid entry. Must be from 0 to 100,000.")
        else:
            return turnovers

def get_three_pointers_made():
    while True:
        try:
            threes = int(input("Three Pointers Made: "))
        except ValueError:
            print("Invalid integer. Try again.")
            continue

        if threes < 0 or threes > 100000:        
            print(f"Invalid entry. Must be from 0 to 100,000.")
        else:
            return threes
        
def get_free_throws_made():
    while True:
        try:
            frees = int(input("Free Throws Made: "))
        except ValueError:
            print("Invalid integer. Try again.")
            continue

        if frees < 0 or frees > 100000:        
            print(f"Invalid entry. Must be from 0 to 100,000.")
        else:
            return frees

def get_lineup_number(players, prompt):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Invalid integer. Please try again.")
            continue

        if number < 1 or number > players.count:
            print("Invalid player number. Please try again.")
        else:
            return number

def delete_player(players):
    number = get_lineup_number(players, "Number: ")
    player = players.remove(number)
    db.delete_player(player)
    db.update_starting_order(players)
    print(f"{player.fullName} was deleted.\n")

def move_player(players):
    old_number = get_lineup_number(players, "Current lineup number: ")
    player = players.get(old_number)
    print(f"{player.fullName} was selected.")
    new_number = get_lineup_number(players, "New lineup number: ")

    players.move(old_number, new_number)
    db.update_starting_order(players)
    print(f"{player.fullName} was moved.\n")

def edit_player_position(players):
    number = get_lineup_number(players, "Lineup number: ")
    player = players.get(number)
    print(f"You selected {player.fullName} POS={player.position}")
    
    player.position = get_player_position()
    db.update_player(player)
    print(f"{player.fullName} was updated.\n")

def edit_player_stats(players):
    number = get_lineup_number(players, "Lineup number: ")
    player = players.get(number)
    print(f"You selected {player.fullName} Points={player.points} Rebounds={player.rebounds} Assists={player.assists} Blocks={player.blocks} Steals={player.steals} Turnovers={player.turnovers} 3-pointers={player.threePointersMade} Free-Throws={player.freeThrowsMade}")
    
    player.points = get_points()
    player.rebounds = get_rebounds()
    player.assists = get_assists()
    player.blocks = get_blocks()
    player.steals = get_steals()
    player.turnovers = get_turnovers()
    player.threePointersMade = get_three_pointers_made()
    player.freeThrowsMade = get_free_throws_made()

    db.update_player(player)
    print(f"{player.fullName} was updated.\n")

def display_lineup(players):
    if players == None:
        print("There are currently no players in the lineup.")        
    else:
        print(f"{'':3}{'Player':25}{'POS':6}{'Points':>10}{'Rebounds':>10}{'Assists':>10}{'Blocks':>10}{'Steals':>10}{'Turnovers':>12}{'3-Pointers':>12}{'Free-Throws ':>14}")
        print("-" * 118)
        for player in players:
            print(f"{player.startingOrder:<3d}{player.fullName:25}{player.position:6}" + \
                  f"{player.points:10d}{player.rebounds:10d}{player.assists:10d}{player.blocks:10d}{player.steals:10d}{player.turnovers:10d}{player.threePointersMade:10d}{player.freeThrowsMade:10d}")
    print()   

def display_separator():
    print()
    print("=" * 118)
    print()

def display_title():
    print("                                           Basketball Team Manager                             ")

def display_dates():
    print()

    date_format = "%Y-%m-%d"
    now = datetime.now()    
    current_date = datetime(now.year, now.month, now.day)
    print(f"CURRENT DATE:    {current_date.strftime(date_format)}")

    while True:
        game_date_str = input("GAME DATE:       ")
        if game_date_str == "":
            print()
            return

        try:
            game_date = datetime.strptime(game_date_str, date_format)
        except ValueError:
            print("Incorrect date format. Please try again.")
            continue
        
        time_span = game_date - current_date

        if time_span.days > -1:
            print()
            print(f"DAYS UNTIL GAME: {time_span.days}")
        print()
        break  

def display_menu():
    print("MENU OPTIONS")
    print("1 – Display lineup")
    print("2 – Add player")
    print("3 – Remove player")
    print("4 – Move player")
    print("5 – Edit player position")
    print("6 – Edit player stats")
    print("7 - Display Menu")
    print("8 - Exit program")
    print()

def display_positions():
    print("POSITIONS")
    print(", ".join(POSITIONS))

def main():
    display_separator()
    display_title()
    display_dates()
    display_menu()
    display_positions()

    db.connect()
    players = db.get_players()
    if players == None:
        players = Lineup()         

    display_separator()
    
    while True:
        try:
            option = int(input("Menu option: "))
            print()
        except ValueError:
            option = -1
            
        if option == 1:
            display_lineup(players)
        elif option == 2:
            add_player(players)
            players = db.get_players()
        elif option == 3:
            delete_player(players)
        elif option == 4:
            move_player(players)
        elif option == 5:
            edit_player_position(players)
        elif option == 6:
            edit_player_stats(players)
        elif option == 7:
            display_menu()
        elif option == 8:
            db.close()
            print("Bye!")
            break
        else:
            print("Not a valid option. Please try again.\n")
            display_menu()

if __name__ == "__main__":
    main()
