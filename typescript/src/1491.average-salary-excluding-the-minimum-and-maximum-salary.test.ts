import { average } from "./1491.average-salary-excluding-the-minimum-and-maximum-salary";

test('ex-1', () => {
    expect(average([4000, 3000, 1000, 2000])).toBe(2500)
})


test('ex-2', () => {
    expect(average([1000, 2000, 3000])).toBe(2000)
})

test('same value', () => {
    expect(average([1000, 1000, 1000])).toBe(1000)
})
