from theatrical_players.price_calculator import PerformancePriceCalculator
from theatrical_players.volume_credits_calculator import VolumeCreditsCalculator


def format_as_dollars(amount):
    return f"${amount:0,.2f}"


class StringStatementPrinter:
    def __init__(self, invoice, plays):
        self._performances = invoice["performances"]
        self._plays = plays
        self._customer = invoice["customer"]
        self._price_calculator = PerformancePriceCalculator(plays)
        self._volume_credits_calculator = VolumeCreditsCalculator(plays)

    def print(self) -> str:
        result: list[str] = [f"Statement for {self._customer}"]
        result.extend(self._statement_for_performance(perf) for perf in self._performances)
        total_price = self._price_calculator.total(self._performances) / 100
        total_volume_credits = self._volume_credits_calculator.total(self._performances)
        result.append(f"Amount owed is {format_as_dollars(total_price)}")
        result.append(f"You earned {total_volume_credits} credits\n")
        return "\n".join(result)

    def get_play_for_performance(self, performance):
        return self._plays[performance["playID"]]

    def _statement_for_performance(self, perf) -> str:
        play = self.get_play_for_performance(perf)
        return f' {play["name"]}: {format_as_dollars(self._price_calculator.calculate_price(perf)/100)} ({perf["audience"]} seats)'
