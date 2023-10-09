import math

from theatrical_players.model import Performance


class VolumeCreditsCalculator:
    def total(self, performances: list[Performance]) -> float:
        volume_credits = 0
        for perf in performances:
            volume_credits += max(perf.audience - 30, 0)
            if "comedy" == perf.play.type:
                volume_credits += math.floor(perf.audience / 5)
        return volume_credits
