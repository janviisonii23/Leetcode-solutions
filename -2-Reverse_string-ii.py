class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)  # Convert the string to a list of characters
        for i in range(0, len(s), 2 * k):
            s[i:i + k] = reversed(s[i:i + k])  # Reverse the first k characters in each 2k segment
        return ''.join(s)  # Join the list back into a string and return
