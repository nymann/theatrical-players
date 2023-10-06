class PerformancePriceCalculator:
    def __init__(self, plays) -> None:
        self._plays = plays

    def calculate_price(self, perf) -> float:
        play = self._get_play_for_performance(perf)
        if play["type"] == "tragedy":
            return self._amount_for_tragedy(perf)
        if play["type"] == "comedy":
            return self._amount_for_comedy(perf)
        raise ValueError(f'unknown type: {play["type"]}')

    def total(self, performances) -> float:
        return sum(self.calculate_price(perf) for perf in performances)

    def _amount_for_tragedy(self, perf) -> float:
        this_amount = 40000
        if perf["audience"] > 30:
            this_amount += 1000 * (perf["audience"] - 30)
        return this_amount

    def _amount_for_comedy(self, perf) -> float:
        this_amount = 30000
        if perf["audience"] > 20:
            this_amount += 10000 + 500 * (perf["audience"] - 20)

        this_amount += 300 * perf["audience"]
        return this_amount

    def _get_play_for_performance(self, performance):
        return self._plays[performance["playID"]]
