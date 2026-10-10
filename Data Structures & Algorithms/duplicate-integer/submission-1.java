class Solution {

    HashMap hash = new HashMap();
    public boolean hasDuplicate(int[] nums) {

        for (int i = 0; i < nums.length; i++){

            if (hash.containsKey(nums[i])){
                return true;
            } else {
                hash.put(nums[i], nums[i]);
            }
        }
        return false;
    }
}
