from itertools import combinations
from time import time

from AlgoInvest.utils.utils import csv_to_list
from AlgoInvest.utils.shares_portfolio import SharesPortfolio, Share
from AlgoInvest import MAX_WALLET_COST


def brutal_force_itertools(path, start):
    shares_from_csv = csv_to_list(path)
    # Removed header
    shares_from_csv = shares_from_csv[1:]
    # For each action, generate a Share object
    shares_list = []
    for action in shares_from_csv:
        shares_list.append(Share(action[0], action[1], action[2]))

    step = time()
    print(f"\n\t\tshares_list:\t{(step-start):>20.2f}")

    # Generate all combinations of 1 to size_of_list elements of shares_list
    combinations_list = []
    for k in range(1, len(shares_list) + 1):
        combinations_list += list(combinations(shares_list, k))

    step_mem = step
    step = time()
    print(f"\t\tcombinations_list:\t\t{(step-step_mem):.2f}")

    # Generate SharesPortfolio list
    shares_portfolio_list = []
    for combination in combinations_list:
        shares_portfolio_list.append(SharesPortfolio(combination))

    step_mem = step
    step = time()
    print(f"\t\tshares_portfolio_list:\t\t{(step-step_mem):.2f}")

    # Sorted shares_portfolio_list by benefit
    shares_portfolio_list.sort(key=lambda x: x.benefit, reverse=True)

    step_mem = step
    step = time()
    print(f"\t\tsorted shares_portfolio_list:\t{(step-step_mem):.2f}")

    # Keep the number_of_item first benefit with a cost less or equal to MAX_WALLET_COST €
    number_of_item = 1
    shares_portfolio_index = []
    for index, shares_portfolio in enumerate(shares_portfolio_list):
        if shares_portfolio.cost <= MAX_WALLET_COST:
            shares_portfolio_index.append(index)
            number_of_item -= 1
            if number_of_item == 0:
                break
    for index in shares_portfolio_index:
        print(shares_portfolio_list[index])
