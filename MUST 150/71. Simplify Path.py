class Solution:
    def simplifyPath(self, path: str) -> str:
        # .. means we go back to the previous directory
        # . means we are in the current directory and do nothing
        # No trailing / and only a single / in between two directory name
        # We use stack so that we can go back to or pop the previous directory in O(1) time for ..
        # Overall time and space complexity O(n)

        stack = []
        directoryName = ''

        for i in path + '/':  # We add a trailing / so that crteating directoryName becomes easier
            if i == '/':
                if directoryName == '..':
                    if len(stack):
                        stack.pop()
                elif directoryName != '.' and directoryName != '':
                    stack.append(directoryName)
                directoryName = ''
            else:
                directoryName += i
        print(stack)
        return '/' + '/'.join(stack)

