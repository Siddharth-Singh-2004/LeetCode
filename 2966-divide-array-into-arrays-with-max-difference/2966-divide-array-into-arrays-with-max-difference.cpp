class Solution {
public:
    vector<vector<int>> divideArray(vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        int size = nums.size();
        vector<vector<int>> result(size / 3, vector<int>(3));
        int index = 0;
        for (int i = 0; i < size; i += 3) {
            if (i+2 < size && nums[i+2] - nums[i] <= k) {
                result[index] = {nums[i], nums[i+1], nums[i+2]};
                index++;
            }
            else {
                return vector<vector <int>>();
            }
        }
        return result;
    }
};