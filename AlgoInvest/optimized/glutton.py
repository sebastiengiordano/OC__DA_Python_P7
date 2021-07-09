from AlgoInvest.utils.utils import csv_to_list
from AlgoInvest.utils.shares_portfolio_optimized import (
    ShareOpt, SharesPortfolioOpt)
from AlgoInvest import MAX_WALLET_COST


def glutton(path):
    # Get the list of shares
    shares_list = csv_to_list(path)
    # Removed header
    shares_list = shares_list[1:]
    # For each action, generate a ShareOpt object
    share_list = []
    for action in shares_list:
        share_list.append(ShareOpt(action[0], action[1], action[2]))
    # Sort list by benefit
    share_list.sort(key=lambda x: x.benefit, reverse=True)
    share_portfolio = SharesPortfolioOpt(portfolio=[])
    for index in range(len(share_list)):
        share_portfolio_update = share_portfolio + share_list[index]
        if share_portfolio_update.cost <= MAX_WALLET_COST * 100:
            share_portfolio = share_portfolio_update
        else:
            break

    # Show the wallet get by glutton algo
    print(share_portfolio)
