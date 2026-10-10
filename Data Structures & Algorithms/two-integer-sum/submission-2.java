class Solution {
    public int[] twoSum(int[] nums, int target) {

        int[] res = new int[2];

        for (int i = 0; i < nums.length; i++) {
            int resta = target - nums[i];

            for (int m = i+1; m < nums.length; m++){
                if (nums[m]==resta){
                    res[0]=i;
                    res[1]=m;
                    return res;
                }
            }
        }
        return null;
    }
}
