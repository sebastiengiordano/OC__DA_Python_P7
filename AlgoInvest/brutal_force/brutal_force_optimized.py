from operator import le
from time import time

from AlgoInvest.utils.utils import csv_to_list
from AlgoInvest.utils.shares_portfolio_optimized import (
    ShareOpt, SharesPortfolioOpt)
from AlgoInvest import MAX_WALLET_COST


def brutal_force_optimized(path, start):

    # Get the list of shares
    shares_from_csv = csv_to_list(path)
    # Removed header
    shares_from_csv = shares_from_csv[1:]
    # For each action, generate a ShareOpt object
    shares_list = []
    for action in shares_from_csv:
        shares_list.append(ShareOpt(action[0], action[1], action[2]))

    step = time()
    print(f"\n\t\tshares_list:\t{(step-start):>28.2f}")

    # Generate a table in order to include the best way to chose the shares
    # And append it the first share portfolio
    first_share_portfolio = SharesPortfolioOpt([shares_list[0]])
    first_share_portfolio.update()
    best_shares_portfolio = [first_share_portfolio]

    # Genererate list of SharesPortfolio
    for k in range(1, len(shares_list)):
        best_shares_portfolio += check_share(
            best_shares_portfolio, shares_list[k])
        share_portfolio = SharesPortfolioOpt([shares_list[k]])
        share_portfolio.update()
        best_shares_portfolio.append(share_portfolio)
        if time() - start > 60:
            print(f"Too long: {k} items managed in {(time() - start):.2f}s")
            break

    step_mem = step
    step = time()
    print(f"\t\tGenererate list of SharesPortfolio:\t{(step-step_mem):.2f}")

    # Sorted best_shares_portfolio by benefit
    best_shares_portfolio.sort(key=lambda x: x.benefit, reverse=True)

    step_mem = step
    step = time()
    print(f"\t\tsorted best_shares_portfolio:\t\t{(step-step_mem):.2f}")

    # Keep the number_of_item first benefit with
    # a cost less or equal to MAX_WALLET_COST €
    number_of_item = 1
    shares_portfolio_index = []
    for index, shares_portfolio in enumerate(best_shares_portfolio):
        if shares_portfolio.cost <= MAX_WALLET_COST * 100:
            shares_portfolio_index.append(index)
            number_of_item -= 1
            if number_of_item == 0:
                break
    for index in shares_portfolio_index:
        print(best_shares_portfolio[index])


def check_share(
        best_shares_portfolio: list[SharesPortfolioOpt],
        share: ShareOpt
        ) -> list[SharesPortfolioOpt]:
    shares_portfolio = []
    for share_portfolio in best_shares_portfolio:
        share_portfolio_update = share_portfolio + share
        if share_portfolio_update.cost <= MAX_WALLET_COST * 100:
            shares_portfolio.append(share_portfolio_update)
    return shares_portfolio
