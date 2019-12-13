def split_func(dic):
    return ' '.join(f'{k.split("_")[-1]} = "{v}" ' for k,v in dic.items())


def tag_func(tag,*args,**kwargs):
    proper=split_func(kwargs)
    content=' '.join(args)
    return f' <{tag} {proper}> {content} </{tag}>'


if __name__=='__main__':
    print(tag_func('p',
              tag_func('span','curso python 3 por '),
              tag_func('strong','Juracy Filho',id='jf'),
              tag_func('span', 'e'),
              tag_func('strong','Leonarno Leitão',id='ll'),
              HTML_class='alert'
    ))