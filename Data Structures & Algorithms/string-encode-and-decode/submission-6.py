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


### 3 - Idea - solution from Recommended YouTube ###
# https://youtu.be/B1k_sxOSgv8?si=SaCrLNmXM26av-Lu
# Note: no need to use character delimiter out of 0-255 (256 ASCII) like I used delimiter '😀' in 1 & 2 solutions
# Refactored recommended YouTube solution using 'parts' to increase efficiency in 'Encode'
# to prevent creating new string object while concatenating:
#   res = ""
#   for s in strs:
#       res += str(len(s)) + "#" + s

## Intuition:
# Instead of storing all string lengths first and then appending the strings, we can directly attach each string to its length.
# For every string, we write length#string.
# The # character acts as a clear boundary between the length and the actual content, and using the length ensures we know exactly how many characters to read—no matter what characters appear in the string itself.
# During decoding, we simply read characters until we reach # to find the length, then extract exactly that many characters as the string.
# This approach is both simpler and more efficient because it avoids building separate sections for lengths and content.

## Algorithm:

## Encoding:
#   1. Initialize an empty result builder (or list of string parts).
#   2. For each string in the list:
#       - Compute its length.
#       - Append "length#string" to the builder.
#   3. Return the final encoded string.

## Decoding:
#   1. Initialize an empty list for the decoded strings and a pointer i = 0.
#   2. While i is within the bounds of the encoded string:
#       - Move a pointer j forward until it finds '#' — this segment represents the length.
#       - Convert the substring s[i:j] into an integer length.
#       - Move i to the character right after '#'.
#       - Extract the next length characters — this is the original string.
#       - Append the extracted string to the result list.
#       - Move i forward by length to continue decoding the next segment.
#   3. Return the list of decoded strings.

## Time & Space Complexity:
# Time complexity: O(m+n)for each encode() and decode() function calls.
# Space complexity: O(m+n) for each encode() and decode() function calls.
# Where 'm' is the sum of lengths of all the strings and 'n' is the number of strings.

class Solution:

    def encode(self, strs: List[str]) -> str:

        parts = []

        for s in strs:
            parts.append(str(len(s)))
            parts.append("#")
            parts.append(s)

        return "".join(parts)
        # ["Hello", "World"] => "5#Hello5#World"
        # ["", ""]           => "0#0#"
        # [""]               => "0#"
        # []                 => ""

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        # s = "5#Hello5#World"
        while i < len(s):

            # outer 1-iteration: i = 0, j = 0 after "Hello" i = 7, j = 7
            j = i
            
            # Find the '#' after the length
            # inner 1-iteration: s[0] != '#' ('5' != '#' -> j += 1), next iteration: s[1] != "#" '(#' != '#' -> exit from while)
            while s[j] != "#":
                # inner 1-iteration: j = 0 + 1 = 1
                j += 1

            # outer 1-iteration: convert "5" to int as length - 'i' start index in 's' string and 'j' is end index
            length = int(s[i:j])
            
            # Move i to the first character of the string
            # outer 1-iteration: i = 1 + 1 = 2
            i = j + 1
            # outer 1-iteration: j = 2 + 5 = 7
            j = i + length

            # Extract the string of the given length
            # append string "Hello" - 'i' start index of string 's' and 'j' is end index
            res.append(s[i:j])
            
            # Move i to the next length field
            # i = 7
            i = j

        return res

        #1 s = "5#Hello5#World" -> res = ["Hello","World"]
        #2 s = "0#0#" -> res = ["", ""]
        #3 s = "0#" -> res = [""]
        #4 s = "" -> res = []



