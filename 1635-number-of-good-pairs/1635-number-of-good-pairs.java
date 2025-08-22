import java.util.*;

class Solution {
    public int numIdenticalPairs(int[] nums) {
        Map<Integer, Integer> hm = new HashMap<>();
        int gp = 0;
        for (int i = 0; i < nums.length; i++) {
            gp = gp + hm.getOrDefault(nums[i], 0);
            hm.put(nums[i], hm.getOrDefault(nums[i], 0) + 1);
        }
        return gp;
    }
}
