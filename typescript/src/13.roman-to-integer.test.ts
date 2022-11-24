import { romanToInt } from "./13.roman-to-integer"

test("only I", () => {
    expect(romanToInt("III")).toBe(3)
});

test("only V", () => {
    expect(romanToInt("V")).toBe(5)
});

test("only X", () => {
    expect(romanToInt("X")).toBe(10)
});

test("only L", () => {
    expect(romanToInt("L")).toBe(50)
});

test("only C", () => {
    expect(romanToInt("C")).toBe(100)
});

test("only D", () => {
    expect(romanToInt("D")).toBe(500)
});

test("only 100", () => {
    expect(romanToInt("M")).toBe(1000)
});

test("I can be placed before V (5) make 4.", () => {
    expect(romanToInt("IV")).toBe(4)
});

test("I can be placed before X (10) make 9.", () => {
    expect(romanToInt("IX")).toBe(9)
});

test("X can be placed before L (50) make 40.", () => {
    expect(romanToInt("XL")).toBe(40)
});

test("X can be placed before C (100) make 90.", () => {
    expect(romanToInt("XC")).toBe(90)
});

test("C can be placed before D (500) make 400.", () => {
    expect(romanToInt("CD")).toBe(400)
});

test("C can be placed before M (1000) make 900.", () => {
    expect(romanToInt("CM")).toBe(900)
});

test("mixed", () => {
    expect(romanToInt("LVIII")).toBe(58)
});

test("mixed2", () => {
    expect(romanToInt("MCMXCIV")).toBe(1994)
});