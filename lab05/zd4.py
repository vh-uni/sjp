#!/usr/bin/python3

from random import choice

coin_toss_options = ("heads", "tails")


def coin_toss(inp: str):
    coin = choice(coin_toss_options)
    coin_index = coin_toss_options.index(coin)

    if coin == inp or coin.startswith(inp) or int(inp) == coin_index+1:
        print(f"You won! It was {coin}.")
        return True

    print(f"You lost! It was {coin}.")
    return False


def main() -> None:
    games_counter = {"losses": 0, "wins": 0}

    while inp := input(f"Let's flip a coin — heads or tails? (input q to quit): "):
        if inp == "q":
            print("Ending game...")
            break

        if inp in coin_toss_options or any([option.startswith(inp) for option in coin_toss_options]) or int(inp) in range(0, len(coin_toss_options)):
            games_counter[("losses", "wins")[coin_toss(inp)]] += 1
        else:
            print("Wrong input.")
        # TODO: continue?


if __name__ == "__main__":
    main()