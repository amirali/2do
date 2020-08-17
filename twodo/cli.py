import os
import fire

class Twodo:
    def __init__(self):
        self.file = os.path.join(os.path.expanduser('~'), '.twodo.txt')

        if not os.path.exists(self.file):
            with open(self.file, 'w') as f:
                pass

    
    def add(self, *words):
        line = ' '.join(words)
        with open(self.file, 'a') as f:
            f.writelines('-' + line + '\n')

    def clean(self):
        with open(self.file, 'r') as f:
            todos = f.read().split('\n')
        
        for i in range(len(todos)-1):
            if todos[i][0] == '+':
                del todos[i]

        with open(self.file, 'w') as f:
            f.write('\n'.join(todos))

    def delete(self, *tids):
        pass

    def done(self, *tids):
        pass

    def list(self):
        pass

    def sort(self):
        pass

    def undone(self, *tids):
        pass

def main():
    fire.Fire(Twodo)

if __name__ == "__main__":
    fire.Fire(Twodo)
