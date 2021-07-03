'''Manage share and shares portfolio.

Classes:
    Share
    SharesPortfolio

'''


class Share:
    '''Class which represent a share.

    Attributes
    ----------
    name : Label of the share.
    cost : Cost of the share.
    benefit : Benefit in % of the share

    '''
    def __init__(self, name: str, cost: str, benefit: str) -> None:
        self._name = name
        self._cost = float(cost)
        self._benefit = float(benefit)

    @property
    def name(self):
        return self._name

    @property
    def cost(self):
        return self._cost

    @property
    def benefit(self):
        return self._benefit


class SharesPortfolio:
    def __init__(self, portfolio: list[Share]) -> None:
        self._portfolio = portfolio
        self._portfolio_cost_benefit()

    @property
    def cost(self):
        return self._portfolio_cost

    @property
    def benefit(self):
        return self._portfolio_benefit

    def _portfolio_cost_benefit(self):
        global_cost = 0
        global_benefit = 0
        for share in self._portfolio:
            cost = share.cost
            global_cost += cost
            global_benefit += cost * share.benefit / 100
        self._portfolio_cost = global_cost
        self._portfolio_benefit = global_benefit

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
