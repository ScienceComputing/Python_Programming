def list2dict(key_list, value_list):
    """Return a dictionary where key_list provides the keys and value_list provides the values."""
    zipped_iterator = zip(key_list, value_list)
    result_dict = dict(zipped_iterator)
    return result_dict

list_of_list = [
  ['Arab World',
  'ARB',
  'Adolescent fertility rate (births per 1,000 women ages 15-19)',
  'SP.ADO.TFRT',
  '1960',
  '133.56090740552298'],
  ['Arab World',
  'ARB',
  'International migrant stock, total',
  'SM.POP.TOTL',
  '1960',
  '3324685.0']]

var_name = [
 'CountryName',
 'CountryCode',
 'IndicatorName',
 'IndicatorCode',
 'Year',
 'Value']

# Convert list of lists into list of dicts
list_of_dict = [list2dict(var_name, list_i) for list_i in list_of_list]
print(list_of_dict[0])
# {'CountryName': 'Arab World', 'CountryCode': 'ARB', 'IndicatorName': 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'IndicatorCode': 'SP.ADO.TFRT', 'Year': '1960', 'Value': '133.56090740552298'}
