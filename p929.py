class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniq_list = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            uniq_list.add(local.replace(".", "") + '@' + domain ) 
        return len(uniq_list)
