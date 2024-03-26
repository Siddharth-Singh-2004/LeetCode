class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int missing = 1;
        int n = nums.size();

        // Sort the array
        std::sort(nums.begin(), nums.end());
        
        for (int i = 0; i<n; i++){
            if (nums[i] == missing) {
                missing++;
            }
        }
        return missing;
    }
};