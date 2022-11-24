/*
 * @lc app=leetcode id=13 lang=typescript
 *
 * [13] Roman to Integer
 */

// @lc code=start
function romanToInt(s: string): number {
    s = s.replace('IV', 'IIII')
    s = s.replace('IX', 'VIIII')
    s = s.replace('XL', 'XXXX')
    s = s.replace('XC', 'LXXXX')
    s = s.replace('CD', 'CCCC')
    s = s.replace('CM', 'DCCCC')

    const arr = [...s]
    let sum = 0
    arr.forEach(e => {
        switch (e) {
            case 'I': sum += 1; break;
            case 'V': sum += 5; break;
            case 'X': sum += 10; break;
            case 'L': sum += 50; break;
            case 'C': sum += 100; break;
            case 'D': sum += 500; break;
            case 'M': sum += 1000; break;
            default:
        }
    });
    return sum
};
// @lc code=end

export { romanToInt }