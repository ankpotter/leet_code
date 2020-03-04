class Solution:
    def lengthOfLongestSubstring(self, s):
        current_character = []
        cur_len = 0
        max_len = 0
        max_str = ''
        for i in s:
            if(i in current_character):
                if(max_len < cur_len):
                    max_len = cur_len
                    max_str = ''.join(current_character)
                current_character = current_character[current_character.index(i)+1:]
                current_character.append(i)
                cur_len = len(current_character)
            else:
                current_character.append(i)
                cur_len += 1
        if(cur_len > max_len):
            return cur_len
        else:
            return max_len
        