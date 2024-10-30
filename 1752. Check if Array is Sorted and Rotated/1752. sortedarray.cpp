class Solution
{
public:
    bool check(vector<int> &nums)
    {
        int cnt = 0;
        int temp = 0;
        for (int i = 0; i < nums.size() - 1; i++)
        {
            if (nums[i] > nums[i + 1])
            {
                temp = i + 1;
                cnt++;
            }
        }
        if (cnt > 1)
        {
            return false;
        }
        if (cnt == 0)
        {
            return true;
        }
        if (cnt == 1)
        {
            for (int i = 0; i < temp - 1; i++)
            {
                if (nums[i] <= nums[i + 1])
                {
                    continue;
                }
                else
                {
                    return false;
                }
            }
            for (int i = temp; i < nums.size() - 1; i++)
            {
                if (nums[i] <= nums[i + 1])
                {
                    continue;
                }
                else
                {
                    return false;
                }
            }
            if (nums[0] >= nums.back())
            {
                exit;
            }
            else
            {
                return false;
            }
        }
        return true;
    }
};