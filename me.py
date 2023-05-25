with open('scu_stopwords.txt', 'r',encoding='utf-8') as f1, open('hit_stopwords.txt', 'r',encoding='utf-8') as f2, open('new_stopwords.txt', 'w',encoding='utf-8') as f3:
    lines = set(f1.readlines() + f2.readlines())
    f3.writelines(sorted(lines))
