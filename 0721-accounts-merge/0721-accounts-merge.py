class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        emailToName = {}
        emailToID = {}
        parent = {}

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in emailToID:
                    emailToID[email] = len(emailToID)
                    parent[emailToID[email]] = emailToID[email]
                if email not in emailToName:
                    emailToName[email] = name
                union(emailToID[account[1]], emailToID[email])

        mergedAccounts = {}
        for email, emailID in emailToID.items():
            rootID = find(emailID)
            if rootID not in mergedAccounts:
                mergedAccounts[rootID] = [email]
            else:
                mergedAccounts[rootID].append(email)

        result = []
        for emails in mergedAccounts.values():
            emails.sort()
            name = emailToName[emails[0]]
            result.append([name] + emails)

        return result

    
