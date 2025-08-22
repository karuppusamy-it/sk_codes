class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map <Integer,Integer> hm= new HashMap<>();
        for(int i=0;i<nums.length;i++)
        {
            int a=target-nums[i];
            if(hm.containsKey(a))
            {
                return new int[]{i,hm.get(a)};
            }   
            else
            {
                hm.put(nums[i],i);
            }
        }
         return new int[]{};
    }
}