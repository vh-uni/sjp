#!/usr/bin/python3

from random import choice

coin_toss_options = ("heads", "tails")


def coin_toss(inp: str) -> bool:
    coin = choice(coin_toss_options)
    coin_index = coin_toss_options.index(coin)

    try:
        if coin == inp or coin.startswith(inp) or int(inp) == coin_index+1:
            print(f"You won! It was {coin}.")
            return True
    except:
        pass

    print(f"You lost! It was {coin}.")
    return False


def main() -> None:
    games_counter = {"losses": 0, "wins": 0}

    while inp := input(f"Let's flip a coin — heads or tails? (input q to quit): "):
        if inp == "q":
            print("Ending game...")
            print(f"You won {games_counter['wins']} times and lost {games_counter['losses']} times.")
            break

        try:
            if inp in coin_toss_options or any([option.startswith(inp) for option in coin_toss_options]) or int(inp) in range(1, len(coin_toss_options)+1):
                games_counter[("losses", "wins")[coin_toss(inp)]] += 1
            else:
                print("Wrong input.")
        except:
            pass


if __name__ == "__main__":
    main()