x = ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]

def recur(arr):
    for i in arr:
        if type(i) == list:
            recur(i)
        else:
            print(i)

recur(x)