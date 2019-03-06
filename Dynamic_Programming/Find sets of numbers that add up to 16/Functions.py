def rcc_without_dyamic_programming(_list, _sum, idx):
    if _sum < 0:
        return 0
    if idx < 0:
        return 0
    if  _sum == 0:
        return 1
    if  _list[idx-1] > _sum :
        return rcc_without_dyamic_programming(_list, _sum, idx-1)
    else:
        return (rcc_without_dyamic_programming(_list, _sum - _list[idx-1], idx-1) +
         rcc_without_dyamic_programming(_list, _sum, idx-1))
def rcc_with_dyamic_programming(_list, _sum, idx, mem):
    key = str(_sum) + ":" + str(idx)
    if key in mem.keys():
        return mem[key]
    if _sum < 0:
        return 0
    if idx < 0:
        return 0
    if  _sum == 0:
        return 1
    if  _list[idx-1] > _sum :
        to_return = rcc_with_dyamic_programming(_list, _sum, idx-1, mem)
    else:
        to_return = (rcc_with_dyamic_programming(_list, _sum - _list[idx-1], idx-1, mem) +
         rcc_with_dyamic_programming(_list, _sum, idx-1, mem))
    mem[key] = to_return
    return to_return

              