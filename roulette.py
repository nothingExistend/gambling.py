import random

def expl():
    expl = ["colors (red and black)", "specific numbers (0 - 36), (0 as green)", "a range of numbers (1 - 12, 13 - 24, 25 - 36), (input as 1, 2 or 3)", "more features following soon"]

    def title() :
        print(r"      ___           ___           ___           ___           ___                   ___           ___      ")
        print(r"     /\  \         /\  \         /\__\         /\  \         /\__\      ___        /\__\         /\  \     ")
        print(r"    /::\  \       /::\  \       /::|  |       /::\  \       /:/  /     /\  \      /::|  |       /::\  \    ")
        print(r"   /:/\:\  \     /:/\:\  \     /:|:|  |      /:/\:\  \     /:/  /      \:\  \    /:|:|  |      /:/\:\  \   ")
        print(r"  /:/  \:\  \   /::\~\:\  \   /:/|:|__|__   /::\~\:\__\   /:/  /       /::\__\  /:/|:|  |__   /:/  \:\  \  ")
        print(r" /:/__/_\:\__\ /:/\:\ \:\__\ /:/ |::::\__\ /:/\:\ \:|__| /:/__/     __/:/\/__/ /:/ |:| /\__\ /:/__/_\:\__\ ")
        print(r" \:\  /\ \/__/ \/__\:\/:/  / \/__/~~/:/  / \:\~\:\/:/  / \:\  \    /\/:/  /    \/__|:|/:/  / \:\  /\ \/__/ ")
        print(r"  \:\ \:\__\        \::/  /        /:/  /   \:\ \::/  /   \:\  \   \::/__/         |:/:/  /   \:\ \:\__\   ")
        print(r"   \:\/:/  /        /:/  /        /:/  /     \:\/:/  /     \:\  \   \:\__\         |::/  /     \:\/:/  /   ")
        print(r"    \::/  /        /:/  /        /:/  /       \::/__/       \:\__\   \/__/         /:/  /       \::/  /    ")
        print(r"     \/__/         \/__/         \/__/         ~~            \/__/                 \/__/         \/__/     ")
        print()
        print()

    title()

    print("RULESET:")
    print("  You can bet on:")

    for i in expl :
        print("   -  " + i)

    print()
    print("place your bets now")
    print()

def main():
    # INPUTS
    bets = ["" , ]

    b_col = input("color: ")
    if b_col == "":


    _RANDOM = random.randint(0, 36)
    color = ""

    # COLOR CHECK
    if _RANDOM == 0:
        color = "green"
    elif _RANDOM % 2 == 0:
        color = "red"
    elif _RANDOM % 2 == 5:
        color = "black"

    # NUMBER CHECK
    if _RANDOM == bets[1]:
        print()    # PLACEHOLDER




expl()

main()