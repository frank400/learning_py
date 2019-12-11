def tag(text,classe='sucess'):
    return f'<div class="{classe}">{text}</div>'

if __name__=="__main__":
    #test(assertions)
    assert tag("incluido com sucesso")==\
        '<div class="sucess">incluido com sucesso</div>'
    print(tag('block'))