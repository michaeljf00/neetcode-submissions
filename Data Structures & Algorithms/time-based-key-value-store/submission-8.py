class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.timemap:
            return ''

        time_list = self.timemap[key]
        left, right = 0, len(self.timemap[key])-1

        res = ''
        while left <= right:
            mid = (left + right) // 2
            time, value = time_list[mid]

            if time <= timestamp:
                res = value
                left = mid + 1
            else:
                right = mid - 1
            
        return res
