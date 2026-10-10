class Solution {
    public boolean hasDuplicate(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            for (int m = i + 1; m < nums.length; m++){
                if (nums[i]==nums[m]) {
                    return true;
                }
            }
        }
        return false;
    }
}