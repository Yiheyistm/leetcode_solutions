class MapSum:

    def __init__(self):
        self.root = {}
        self.dict_map = defaultdict(int)      

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        for ch in key:
            if ch not in curr:
                curr[ch] = {}
            curr["val"] = curr.get("val", 0) + val - self.dict_map[key]
            curr = curr[ch]
        curr["val"] = curr.get("val", 0) + val - self.dict_map[key]
        self.dict_map[key] = val
        
        

    def sum(self, prefix: str) -> int:
        total = 0
        curr = self.root
        for ch in prefix:
            if ch not in curr:
                return 0
            curr = curr[ch]
        return curr["val"]
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)