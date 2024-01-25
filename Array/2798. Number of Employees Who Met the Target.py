class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:

        employee = 0

        for hour in hours:
            if hour >= target:
                employee += 1

        return employee