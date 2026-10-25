class Solution:

  def countDaysTogether(
      self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
  ) -> int:
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def convert_to_days(date_str: str) -> int:
      month, day = map(int, date_str.split("-"))
      return sum(days_in_months[: month - 1]) + day

    alice_arrival = convert_to_days(arriveAlice)
    alice_leave = convert_to_days(leaveAlice)
    bob_arrival = convert_to_days(arriveBob)
    bob_leave = convert_to_days(leaveBob)

    latest_arrival = max(alice_arrival, bob_arrival)
    earliest_leave = min(alice_leave, bob_leave)

    if latest_arrival <= earliest_leave:
      return earliest_leave - latest_arrival + 1
    return 0