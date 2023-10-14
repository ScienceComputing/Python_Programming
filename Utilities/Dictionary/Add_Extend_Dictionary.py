amino_acid['new_key'] = value 
amino_acid['new_key'] = []
amino_acid['new_key'] = ()
amino_acid['new_key'] = {}
amino_acid['new_key'].append(value)
amino_acid['new_key'].append([])
amino_acid['new_key'].append(())
amino_acid['new_key'].append({})

amino_acid = {'Glutamine': 'Help the immune system function and normal brain function and digestion'}
amino_acid_cys = [('Cysteine', 'Help prevent side effects due to drug reactions and toxic chemicals')]

# Update the dictionary with new key-value pair 
amino_acid.update(amino_acid_cys)
print(amino_acid['Cys'])
