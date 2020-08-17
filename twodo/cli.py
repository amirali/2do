import os
import fire

class Twodo:
    def __init__(self):
        self.file = os.path.join(os.path.expanduser('~'), '.twodo.txt')
    
    def add(self, *words):
        pass

    def clean(self):
        pass

    def delete(self, tid):
        pass

    def done(self, tid):
        pass

    def list(self):
        pass

    def sort(self):
        pass

    def undone(self, tid):
        pass

def main():
    fire.Fire(Twodo)

if __name__ == "__main__":
    fire.Fire(Twodo)
