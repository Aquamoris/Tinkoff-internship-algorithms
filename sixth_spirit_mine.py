def sixth_task():
    class Ghost:
        def __init__(self, id, band, band_count):
            self.id = id
            self.band = band
            self.band_count = band_count

        def __repr__(self):
            return repr(f'{self.id} {self.band} {self.band_count}')

    first = list(map(int, input().split()))
    n, m = first[0], first[1]

    ghosts = []
    for i in range(n):
        ghosts.append(Ghost(i+1, {i+1}, 1))

    for i in range(m):
        response = list(map(int, input().split()))
        response_type = response[0]
        if response_type == 1:
            ghost_1 = ghosts[response[1] - 1]
            ghost_2 = ghosts[response[2] - 1]

            if ghost_2.id in ghost_1.band:
                continue
            else:
                ghost_1.band.add(ghost_2.id)
                ghost_2.band.add(ghost_1.id)
                ghost_1.band_count += 1
                ghost_2.band_count += 1

                new_band = ghost_1.band | ghost_2.band

                for ghost_id in new_band:
                    if ghost_id != response[1] and ghost_id != response[2]:
                        ghosts[ghost_id - 1].band = new_band
                        ghosts[ghost_id - 1].band_count += 1

                ghost_1.band = new_band
                ghost_2.band = new_band
        elif response_type == 2:
            ghost_1 = ghosts[response[1] - 1]
            ghost_2 = ghosts[response[2] - 1]

            print('YES') if ghost_2.id in ghost_1.band else print('NO')
        else:
            ghost_to_count = ghosts[response[1] - 1]
            print(ghost_to_count.band_count)


if __name__ == '__main__':
    sixth_task()