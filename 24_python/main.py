#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Xiao Huang'


class Solution(object):
    def __init__(self, nums, exp, cnt, target):
        self.nums = nums
        self.exp = exp
        self.cnt = cnt
        self.target = target

    def start(self):
        output = "Numbers: "
        for num in self.nums:
            output += str(num) + " "
        print output
        if not self.calculate(self.cnt):
            print "No solution."
        output = "Numbers: "

    def calculate(self, n):
        if n == 1:
            if self.nums[0] == self.target:
                print self.exp[0]
                return True
            else:
                return False
        else:
            for i in range(n):
                for j in range(i+1, n):
                    num_a = self.nums[i]
                    num_b = self.nums[j]
                    # move the last number to j position
                    # save the temp result in i position
                    self.nums[j] = self.nums[n - 1]
                    exp_a = self.exp[i]
                    exp_b = self.exp[j]
                    self.exp[j] = self.exp[n-1]

                    # a + b
                    self.exp[i] = "(" + exp_a + "+" + exp_b + ")"
                    self.nums[i] = num_a + num_b
                    if self.calculate(n-1):
                        return True

                    # a - b
                    self.exp[i] = "(" + exp_a + "-" + exp_b + ")"
                    self.nums[i] = num_a - num_b
                    if self.calculate(n-1):
                        return True

                    # b - a
                    self.exp[i] = "(" + exp_b + "-" + exp_a + ")"
                    self.nums[i] = num_b - num_a
                    if self.calculate(n-1):
                        return True

                    # a * b
                    self.exp[i] = "(" + exp_a + "*" + exp_b + ")"
                    self.nums[i] = num_a * num_b
                    if self.calculate(n-1):
                        return True

                    # a / b
                    if num_b != 0:
                        self.exp[i] = "(" + exp_a + "/" + exp_b + ")"
                        self.nums[i] = num_a / float(num_b)
                        if self.calculate(n-1):
                            return True

                    # b / a
                    if num_a != 0:
                        self.exp[i] = "(" + exp_b + "/" + exp_a + ")"
                        self.nums[i] = num_b / float(num_a)
                        if self.calculate(n-1):
                            return True

                    self.nums[i] = num_a
                    self.nums[j] = num_b
                    self.exp[i] = exp_a
                    self.exp[j] = exp_b
            return False


if __name__ == "__main__":
    cnt = 4
    target = 24
    nums = [-1] * cnt
    for i in range(cnt):
        while True:
            try:
                nums[i] = int(raw_input("Please enter number " + str(i+1) + ": " ))
                break
            except ValueError:
                print "That was no valid number. Please try again..."
    exp = [str(x) for x in nums]

    s = Solution(nums, exp, cnt, target)
    s.start()