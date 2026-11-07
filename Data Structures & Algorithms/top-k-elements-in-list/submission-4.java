class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        int max = 0;
        for (int num: nums){
            map.put(num, map.getOrDefault(num, 0) + 1);
            max = Math.max(max, map.get(num));
        }
        List<Integer>[] lst = new List[max+1];

        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            int val = entry.getValue();
            if (lst[val] != null) {
                lst[val].add(entry.getKey());
            }
            else {
                lst[val] = new ArrayList<Integer>();
                lst[val].add(entry.getKey());
            }            
        }
        int[] result = new int[k];
        int counter = 0;
        for (int i = max; i >= 0; i--){
            if (counter == k){
                break;
            }
            if (lst[i] != null){
                for (int num: lst[i]) {
                    result[counter] = num;
                    counter+=1;
                }
            }
            
        }

            System.out.println(map);
            System.out.println(max);
            System.out.println(Arrays.toString(lst));
        return result;
    }
}
