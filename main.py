import myentry

# myentry.pyを用意し、以下のようにYOUR_ENTRY_LISTを宣言する
# YOUR_ENTRY_LIST = [
#     [class, 定員N, エントリー数v, 通りたい度w],
#     [class, 定員N, エントリー数v, 通りたい度w],
#     [class, 定員N, エントリー数v, 通りたい度w]
#     ]

YOUR_ENTRY_LIST = myentry.YOUR_ENTRY_LIST


# 定員割れ科目の除外
def removeShortage(entries_list):
    clean_entries_list = []
    for entry in entries_list:
        if entry[1] >= entry[2]:
            print(entry[0] + "は倍率が1以下です。プロセスから除外します。")
        else:
            clean_entries_list.append(entry)
    print("==========")
    return clean_entries_list


def calc(entries_list):
    # 当選確率リスト
    p_list = []

    # 期待値Eを計算
    for entry in entries_list:
        p_list.append(entry[1] / entry[2])
    E = sum(p_list)

    # 期待値Eの出力
    if E > 8.0:
        print('期待値Eが8.0を超えています。')
    print('期待値E: ' + str(E))

    # 通りたい度リスト
    w_list = []
    for entry in entries_list:
        w_list.append(entry[3])

    # 期待値Eにより重み付けされた当選確率の計算
    pDash_list = []
    for i, entry in enumerate(entries_list):
        pDash_list.append((w_list[i] / sum(w_list)) * p_list[i])
    pDoubleDash_list = []
    for j, pDash in enumerate(pDash_list):
        pDoubleDash_list.append((E / sum(pDash_list)) * pDash)

    # 最終的な結果の出力
    for i, entry in enumerate(entries_list):
        print(entry[0] + "の重み付け当選確率: " + str(pDoubleDash_list[i]))


if __name__ == '__main__':
    calc(removeShortage(YOUR_ENTRY_LIST))
