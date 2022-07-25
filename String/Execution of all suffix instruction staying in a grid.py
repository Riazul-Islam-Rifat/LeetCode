class Solution:
    def executeInstructions(self, n: int, startPos, s: str):
        answer = []
        itr = 0
        n = n - 1
        while itr < len(s):
            startFrom = [startPos[0], startPos[1]]
            count = 0
            moves_to_execute = s[itr:]
            for item in moves_to_execute:
                if item == "R":
                    if (startFrom[1] + 1) <= n:
                        startFrom[1] = startFrom[1] + 1
                        count += 1
                    else:
                        break
                elif item == "L":
                    if (startFrom[1] - 1) >= 0:
                        startFrom[1] = startFrom[1] - 1
                        count += 1
                    else:
                        break
                elif item == "D":
                    if (startFrom[0] + 1) <= n:
                        startFrom[0] = startFrom[0] + 1
                        count += 1
                    else:
                        break
                elif item == "U":
                    if (startFrom[0] - 1) >= 0:
                        startFrom[0] = startFrom[0] - 1
                        count += 1
                    else:
                        break

            answer.append(count)
            itr += 1
        return answer