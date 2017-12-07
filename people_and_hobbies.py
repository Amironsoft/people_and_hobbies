import pandas as pd

from plot_circles import plot_circles

if __name__ == '__main__':
    print('people_and_hobbies started')
    # initial loading of data
    df = pd.read_csv('users.tsv', sep='\t')
    uniq_names = sorted(df['username'].unique())  # people name set
    print(uniq_names, '\n')
    main_table = []  # main table to storage name, hobby_list, count

    for name in uniq_names:
        print(name)  # person name
        hobby_list = set(df[df['username'] == name]['hobby'].values)
        count = len(hobby_list)  # the quantity of hobbies for each person
        main_table.append([name, hobby_list, count])  # add info about each
        print('\t', *hobby_list)

    print(main_table)
    hobby_dict = {a_name: set(a_hobby_list) for a_name, a_hobby_list, a_count in main_table}

    for a_name, a_hobby_list, a_count in main_table:
        a_score_list = []  # score list for each person
        for b_name, b_hobby_list, b_count in main_table:
            if a_name != b_name:  # do not compare person himself
                score = 2*len(a_hobby_list & b_hobby_list)/(a_count + b_count)
                # the similarities with hobbies of other person
                a_score_list.append([b_name, score])

        x = a_name
        y, score = max(a_score_list, key=lambda x: x[1])
        print(x, y, score)  # closest person

        ofile = rf'img/{x}_{y}_{score:0.2f}.png'
        plot_circles(x, y, score, ofile, hobby_dict[x], hobby_dict[y])

