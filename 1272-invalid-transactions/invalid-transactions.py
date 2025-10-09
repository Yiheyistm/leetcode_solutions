class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transaction_list = defaultdict(list)
        invalid_transactions = set()
       
        transactions = sorted(transactions)
        for i in range(len(transactions)):
            name, time, amount, city = transactions[i].split(',')
            if int(amount) > 1000:
                invalid_transactions.add(i)

            for j in range(i + 1, len(transactions)):
                nm, t1, am, ct = transactions[j].split(',')
                if name != nm:
                    break

                if city != ct and abs(int(time) - int(t1)) <= 60:
                    invalid_transactions.add(j)
                    invalid_transactions.add(i)

        return [transactions[i] for i in invalid_transactions]


        # group = defaultdict(list)
        # for i in range(len(transactions)):
        #     name, time, amount, city = transactions[i].split(',')
        #     group[name].append((int(time),int(amount), city, transactions[i]))
        # # print(group)
        # ans = []
        # for name, transaction in group.items():
        #     transaction.sort(key = lambda x:x[0])
        #     left = 0
        #     marked = [False] * len(transaction)
        #     for right in range(len(transaction)):
        #         while transaction[right][0] - transaction[left][0] > 60:
        #             left += 1
        #         for i in range(left, right):
        #             if transaction[i][2] != transaction[right][2]:
        #                 if not marked[i]:
        #                     ans.append(transaction[i][3])
        #                     marked[i] = True

        #                 if not marked[right]:
        #                     ans.append(transaction[right][3])
        #                     marked[right] = True
        #         if transaction[right][1] > 1000 and not marked[right]:
        #             ans.append(transaction[right][3])
        #             marked[right] = True
        # return ans