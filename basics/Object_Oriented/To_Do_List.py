from datetime import datetime


class Task:
    def __init__(self,desc):
        self.desc=desc
        self.done=False
        self.create=datetime.now()
    
    def __str__(self):
        return self.desc + (' (Concluida)'if self.done else '')
    
    def conclude(self):
        self.done = True


def main():
    home=[]
    home.append(Task('Passar Roupa'))
    home.append(Task('Lavar Prato'))

    [task.conclude() for task in home if task.desc=='Lavar Prato']
    for task in home:
        print(f'-{task}')


if __name__=='__main__':
    main()