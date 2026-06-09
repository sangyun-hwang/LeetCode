/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const seen = {};

    for (const [i, num] of nums.entries()) {
        const need = target - num;

        if (need in seen) {
            return [seen[need], i];
        }

        seen[num] = i;
    }
    
};