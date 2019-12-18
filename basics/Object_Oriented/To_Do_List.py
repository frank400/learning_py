from datetime import datetime,timedelta

class Unfound_task(Exception):
    pass

class Project:
    def __init__(self,name):
        self.name=name
        self.tasks=[]

    def __iter__(self):
        return self.tasks.__iter__()
    
    def __str__(self):
        return f'{self.name} ({len(self.pendent())} undone task(s))'
    
    def __iadd__(self,task):
        task.owner=self
        self._add_task(task)
        return self

    def _add_task(self,task,**kwargs):
        self.tasks.append(task)
    
    def _add_new_task(self,desc,**kwargs):
        self.tasks.append(Task(desc,kwargs.get('deadline',None)))

    def add(self,task,deadline =None,**kwargs):
        choosed_task=self._add_task if isinstance(task,Task) else self._add_new_task
        kwargs['deadline']=deadline
        choosed_task(task,**kwargs)
        
    def pendent(self):
        return [task for task in self.tasks if not task.done]
    
    def search(self,desc):
        try:
            return [task for task in self.tasks
                    if task.desc==desc][-1]
        except IndexError as e:
            raise Unfound_task(str(e))


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
        self.owner=None
    
    def conclude(self):
        super().conclude()
        new_deadline= datetime.now() + timedelta(days= self.days)
        new_task=RecorrentTask(self.desc,new_deadline,self.days)
        if self.owner:
            self.owner += new_task
        return new_task

def main():
    home=Project('build a house')

    home.add('build walls',datetime.now()+  timedelta(days=4))
    home.add('make the floor')
    home.add('ceiling')

    home += RecorrentTask('make the bed',datetime.now(),3)
    try:
        home.search('make the bed').conclude()
    except Unfound_task as e:
        print (f'the cause of problem was {str(e)}')
    print(home)

    #



    home.search('make the floor').conclude()
    for task in home:
        print(f'-{task}')


if __name__=='__main__':
    main()