class Solution
{
public:
    bool isPalindrome(int x)
    {

        if (x < 0)
        {
            return false;
        }
        else
        {
            int reverse = 0;
            int temp = x;
            while (temp > 0)
            {
                int lastdigit = temp % 10;
                temp = temp / 10;
                if (INT_MIN / 10 <= reverse && reverse <= INT_MAX / 10)
                {
                    reverse = (reverse * 10) + lastdigit;
                }
                else
                {
                    return false;
                }
            }
            if (reverse == x)
            {
                return true;
            }
            return false;
        }
    }
};