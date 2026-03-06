def calc_price(items, is_member):
    # 合計金額を計算する処理
    total = 0
    for i in items:
        total += i

    # 会員の場合は割引する。ただし10000円以上の買い物の時だけ
    if is_member == True:
        if total >= 10000:
            total = total * 0.9
        else:
            total = total
    else:
        total = total

    # 送料の計算。5000円未満なら500円かかる
    if total < 5000:
        total = total + 500

    return total


# テスト実行
cart_items = [3000, 2500, 5000]
print(calc_price(cart_items, True))
