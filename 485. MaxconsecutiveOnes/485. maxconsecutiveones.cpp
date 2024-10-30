class Solution
{
public:
    int findMaxConsecutiveOnes(vector<int> &nums)
    {
        int cnt = 0;
        int prev = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] != 1)
            {
                if (cnt > prev)
                {
                    prev = cnt;
                }
                cnt = 0;
                continue;
            }
            cnt++;
        }
        if (cnt > prev)
        {
            return cnt;
        }
        return prev;
    }
};