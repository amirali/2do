import os
import fire

class Twodo:
    def __init__(self):
        self.file = os.path.join(os.path.expanduser('~'), '.twodo.txt')
        self.undone_sign = '[ ]'
        self.done_sign = '[x]'

        if not os.path.exists(self.file):
            with open(self.file, 'w') as f:
                pass

    
    def add(self, *words):
        line = ' '.join(words)
        with open(self.file, 'a') as f:
            f.writelines('-' + line + '\n')

    def clean(self):
        with open(self.file, 'r') as f:
            tasks = f.read().split('\n')
        
        for i in range(len(tasks)-1):
            if tasks[i][0] == '+':
                del tasks[i]

        with open(self.file, 'w') as f:
            f.write('\n'.join(tasks))

    def delete(self, *tids):
        pass

    def done(self, *tids):
        with open(self.file, 'r') as f:
            tasks = f.read().split('\n')

        for tid in tids:
            tid = int(str(tid).lstrip('0'))
            if tid > len(tasks):
                print("There isn't this todo index")
                return

            tasks[tid-1] = '+' + tasks[tid-1][1:]

        with open(self.file, 'w') as f:
            f.write('\n'.join(tasks))

    def list(self):
        with open(self.file, 'r') as f:
            tasks = f.read().split('\n')

        for i in range(len(tasks)-1):
            if tasks[i][0] == '-':
                print(self.undone_sign + ' ' + str(i+1).zfill(3) + ": " + tasks[i][1:])
            else:
                print(self.done_sign + ' ' + str(i+1).zfill(3) + ": " + tasks[i][1:])

    def sort(self):
        with open(self.file, 'r') as f:
            tasks = f.read().split('\n')

        del tasks[-1]
        tasks.sort()

        with open(self.file, 'w') as f:
            f.write('\n'.join(tasks) + '\n')

    def undone(self, *tids):
        with open(self.file, 'r') as f:
            tasks = f.read().split('\n')

        for tid in tids:
            tid = int(str(tid).lstrip('0'))
            if tid > len(tasks):
                print("There isn't this todo index")
                return

            tasks[tid-1] = '-' + tasks[tid-1][1:]

        with open(self.file, 'w') as f:
            f.write('\n'.join(tasks))

def main():
    fire.Fire(Twodo)

if __name__ == "__main__":
    fire.Fire(Twodo)
