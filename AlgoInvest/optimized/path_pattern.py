from cmath import cos
from time import time

from AlgoInvest import MAX_WALLET_COST
from AlgoInvest.utils.shares_portfolio_optimized import (
    ShareOpt, SharesPortfolioOpt)
from AlgoInvest.utils.utils import csv_to_list


def path_pattern(path: str, start: time):

    # Get the list of shares
    shares_from_csv = csv_to_list(path)
    # Removed header
    shares_from_csv = shares_from_csv[1:]
    # For each action, generate a ShareOpt object
    shares_list = []
    for action in shares_from_csv:
        shares_list.append(ShareOpt(action[0], action[1], action[2]))

    step = time()
    print(f"\n\t shares_list:\t{step-start}")

    number_of_shares = len(shares_list)

    # Generate matrix for best benefit path
    # First column correspond to initial value, set to 0
    best_benefit = [
        [0 for _ in range(MAX_WALLET_COST + 1)]
        for _ in range(number_of_shares + 1)
        ]
    # Generate matrix which store all course path
    course_path = [
        [0 for _ in range(MAX_WALLET_COST + 1)]
        for _ in range(number_of_shares + 1)
        ]

    # pathfinding algorithm
    for i in range(1, number_of_shares + 1):
        share = shares_list[i - 1]
        cost = cost_in_cents_to_int(share.cost)
        benefit = share.money_benefit
        for b in range(1, MAX_WALLET_COST + 1):
            # Check if cost is lower than the row cost
            if cost <= b:
                # keep the best between the preview benefit of this row
                # and (the preview benefit of this row minus this share cost
                # plus the benefit of this share)
                row_b_minus_cost = b - cost
                benefit_temp = best_benefit[i-1][row_b_minus_cost] + benefit
                if benefit_temp > best_benefit[i-1][b]:
                    best_benefit[i][b] = benefit_temp
                    course_path[i][b] = row_b_minus_cost
                else:
                    best_benefit[i][b] = best_benefit[i-1][b]
                    course_path[i][b] = b
            else:
                # cost is too high, we keep the last benefit
                best_benefit[i][b] = best_benefit[i-1][b]
                course_path[i][b] = b

    # Seek for the list of shares,
    # by browsing the course_path matrix in reverse,
    # from its last cell (which contains the best benefit)
    j = MAX_WALLET_COST
    shares_portfolio = SharesPortfolioOpt([])
    for i in range(number_of_shares, 0, -1):
        current_course_path = course_path[i][j]
        if current_course_path < j:
            # This share has been added
            shares_portfolio += shares_list[i - 1]
            # Jump to the row where we come from
            j = current_course_path

    print(shares_portfolio)


def cost_in_cents_to_int(cost_in_cents: int) -> int:
    if cost_in_cents <= 0:
        return MAX_WALLET_COST + 1
    if cost_in_cents % 100:
        return int(cost_in_cents / 100) + 1
    else:
        return int(cost_in_cents / 100)
