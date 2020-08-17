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
        pass

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
