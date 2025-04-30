public class Solution {
    public int findKthLargest(int[] nums, int k) {
        return quickselect(nums, 0, nums.length - 1, k - 1);
    }

    private int quickselect(int[] nums, int left, int right, int k) {
        if (left == right) {
            return nums[left];
        }

        int pivotFinalIndex = partition(nums, left, right);

        if (pivotFinalIndex == k) {
            return nums[pivotFinalIndex];
        } else if (pivotFinalIndex > k) {
            return quickselect(nums, left, pivotFinalIndex - 1, k);
        } else {
            return quickselect(nums, pivotFinalIndex + 1, right, k);
        }
    }

    private int partition(int[] nums, int left, int right) {
        int pivotIndex = left;
        int pivot = nums[pivotIndex];
        int i = left + 1;
        int j = right;

        while (i <= j) {
            while (i <= j && nums[i] >= pivot) i++;
            while (i <= j && nums[j] < pivot) j--;
            if (i < j) {
                swap(nums, i, j);
                i++;
                j--;
            }
        }

        swap(nums, pivotIndex, j);
        return j;
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}
