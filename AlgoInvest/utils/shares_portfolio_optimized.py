'''Manage share and shares portfolio.

Classes:
    Share
    SharesPortfolio

'''


class ShareOpt:
    '''Class which represent a share.

    Attributes
    ----------
    name : Label of the share.
    cost : Cost of the share.
    benefit : Benefit in % of the share
    money_benefit : Benefit calculate (cost * benefit / 100)

    '''

    def __init__(self, name: str, cost: str, benefit: str) -> None:
        self._name = name
        self._cost = int(cost * 100)
        self._benefit = float(benefit)
        self._money_benefit = cost * benefit / 100

    @property
    def name(self):
        return self._name

    @property
    def cost(self):
        return self._cost

    @property
    def benefit(self):
        return self._benefit

    @property
    def money_benefit(self):
        return self._money_benefit


class SharesPortfolioOpt:
    '''Class which represent a portfolio of shares.

    Attributes
    ----------
    portfolio : List of share.
    portfolio_cost : Cost of the share.
    benefit : Benefit in % of the share
    money_benefit : Benefit calculate (cost * benefit / 100)

    '''
    def __init__(self, portfolio: list[Share]) -> None:
        self._portfolio = portfolio
        self._portfolio_cost = 0
        self._portfolio_benefit = 0

    def update(self) -> None:
        global_cost = 0
        global_benefit = 0
        for share in self._portfolio:
            global_cost += share.cost
            global_benefit += share.cost * share.benefit / 100
        self._portfolio_cost = global_cost
        self._portfolio_benefit = global_benefit

    @property
    def cost(self):
        return self._portfolio_cost

    @property
    def benefit(self):
        return self._portfolio_benefit

    def _max_name_len(self):
        max_name_len = 0
        for name in [share.name for share in self._portfolio]:
            if len(name) > max_name_len:
                max_name_len = len(name)
        return max_name_len

    def __str__(self) -> str:
        max_name_len = self._max_name_len()
        benefit_in_perc = (
            self._portfolio_benefit
            / self._portfolio_cost
            * 100)
        str_to_print = ("\n\tShares of this portfolio:")
        for share in self._portfolio:
            str_to_print += (
                f"\n\t\t{share.name.ljust(max_name_len)}"
                + f"\tcost: {share.cost:7.2f} € "
                + f"\tbenefit: {share.benefit:6.2f} %")
        str_to_print += (
            "\n\n\t\t"
            + f"Global cost:                   \t{self._portfolio_cost:7.2f} €"
            + "\n\t\t"
            + "Global benefit (after 2 years):\t"
            + f"{self._portfolio_benefit:7.2f} € "
            + f"{benefit_in_perc:7.2f} %"
            )
        return str_to_print

    def __add__(self, share: Share):
        name = self._portfolio.copy()
        name.append(share)
        return SharesPortfolioOpt(
            name,
            self._portfolio_cost + share.cost,
            self._portfolio_benefit + (
                share.cost * share.benefit / 100
                )
            )
