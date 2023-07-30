class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int xors = 0;
        for(int i= 0 ; i< nums.size(); i++)
            xors ^= nums[i];  
            //std::cout<< xors << std::endl;
        return xors;
    }
};