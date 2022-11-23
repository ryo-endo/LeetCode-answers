/*
 * @lc app=leetcode id=9 lang=typescript
 *
 * [9] Palindrome Number
 */

// @lc code=start
function isPalindrome(x: number): boolean {
    const arr = [...String(x)];
    const len = arr.length;
    for (let i = 0; i < len / 2; i++) {
        if (arr[i] != arr[len - 1 - i]) return false;
    }
    return true;
};
// @lc code=end

export { isPalindrome };