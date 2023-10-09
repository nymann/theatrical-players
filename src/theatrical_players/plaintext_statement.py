from theatrical_players.currency_converter import CurrencyFormatter
from theatrical_players.model import CustomerPerformances
from theatrical_players.model import Performance
from theatrical_players.price_calculator import PerformancePriceCalculator
from theatrical_players.volume_credits_calculator import VolumeCreditsCalculator


class PlaintextStatement:
    def __init__(self, currentcy_formatter: CurrencyFormatter) -> None:
        self._price_calculator = PerformancePriceCalculator()
        self._volume_credits_calculator = VolumeCreditsCalculator()
        self._formatter = currentcy_formatter

    def render(self, customer_performances: CustomerPerformances) -> str:
        result: list[str] = [f"Statement for {customer_performances.customer}"]
        result.extend(self._statement_for_performance(perf) for perf in customer_performances.performances)
        total_price = self._price_calculator.total(customer_performances.performances)
        total_volume_credits = self._volume_credits_calculator.total(customer_performances.performances)
        result.append(f"Amount owed is {self._formatter.format(total_price)}")
        result.append(f"You earned {total_volume_credits} credits")
        return "\n".join(result)

    def _statement_for_performance(self, perf: Performance) -> str:
        price = self._price_calculator.calculate(perf)
        return f" {perf.play.name}: {self._formatter.format(price)} ({perf.audience} seats)"
