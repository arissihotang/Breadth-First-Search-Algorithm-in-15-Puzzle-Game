from collections import deque

class Puzzle15:
    def __init__(self, initial_state):
        self.initial_state = initial_state

        self.goal_state = [1, 2, 3, 4,
                           5, 6, 7, 8,
                           9, 10, 11, 12,
                           13, 14, 15, 0]

        self.moves = {'up': -4, 'down': 4, 'left': -1, 'right': 1}

    def solve(self):
        queue = deque()  # 1
        visited = set()  # 1
        queue.append((self.initial_state, []))  # 1
        visited.add(tuple(self.initial_state))  # n

        while queue:
            state, path = queue.popleft()  # 1 * n
            print("state: ", state)  # 1 * n
            state == self.goal_state  # 1 * n

            if state == self.goal_state:
                return path

            empty_tile_index = state.index(0)  # 1 * n

            for move, step in self.moves.items():
                new_index = empty_tile_index + step  # 1 * n * n

                if not self.is_valid_move(empty_tile_index, move):
                    continue

                new_state = self.swap_tiles(state, empty_tile_index, new_index)  # 2 * n * n

                if tuple(new_state) not in visited:
                    queue.append((new_state, path + [move]))  # 1 * n * n
                    visited.add(tuple(new_state))  # n * n * n

            return None

    def is_valid_move(self, empty_tile_index, move):
        if move == 'up' and empty_tile_index < 4:
            return False

        if move == 'down' and empty_tile_index > 11:
            return False

        if move == 'left' and empty_tile_index % 4 == 0:
            return False

        if move == 'right' and (empty_tile_index + 1) % 4 == 0:
            return False

        return True

    def swap_tiles(self, state, index1, index2):  # 2
        new_state = list(state)
        new_state[index1], new_state[index2] = new_state[index2], new_state[index1]

        return new_state
