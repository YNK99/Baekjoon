def solution(id_list, report, k):
    stopped_id = []
    singo = {c:[] for c in id_list}
    mail_list = {c:0 for c in id_list}
    for r in report:
        singo[r.split()[1]].append(r.split()[0])
    for user, singo_id in singo.items():
        if len(set(singo_id)) >= k:
            stopped_id.append(user)
        singo[user] = set(singo[user])
    for stopped in stopped_id:
        for s in singo[stopped]:
            mail_list[s] = mail_list[s] + 1
    return list(mail_list.values())