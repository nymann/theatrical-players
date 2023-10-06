import math


def format_as_dollars(amount):
    return f"${amount:0,.2f}"


def amount_for_tragedy(perf) -> float:
    this_amount = 40000
    if perf["audience"] > 30:
        this_amount += 1000 * (perf["audience"] - 30)
    return this_amount


def amount_for_comedy(perf) -> float:
    this_amount = 30000
    if perf["audience"] > 20:
        this_amount += 10000 + 500 * (perf["audience"] - 20)

    this_amount += 300 * perf["audience"]
    return this_amount


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


def amount_for_performance(perf, plays) -> float:
    play = get_play_for_performance(perf, plays)
    if play["type"] == "tragedy":
        return amount_for_tragedy(perf)
    if play["type"] == "comedy":
        return amount_for_comedy(perf)
    raise ValueError(f'unknown type: {play["type"]}')


def amount_for_performances(performances, plays) -> float:
    return sum(amount_for_performance(perf, plays) for perf in performances)


def statement(invoice, plays):
    result = f'Statement for {invoice["customer"]}\n'
    performances = invoice["performances"]

    for perf in performances:
        play = plays[perf["playID"]]
        result += f' {play["name"]}: {format_as_dollars(amount_for_performance(perf, plays)/100)} ({perf["audience"]} seats)\n'

    result += f"Amount owed is {format_as_dollars(amount_for_performances(performances, plays)/100)}\n"
    result += f"You earned {volume_credits_for_performances(performances, plays)} credits\n"
    return result
