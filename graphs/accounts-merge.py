# Pattern: Union Find (Disjoint Set)
# Time: O(n * α(n)) where n is total emails, α is inverse Ackermann (basically O(n))
# Space: O(n) — parent dict + email_to_name dict + groups dict
# Key insight: if two emails appear in the same account, union them. union find chains
#   connections so emails linked through shared accounts end up in the same group.
# How union find works:
#   - find(x): follows parent pointers to the root of x's group. path compression flattens the chain.
#   - union(x, y): makes the root of x's group point to the root of y's group. now they're one group.
#   - initialize by setting parent[x] = x for every element (everyone starts as their own boss)
# Gotchas:
#   - Map email -> name, NOT name -> email (multiple people can share a name)
#   - Union find only deals with emails. name mapping is a separate dict combined at the end.
#   - For each account, union all emails with the first email — no need to union every pair
#   - Group by find(email) at the end to collect all emails sharing a root
#   - Sort emails within each group before returning
# Still learning: struggled with connecting union find mechanics to the name mapping. key
#   realization is they're separate concerns combined only in the final step.
# Palantir framing: "identify networks of related operatives by merging accounts sharing aliases"

def merge_accounts(accounts: list[list[str]]) -> list[list[str]]:
    parent = {}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        parent[find(x)] = find(y)

    # step 1: map email -> name
    email_to_name = {}
    for account in accounts:
        for email in account[1:]:
            email_to_name[email] = account[0]

    # step 2: initialize parent — every email is its own boss
    for account in accounts:
        for email in account[1:]:
            parent[email] = email

    # step 3: union all emails within each account
    for account in accounts:
        first_email = account[1]
        for email in account[2:]:
            union(first_email, email)

    # step 4: group emails by root
    groups = {}
    for email in parent:
        root = find(email)
        if root not in groups:
            groups[root] = []
        groups[root].append(email)

    # step 5: build result
    result = []
    for root, emails in groups.items():
        name = email_to_name[root]
        result.append([name] + sorted(emails))
    return result
