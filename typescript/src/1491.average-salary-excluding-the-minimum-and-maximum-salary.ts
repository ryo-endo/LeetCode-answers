/*
 * @lc app=leetcode id=1491 lang=typescript
 *
 * [1491] Average Salary Excluding the Minimum and Maximum Salary
 */

// @lc code=start
function average(salary: number[]): number {
    salary = salary.sort((a, b) => a - b)
    salary.shift()
    salary.pop()
    const sum = salary.reduce((acc, v) => acc + v, 0)

    return sum / salary.length
};
// @lc code=end

export { average }
