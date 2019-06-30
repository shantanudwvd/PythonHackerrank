def fun(s):
    username = ""
    website_name = ""
    ext = ""
    idx = s.find("@")
    if idx == -1:
        return False
    i = 0
    while i < idx:
        username += s[i]
        i += 1
    idx1 = s.find(".")
    if idx1 == -1:
        return False
    idx += 1
    while idx < idx1:
        website_name += s[idx]
        idx += 1
    idx1 += 1
    while idx1 < len(s):
        ext += s[idx1]
        idx1 += 1
    if username.isidentifier() and website_name.isalnum() and len(ext) <= 3:
        return True
    else:
        return False


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
