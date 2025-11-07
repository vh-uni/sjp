#!/usr/bin/python3

from random import choice

rps_options = ("rock", "paper", "scissors")
rps_beaten_by = {"rock": "paper", "paper": "scissors", "scissors": "rock"}


def rock_paper_scissors(inp: str) -> int:
    rps_choice = choice(rps_options)
    winner_option = rps_beaten_by[rps_choice]

    if inp.isdigit():
        inp = rps_options[int(inp)-1]

    if inp not in rps_options:
        for option in rps_options:
            if option.startswith(inp):
                inp = option
                break

    if inp == rps_choice:
        print(f"It's a draw! You both chose {inp}.")
        return 2

    if winner_option == inp:
        print(f"You won! {inp.title()} beat {rps_choice}.")
        return 1

    print(f"You lost! {inp.title()} got beaten by {rps_choice}.")
    return 0


def main() -> None:
    games_counter = {"losses": 0, "wins": 0, "draws": 0}

    while inp := input(f"Let's play Rock Paper Scissors? (input q to quit): ").strip():
        if inp == "q":
            print("Ending game...")
            print(f"Here are your results: {games_counter['wins']} wins, {games_counter['losses']} losses and {games_counter['draws']} draws.")
            break

        try:
            if inp in rps_options or any([option.startswith(inp) for option in rps_options]) or int(inp) in range(1, len(rps_options) + 1):
                games_counter[list(games_counter.keys())[rock_paper_scissors(inp)]] += 1
            else:
                print("Wrong input.")
        except:
            print("Wrong input.")


if __name__ == "__main__":
    main()