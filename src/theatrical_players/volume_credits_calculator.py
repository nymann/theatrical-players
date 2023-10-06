import math


class VolumeCreditsCalculator:
    def __init__(self, plays) -> None:
        self._plays = plays

    def total(self, performances) -> float:
        volume_credits = 0
        for perf in performances:
            play = self._get_play_for_performance(perf)
            volume_credits += max(perf["audience"] - 30, 0)
            if "comedy" == play["type"]:
                volume_credits += math.floor(perf["audience"] / 5)
        return volume_credits

    def _get_play_for_performance(self, performance):
        return self._plays[performance["playID"]]
