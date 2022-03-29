#create one function to partition an array in two halves and the further into two halves
#play on index so that original array can be passed and updated
#create another function which receives indexes and sorts them
#the advantage is that original array is updated.. so no need to manage different variables

class MergeSort:
    '''Performs Merge Sort'''
    def __init__(self, seq):
        self.seq = seq

    def __merge(self, sta, mid, end):
        #program to merge/sort and update

        point_a = sta
        point_b = mid+1
        t_a = []
        while point_a <= mid and point_b <= end:
            if self.seq[point_a] > self.seq[point_b]:
                while (point_a <= mid and point_b <= end) and (self.seq[point_a] > self.seq[point_b]) :
                    t_a.append(self.seq[point_b])
                    point_b+=1                
            else:
                t_a.append(self.seq[point_a])
                point_a+=1
                # point_b+=1
        while point_a <=mid:
            t_a.append(self.seq[point_a])
            point_a+=1
        while point_b <= end:
            t_a.append(self.seq[point_b])
            point_b+=1

        self.seq[sta:end+1] = t_a.copy()

    def __partition(self, sta, end):
        #program to partition the sequence into two
        # print(sta, end)
        if sta < end:
            mid = (sta + end)//2

            self.__partition(sta, mid)
            self.__partition(mid+1, end)
            self.__merge(sta, mid, end)

    def sort(self):
        '''driver function'''
        self.__partition(0, len(self.seq) - 1)
        return self.seq

arr = [2,1,3,4,5,2,3,1,5,6,3,2,3,45,3,23,4,41,1]

ms = MergeSort(arr)

print(ms.sort())
