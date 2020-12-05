# Q04
def cutbar(n, m):
    num = 1     # 棒の数
    count = 0   # 切った回数

    # [n]cmの棒を[num]本になるまで分割する
    while num < n:
        # 棒の本数が人数より多ければ，棒の数が人数分増える．棒の数の方が多ければ，棒の数が倍増する．
        if num <= m:
            num += num
        else:
            num += m
        count += 1

    return count


while True:
    n = int(input("n = "))
    m = int(input("m = "))
    print("=> count =", cutbar(n, m))
