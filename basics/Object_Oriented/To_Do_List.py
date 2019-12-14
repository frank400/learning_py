from datetime import datetime
class Project:
    def __init__(self,name):
        self.name=name
        self.list=[]
    
    def __str__(self):
        return f'{self.name} ({len(self.pendent())} undone task(s))'  

    def add(self,desc):
        self.list.append(Task(desc))
    
    def pendent(self):
        return [task for task in self.list if not task.done]
    
    def search(self,desc):
        return [task for task in self.list
                if task.desc==desc][-1]


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
    home=Project('build a house')
    home.add('build walls')
    home.add('make the floor')
    home.add('ceiling')
    print(home)

    home.search('make the floor').conclude()
    for task in home.list:
        print(f'-{task}')



if __name__=='__main__':
    main()