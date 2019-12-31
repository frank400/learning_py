from functools import reduce
from calendar import mdays, month_name

indice = filter(lambda months: mdays[months] == 31, range(1, 13))
months=map(lambda i:month_name[i],indice)
string_names=reduce(lambda title,names:f'{title}:\n{names}',months,'31 days months')
if __name__=='__main__':
    print(string_names)