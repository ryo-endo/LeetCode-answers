import { isPalindrome } from "./9.palindrome-number";

test("no palindrome", () => {
    expect(isPalindrome(123)).toBe(false);
});

test("palindrome", () => {
    expect(isPalindrome(12321)).toBe(true);
});

test("one word", () => {
    expect(isPalindrome(1)).toBe(true);
});


test("two word", () => {
    expect(isPalindrome(11)).toBe(true);
});

test("minus number", () => {
    expect(isPalindrome(-121)).toBe(false);
});