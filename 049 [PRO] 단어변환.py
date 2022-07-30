# https://school.programmers.co.kr/learn/courses/30/lessons/43163?language=python3

import sys

def compare_word(w1, w2):
    cnt = 1
    n = len(w1)
    for i in range(n):
        if w1[i] != w2[i]:
            cnt -= 1
        if cnt < 0: return False
    return True

def solution(begin, target, words):
    words.append(begin)
    n = len(words)
    visited = [False] * n
    result = sys.maxsize
    try:
        start_i = words.index(target)
    except:
        return 0
    
    def dfs(index, word, dis):
        nonlocal result
        
        if word == begin:
            result = min(result, dis)    
            return
        
        for i in range(n):
            if visited[i]: continue
            if compare_word(word, words[i]):
                visited[i] = True
                dfs(i, words[i], dis+1)
                visited[i] = False
            
    visited[start_i] = True
    dfs(start_i, words[start_i], 0)
    return result