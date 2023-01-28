# Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list of disjoint intervals.
#
# Implement the SummaryRanges class:
#
# SummaryRanges() Initializes the object with an empty stream.
# void addNum(int value) Adds the integer value to the stream.
# int[][] getIntervals() Returns a summary of the integers in the stream currently as a list of disjoint intervals [starti, endi]. The answer should be sorted by starti.
#
#
# Example 1:
#
# Input
# ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
# [[], [1], [], [3], [], [7], [], [2], [], [6], []]
# Output
# [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]
#
# Explanation
# SummaryRanges summaryRanges = new SummaryRanges();
# summaryRanges.addNum(1);      // arr = [1]
# summaryRanges.getIntervals(); // return [[1, 1]]
# summaryRanges.addNum(3);      // arr = [1, 3]
# summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
# summaryRanges.addNum(7);      // arr = [1, 3, 7]
# summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
# summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
# summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
# summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
# summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]
from typing import List


class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        if not self.intervals:
            self.intervals.append([value, value])
            return

        for i, interval in enumerate(self.intervals):
            if interval[0] <= value <= interval[1]:
                return
            elif interval[0] > value:
                if i > 0 and self.intervals[i - 1][1] == value - 1:
                    self.intervals[i - 1][1] = value
                    if i < len(self.intervals) and self.intervals[i][0] == value + 1:
                        self.intervals[i - 1][1] = self.intervals[i][1]
                        self.intervals.pop(i)
                elif i < len(self.intervals) and self.intervals[i][0] == value + 1:
                    self.intervals[i][0] = value
                else:
                    self.intervals.insert(i, [value, value])
                return
        if self.intervals[-1][1] == value - 1:
            self.intervals[-1][1] = value
        else:
            self.intervals.append([value, value])

    def getIntervals(self) -> List[List[int]]:
        return self.intervals


if __name__ == "__main__":
    summaryRanges = SummaryRanges()
    summaryRanges.addNum(1)  # arr = [1]
    print(summaryRanges.getIntervals())  # return [[1, 1]]
    summaryRanges.addNum(3)  # arr = [1, 3]
    print(summaryRanges.getIntervals())  # return [[1, 1], [3, 3]]
    summaryRanges.addNum(7)  # arr = [1, 3, 7]
    print(summaryRanges.getIntervals())  # return [[1, 1], [3, 3], [7, 7]]
    summaryRanges.addNum(2)  # arr = [1, 2, 3, 7]
    print(summaryRanges.getIntervals())  # return [[1, 3], [7, 7]]
    summaryRanges.addNum(6)  # arr = [1, 2, 3, 6, 7]
    print(summaryRanges.getIntervals())  # return [[1, 3], [6, 7]]