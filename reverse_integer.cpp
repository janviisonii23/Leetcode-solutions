// 7. Reverse Integer

class Solution {
public:
    int reverse(int x) {
        vector<int> arr;
        int number;
        int temp=x;
        string num;
        if(x==0){
            return 0;
        }
        if(x>0){
            while(temp%10==0){
                temp /= 10;
            }
            while(temp>0){
                arr.push_back(temp%10);
                temp /= 10;
            }
            for(int i = 0 ; i< arr.size() ; i++){
                num += to_string(arr[i]);
            }
        }else{
            temp = abs(temp);
            while(temp%10==0){
                temp /= 10;
            }
            while(temp>0){
                arr.push_back(temp%10);
                temp /= 10;
            }
            for(int i = 0 ; i< arr.size() ; i++){
                num += to_string(arr[i]);
            }
        };
        try {
            int number = std::stoi(num);
            if (x<0) {
                number = -number;
            }
            return number;
        } catch (const std::out_of_range&) {
            return 0; // Overflow condition
        }
    return number;
}};
