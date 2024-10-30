class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)  # Sort citations in descending order
        h_index = 0
        
        for i in range(len(citations)):
            if citations[i] >= i + 1:  # Check if there are at least (i + 1) papers with at least (i + 1) citations
                h_index = i + 1  # Update the h-index
        
        return h_index