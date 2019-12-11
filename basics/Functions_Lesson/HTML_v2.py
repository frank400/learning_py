def tag(text,classe='sucess', inline=False):
    tag='span' if inline else 'div'
    return f'<{tag} class="{classe}">{text}</{tag}>'

if __name__=="__main__":
    print(tag('block'))
    #or
    print(tag('block',inline=True))