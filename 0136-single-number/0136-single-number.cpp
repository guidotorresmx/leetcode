class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int xors = 0;
        for(auto i: nums)
            xors ^= i;  
            //std::cout<< xors << std::endl;
        return xors;
    }
};