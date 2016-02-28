#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Xiao Huang'

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def huffman(l):
    while len(l) > 1:
        l = sorted(l, cmpTreeNode)[::-1]
        node_a = l.pop()
        node_b = l.pop()
        node = TreeNode(node_a.val + node_b.val)
        node.left = node_a
        node.right = node_b
        l.append(node)
    return l[0]

def cmpTreeNode(a, b):
    x = a.val
    y = b.val
    if x > y:
        return 1
    if x < y:
        return -1
    return 0

def dfs(root, sol, result, freq):
    if not root.left and not root.right:
        freq.append(root.val)
        result.append(sol)
        return
    if root.left:
        dfs(root.left, sol + "0", result, freq)
    if root.right:
        dfs(root.right, sol + "1", result, freq)
    return

if __name__ == "__main__":
    ol = [2,3,4,4,5,7] # frequency
    l = [TreeNode(x) for x in ol]
    root = huffman(l)
    result = []
    freq = []
    dfs(root, "", result, freq)
    for i in range(len(result)):
        print str(freq[i]) + " -> " + str(result[i])