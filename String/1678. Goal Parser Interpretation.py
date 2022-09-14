class Solution:
    def interpret(self, command: str) -> str:
        # Using built_in replace method to get the desired output
        command = command.replace("()", "o")
        command = command.replace("(al)", "al")

        return command