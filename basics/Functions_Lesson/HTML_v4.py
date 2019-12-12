def tag(content,*args,classe='sucess', inline=False):
    tag='span' if inline else 'div'
    html=content if not callable(content) else content(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'

def tag_list(*itens):
    list=''.join((f'<li>{item}</li>' for item in itens))
    return f'\n<ul>{list}</ul>'



if __name__=="__main__":
    #print(tag('block'))
    #or
    #print(tag('block',inline=True))
    #print(tag_list('alice','frank','max','george'))
    print(tag(tag_list,'alice','frank','max','george',classe='info'))
