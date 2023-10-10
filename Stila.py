from intoExep import ErrorWithInfo
class stilla :
    def __init__(self, N, C, free_slot):
        self.N = N
        self.C = C
        self.free_slot = free_slot

    def checker(self):
        if((len(self.free_slot) < 2) or (self.N < self.C) or (self.C > len(self.free_slot)) or (self.C < 2) ):
            raise ErrorWithInfo

        for i in self.free_slot:
            if (i <= 0):
                raise ErrorWithInfo

    def angry_cov(self):


        if (len(self.free_slot) > 2 and len(self.free_slot) > self.C and self.C > 2):

            emp_slot = self.sort_func(self.free_slot)
            ang_slot = [[]]
            step = 0


            while True:
                curr = []
                step += 1
                angry_cov = self.C - 1
                curr.append(emp_slot[0])

                for i in emp_slot :
                    if((curr[len(curr) - 1] + step < i) and (angry_cov > 0)):
                        curr.append(i)
                        angry_cov -= 1

                if(angry_cov > 0):
                    break

                ang_slot.append(curr)
                print(ang_slot[len(ang_slot) - 1])

            return ang_slot
        else:
            raise ErrorWithInfo

    def sort_func(self, arr_to_sort):
        arr = arr_to_sort

        if(len(arr) < 1):
            return arr

        else:
            pivot = arr[len(arr) // 2]

            left = [i for i in arr if i < pivot]
            middle = [i for i in arr if i == pivot]
            right = [i for i in arr if i > pivot]

            return self.sort_func(left) + middle + self.sort_func(right)


    def find_all_min(self, big_arr):
        min_save_val = []
        for i in big_arr:

            curr_int = 0
            all_val = []
            if len(i) > 2:
                for n in range(1, len(i)):
                    if n == 1:
                        min = i[n] - i[n-1]
                    curr_int = i[n] - i[n-1]

                    if(min > curr_int):
                        min = curr_int
                min_save_val.append(min)
        return min_save_val
    def finaly_cal(self):
        try:
            self.checker();

        except ErrorWithInfo as e:
            return e
        else:
            try:
                all_min = self.find_all_min(self.angry_cov())
            except ErrorWithInfo as exp:
                return exp
            else:
                result = 0
                for i in all_min:
                    if (result < i):
                        result = i
                return result


