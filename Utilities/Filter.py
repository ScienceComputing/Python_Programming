aa = ['histidine', 'isoleucine', 'leucine', 'lysine', 'methionine', 'phenylalanine', 'threonine', 'tryptophan', 'valine']
target_aa = filter(lambda member: len(member) > 9, aa)
print(list(target_aa))
