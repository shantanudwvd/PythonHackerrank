def string_valid(s, k):
    st = []
    i = 0
    done = False
    for i in range(0, len(s)):
        if len(st) == 0:
            st.append([s[i], 1])
            continue
        if len(st):
            if st[-1][0] == s[i]:
                st.append([s[i], st[-1][1]+1])
                if st[-1][1] == k:
                    done = True
                    for j in range(0, k):
                        st.pop()
            else:
                st.append([s[i], 1])
    stri = ''
    for i in range(0, len(st)):
        stri += st[i][0]
    if k == 1:
        return ''
    return stri


s = 'abbcccba'
k = 3
print(string_valid(s, k))
