### Encode and Decode Strings - medium ###
## Recommended solution -> https://youtu.be/B1k_sxOSgv8?si=SaCrLNmXM26av-Lu

# Design an algorithm to encode a list of strings to a string.
# The encoded string is then sent over the network and is decoded back to the original list of strings.

## Machine 1 (sender) has the function:
# String encode(List<String> strs) {
#     // ... your code
#     return encoded_string;
# }

## Machine 2 (receiver) has the function:
# List<String> decode(String encoded_string) {
#     // ... your code
#     return decoded_strs;
# }

## So Machine 1 does:
# String encoded_string = encode(strs);

## and Machine 2 does:
# List<String> decoded_strs = decode(encoded_string);

# decoded_strs in Machine 2 should be the same as the input strs in Machine 1.
# Implement the encode and decode methods.

## Example 1:
# Input: strs = ["Hello","World"]
# Output: ["Hello","World"]
## Explanation:
# Solution solution = new Solution();
# String encoded_string = solution.encode(strs);
# // Machine 1 ---encoded_string---> Machine 2
# List<String> decoded_strs = solution.decode(encoded_string);

## Example 2:
# Input: strs = [""]
# Output: [""]

## Constraints:
# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains any possible characters out of 256 valid ASCII characters.

## Follow up: Could you write a generalized algorithm to work on any possible set of characters?

## Recommended Time & Space Complexity
# You should aim for a solution with O(m) time for each encode() and decode() call and O(m+n) space, 
# where m is the sum of lengths of all the strings and n is the number of strings.

### 1 - Idea - brain storm ### -> spent 60 min. - ❌could not pass all tests by Submit
## Link all strings from input list to one string using delimiter char out of 0-255 ASCII, e.x. "😀"
# Time: O(n) - Encode and Decode
# Space: O(n) - Encode and Decode

# Step 1: 'Encode':
# Step 2: declare char = "😀" and result string
# Step 3: loop the input list of strings and join each to result string with delimiter
# Step 4: return result string

# Step 5: 'Decode':
# Step 6: check if the input string is empty return list with empty element [""]
# Step 7: 'res' - declare result list of strings
# Step 8: 'chars' - declare list of chars
# Step 9: loop the input string
# Step 10: checks in the loop:
# Step 10.1: if character equal delimiter -> append 'chars' list as word to 'res' and clear 'chars' list
# Step 10.2: else -> append character to 'chars' list
# Step 10.3: after loop append last 'chars' list as word to 'res', because in the end of input str there is no delimiter
# Step 11: return 'res' - result list of strings

## Problem with 1 - Idea:
#       problem of using -> return self.delimiter.join(strs)
#1 strs=["Hello", "World"]
#2 strs=["", ""]
#3 strs=[""]
#4 strs=[]
#   The problem is that #3 and #4 become identical after encoding:
#   ["Hello", "World"]  -> "Hello😀World"
#   ["", ""]            -> "😀"
#   [""]                -> ""
#   []                  -> ""

### 2 - Idea - solution from AI hint ###
## You need to know where the count ends. That's why length-prefix formats usually add a second delimiter after the number.
# Your format: <count>😀<data>
# Example: 99😀Hello😀World
# Decode algorithm:
#   Read characters until the first 😀
#   Everything before it is the count
#   Convert it to int
#   Decode the remaining string

class Solution:

    delimiter = "😀"

    def encode(self, strs: List[str]) -> str:

        return str(len(strs)) + self.delimiter + self.delimiter.join(strs)
        # ["Hello", "World"] => "2😀Hello😀World"
        # ["", ""]           => "2😀😀"
        # [""]               => "1😀"
        # []                 => "0😀"

    def decode(self, s: str) -> List[str]:

        if not s:
            return []

        # read characters until the first 😀 delimiter
        index = s.index(self.delimiter)

        # everything before it is the count -> convert it to int
        count = int(s[:index])

        # decode the remaining string
        data = s[index + 1:]

        # covers when in Encode 'strs' is empty list: strs = []
        if count == 0:
            return []

        # covers in Encode 'strs' is not empty list: strs = ["Hello", "World"], ["", ""], [""]
        return data.split(self.delimiter)

        #1 s = "2Hello😀World" -> res = ["Hello","World"]
        #2 s = "2😀😀" -> res = ["", ""]
        #3 s = "1😀" -> res = [""]
        #4 s = "0😀" -> res = []



