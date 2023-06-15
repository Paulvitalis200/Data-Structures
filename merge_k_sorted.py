def merge_lists(lists):
    if lists is None or len(lists) == 0:
        return None

    while len(lists) > 1:
        mergedLists = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if (i+1) < len(lists) else None

            mergedLists.append(merge(l1, l2))

        lists = mergedLists

    return lists[0]


def merge(l1, l2):
    # todo
    p = l1.head
    q = l2.head
    s = None

    if not p:
        return q
    if not q:
        return p

    if p and q:
        if p.data <= q.data:
            s = p
            p = s.next
        else:
            s = q
            q = s.next

        new_head = s

    while p and q:
        if p.data <= q.data:
            s.next = p
            s = p
            p = s.next
        else:
            s.next = q
            s = q
            q = s.next

    if not p:
        s.next = q
    if not q:
        s.next = p

    return new_head
