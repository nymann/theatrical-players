import math

from theatrical_players.price_calculator import PerformancePriceCalculator


def format_as_dollars(amount):
    return f"${amount:0,.2f}"


def get_play_for_performance(performance, plays):
    return plays[performance["playID"]]


def volume_credits_for_performances(performances, plays) -> float:
    volume_credits = 0
    for perf in performances:
        play = get_play_for_performance(perf, plays)
        volume_credits += max(perf["audience"] - 30, 0)
        if "comedy" == play["type"]:
            volume_credits += math.floor(perf["audience"] / 5)
    return volume_credits


def statement_for_performance(perf, plays) -> str:
    calculator = PerformancePriceCalculator(plays)
    play = get_play_for_performance(perf, plays)
    return f' {play["name"]}: {format_as_dollars(calculator.calculate_price(perf)/100)} ({perf["audience"]} seats)'


def statement(invoice, plays):
    results = [f'Statement for {invoice["customer"]}']
    performances = invoice["performances"]
    price_calculator = PerformancePriceCalculator(plays)
    results.extend(statement_for_performance(perf, plays) for perf in performances)
    results.append(f"Amount owed is {format_as_dollars(price_calculator.total(performances)/100)}")
    results.append(f"You earned {volume_credits_for_performances(performances, plays)} credits\n")
    return "\n".join(results)
