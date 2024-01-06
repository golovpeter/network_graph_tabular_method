class Row:
    def __init__(
            self,
            first_work,
            second_work,
            time_work,
    ):
        self.first_work = first_work
        self.second_work = second_work
        self.time_work = time_work

        self.early_start = 0
        self.early_end = 0
        self.later_start = 0
        self.later_end = 0
        self.local_reserve = 0
        self.general_reserve = 0

    def show_row(self):
        print(
            self.first_work,
            self.second_work,
            self.time_work,
            self.early_start,
            self.early_end,
            self.later_start,
            self.later_end,
            self.general_reserve,
            self.local_reserve,
        )
