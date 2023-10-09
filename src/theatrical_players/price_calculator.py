from theatrical_players.model import Performance


class PerformancePriceCalculator:
    def calculate(self, performance: Performance) -> float:
        if performance.play.type == "tragedy":
            return self._amount_for_tragedy(performance)
        if performance.play.type == "comedy":
            return self._amount_for_comedy(performance)
        raise ValueError(f"unknown type: {performance.play.type}")

    def total(self, performances: list[Performance]) -> float:
        return sum(self.calculate(perf) for perf in performances)

    def _amount_for_tragedy(self, performance: Performance) -> float:
        this_amount = 40000
        if performance.audience > 30:
            this_amount += 1000 * (performance.audience - 30)
        return this_amount

    def _amount_for_comedy(self, performance: Performance) -> float:
        this_amount = 30000
        if performance.audience > 20:
            this_amount += 10000 + 500 * (performance.audience - 20)

        this_amount += 300 * performance.audience
        return this_amount
