#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        hashtable = {}
        i = 0
        str = str.split(' ')
        if (len(pattern)!=len(str)):
            return False
        while i<len(pattern):
            if str[i] not in hashtable:
                if (pattern[i] in [v for k,v in hashtable.items()]):
                    return False
                hashtable[str[i]] = pattern[i]
            elif (hashtable[str[i]] != pattern[i]):
                return False
            i +=1
        return True

