from collections import Counter

def minWindow(s: str, t: str) -> str:

    # m = len(s) # source string
    # n = len(t) # target string

    # # make a hashmap of the target string
    # t_character_dict = {}
    # for i in t:
    #     if i in t_character_dict.keys():
    #         t_character_dict[i] = t_character_dict[i] + 1 
    #     else:
    #         t_character_dict[i] = 1

    # left = 0
    # right = 1
    # no_of_char_matched = 0
    # # for j in s:
    # while no_of_char_matched <= len(list(t_character_dict.keys())) and right < m:
    #     if (s[left] in t_character_dict) and (s[right] in t_character_dict):
    #         right = right + 1
    #         no_of_char_matched = no_of_char_matched + 2
    #     elif (s[left] not in t_character_dict) and (s[right] not in t_character_dict):
    #         right = right + 1
    #         left = left + 1
    #         no_of_char_matched = no_of_char_matched + 1
    #     elif (s[left] in t_character_dict) and (s[right] not in t_character_dict):
    #         right = right + 1
    #         no_of_char_matched = no_of_char_matched + 1
    #     else:
    #         left = left + 1
    #         no_of_char_matched = no_of_char_matched + 1
    
    # return s[left: right+1]
    
    if not t or not s:
            return ""

    dict_t = Counter(t)
    required = len(dict_t)

    # Filter s to include only characters in t
    filtered_s = [(i, char) for i, char in enumerate(s) if char in dict_t]

    left = 0
    right = 0
    formed = 0
    window_counts = {}
    
    ans = float("inf"), None, None

    while right < len(filtered_s):
        character = filtered_s[right][1]
        window_counts[character] = window_counts.get(character, 0) + 1

        if window_counts[character] == dict_t[character]:
            formed += 1

        while left <= right and formed == required:
            character = filtered_s[left][1]

            end = filtered_s[right][0]
            start = filtered_s[left][0]
            if end - start + 1 < ans[0]:
                ans = (end - start + 1, start, end)

            window_counts[character] -= 1
            if window_counts[character] < dict_t[character]:
                formed -= 1
            left += 1    

        right += 1    
    
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
    
print(minWindow("ADOBECODEBANC", "ABC"))