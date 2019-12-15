from datetime import datetime,timedelta
class Project:
    def __init__(self,name):
        self.name=name
        self.tasks=[]

    def __iter__(self):
        return self.tasks.__iter__()
    
    def __str__(self):
        return f'{self.name} ({len(self.pendent())} undone task(s))'  

    def add(self,desc,deadline=None):
        self.tasks.append(Task(desc,deadline))
    
    def pendent(self):
        return [task for task in self.tasks if not task.done]
    
    def search(self,desc):
        return [task for task in self.tasks
                if task.desc==desc][-1]


class Task:
    def __init__(self,desc,deadline):
        self.desc=desc
        self.done=False
        self.create=datetime.now()
        self.deadline=deadline
    
    def __str__(self):
        status=[]
        if self.done:
            status.append('(Done)')
        elif self.deadline:
            if datetime.now()>self.deadline:
                status.append("(expired)")
            else:
                days=(self.deadline -datetime.now()).days
                status.append(f'(that task expire in {days} days)')
        return f'{self.desc} ' + ''.join(status)
    
    def conclude(self):
        self.done = True


class RecorrentTask(Task):
    def __init__(self,desc,deadline,days=7):
        super().__init__(desc,deadline)
        self.days=days
    
    def conclude(self):
        super().conclude()
        new_deadline= datetime.now() + timedelta(days= self.days)
        return RecorrentTask(self.desc,new_deadline,self.days)

def main():
    home=Project('build a house')
    home.add('build walls',datetime.now()+  timedelta(days=4))
    home.add('make the floor')
    home.add('ceiling')
    home.tasks.append(RecorrentTask('make the bed',datetime.now()+timedelta(days=2),3))
    home.tasks.append(home.search('make the bed').conclude())
    print(home)

    home.search('make the floor').conclude()
    for task in home:
        print(f'-{task}')


if __name__=='__main__':
    main()