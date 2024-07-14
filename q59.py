# Write the steps to count the number of times a specific substring appears in the string s.

s = "abcdefgabcdxyzabcde"
sub = "abcd"
print(s.count(sub))

# Find the position of all occurrences of a substring in the string s?
st = "abcdefgabcdxyzabcde"
subs = "abcd"
index_list = []
curr=0
while True:
    curr = st.find(subs,curr)
    if curr == -1:
        break
    else:
        index_list.append(curr)
        curr += len(subs)  # Move to the next character after the current found substring
print(index_list)
