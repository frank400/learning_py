tag_atributes=('tag_accesskey','tag_id')
ul_atributes=('ul_id')


def get_atribute(content,supported):
    return ' '.join(f'{k.split("_")[-1]}= "{v}"' for k ,v in content.items() if k in supported)
    


def tag(content,*args,classe='sucess', inline=False,**newkwargs):
    tag='span' if inline else 'div'
    html=content if not callable(content) else content(*args,**newkwargs)
    atributes_tag=get_atribute(newkwargs,tag_atributes)
    return f'<{tag} {atributes_tag} class="{classe}">{html}\n</{tag}>'

def tag_list(*itens,**newkwargs):
    list=''.join((f'<li>{item}</li>' for item in itens))
    atributes_ul = get_atribute(newkwargs,ul_atributes)
    return f'\n<ul {atributes_ul} >{list}</ul>'


if __name__=="__main__":
    print(tag(tag_list,'alice','frank','max','george',classe='info',
              tag_accesskey='m',tag_id='content',ul_id='list'))
