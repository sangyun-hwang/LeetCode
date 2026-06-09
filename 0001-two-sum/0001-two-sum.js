/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const seen = new Map();

    for (const [i, num] of nums.entries()) {
        const need = target - num;

        if (seen.has(need)) {
            return [seen.get(need), i];
        }

        seen.set(num, i);
    }
};