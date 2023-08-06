class Solution:
    def canCompleteCircuit(self, gas: [int], cost: [int]) -> int:
        # When cost is higher than the gas availability we can never traverse the whole route
        if sum(gas)<sum(cost):
            return -1
    # As there will be only one starting station, hence the station with the lowest-
    # remaining gas will be the starting station
        remainingGas = 0 # Keeps track the amount of remaining gas
        startingStation = 0 # Assuming the first station is the starting station
        gasRemainingAtStartingStation = 0 # The lowest remaining gas at starting station

        for station in range(1,len(gas)):
            gasAvailability = gas[station-1] # Gas availability at the previous station
            usedGas = cost[station-1] # Used gas to reach to the current station
            remainingGas+= gasAvailability - usedGas # Remaining gas after a travel

            if remainingGas<gasRemainingAtStartingStation:
                gasRemainingAtStartingStation = remainingGas
                startingStation = station

        return startingStation

    # Time complexity: O(n)
    # Space complexity: O(1)