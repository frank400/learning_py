class Car:
    def __init__(self,max_speed):
        self.speed=0
        self.max_speed=max_speed
    
    def accelerate(self,acceleration):
        if self.speed+acceleration >180:
            self.speed=180
        else:
            self.speed += acceleration
        return self.speed

    def breaking(self,delta=0):
        if self.speed-delta <0:
            self.speed=0
        else:
            self.speed -= delta
        return self.speed

if __name__=='__main__':
    c1=Car(180)

    for _ in range(25):
        print(c1.accelerate(8))
        if c1.speed==180:
            break
    
    for _ in range(10):
        print(c1.breaking(delta=20))
        if c1.speed==0:
            break
