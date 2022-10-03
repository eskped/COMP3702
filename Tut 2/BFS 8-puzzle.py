# from mimetypes import init
import numpy as np
import datetime
import queue as queuelib

class PuzzleState():
    def __init__(self, istate, shape):
        self.actionset = ['L', 'R', 'U', 'D']
        self.shape = shape; order = 'C'
        if isinstance(istate, np.ndarray):
            self.mat = istate
            str_state = ''.join([str(i) for i in np.ravel(self.mat, order=order).tolist()])
            self.id = str_state.replace('0', '_')
        else:
            self.id = istate
            state = [int(i) for i in istate.replace('_','0')]
            self.mat = np.asarray(state).reshape(shape, order=order)
    
    def is_equal(self, anystate):
        return np.array_equal(self.mat, anystate.mat)
    
    def get_neighbourlist(self):
        neighbourlist = []
        for action in self.actionset:
            neighbour = self._step(action)
            neighbourlist.append((neighbour, action))
        return neighbourlist
    
    def _step(self, action):
        def _inc(row, col, action):
            if action == 'L':
                col = max(col-1, 0)
            elif action == 'R':
                col = max(col+1, ncol-1)
            elif action == 'U':
                row = max(row-1,0)
            elif action == 'D':
                row = min(row+1, nrow-1)
            else: 
                raise NotImplementedError(a)
            return (row, col)
        
        nrow, ncol = self.shape
        ipos = np.where(self.mat==0) # i: intial pos of 0
        fpos = _inc(ipos[0], ipos[1], action) # f: final pos of 0
        snext = np.copy(self.mat)
        print(nrow, ncol)
        print("\n")
        print(ipos)
        print("\n")
        print(fpos)
        print("\n")
        print(snext)
        snext[ipos] = self.mat[fpos]
        snext[fpos] = self.mat[ipos]
        return PuzzleState(snext, self.shape)
    
    def get_parity(self):
        flat = self.mat.flatten(order='C')
        n_invs = [0]*len(flat)
        for i, inum in enumerate(flat):
            if inum == 0:
                continue
            for j, jnum in enumerate(flat[i+1:]):
                if jnum == 0:
                    continue
                if jnum < inum:
                    n_invs[inum] += 1
        print(n_invs)
        parity = sum(n_invs)%2
        return parity
    
    
def bfs(start, goal):
        visited = set() # need hashable objects!
        queue = queuelib.Queue()
        queue.put((start, []))
        while queue.qsize() > 0:
            current, path = queue.get()
            visited.add(current.id)
            
            for neighbor, action in current.get_neighbourlist():
                if neighbor.is_equal(goal):
                    return path + [action]
                if neighbor.id in visited:
                    continue
                queue.put((neighbor, path + [action]))
        return None
    
if __name__ == '__main__':
    start = PuzzleState('12345678_', (3,3))
    goal = PuzzleState('1234567_8', (3,3))
    
    time_begin = datetime.datetime.now()
    path = bfs(start,goal)
    time_end = datetime.datetime.now()
    print('path bfs', path)

    

