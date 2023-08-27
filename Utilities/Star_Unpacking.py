def drop_first_last(sequence_quality_score): 
  first, *middle, last = sequence_quality_score
  return avg(middle)

record = ('Jane', 'Female', '12', '20', '0')
name, gender, *PC_gene_expression = record
name
gender
PC_gene_expression

*past, current = [90, 32, 7, 89, 0, 5, 10]
past_avg = sum(past) / len(past)
past
past_avg

items = [5, 6, 7]
head, *tail = items
head
tail
