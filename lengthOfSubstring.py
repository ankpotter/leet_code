def lengthOfLongestSubstring(s):
        current_character = []
        cur_len = 0
        max_len = 0
        max_str = ''
        for i in s:
            print("First : ", current_character)
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
            print("Second : ",current_character)
        if(cur_len > max_len):
            return cur_len
        else:
            return max_len

print(lengthOfLongestSubstring("dvd!k"))