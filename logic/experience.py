class Xp:
    def __init__(self, max_level=10):
        self.now_xp = 0
        self.now_level = 1
        self.max_level = max_level
        self.xp_cap = 10
        self.current_xp_cap = 10
        self.xp_multiplier = 1
        self.create_fibi()

    def next_level(self):
        if self.now_level + 1 <= self.max_level:
            self.now_level += 1
            self.now_xp = self.now_xp - self.current_xp_cap
            self.current_xp_cap = self.calculate_new_xp_cap()
        else:
            self.now_xp = self.current_xp_cap

    def calculate_new_xp_cap(self) -> int:
        return self.xp_cap * self.fibi[self.now_level - 1]

    def add_xp(self, amount: int) -> None:
        self.now_xp += amount
        if self.now_xp >= self.current_xp_cap:
            self.next_level()

    def create_fibi(self) -> None:
        a = 0
        b = 1
        self.fibi = []
        for _ in range(self.max_level):
            result = a + b
            a = b
            b = result
            self.fibi.append(result)
