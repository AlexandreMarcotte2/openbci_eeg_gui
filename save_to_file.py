import threading
import numpy as np
from time import sleep

class WriteDataToFile(threading.Thread):
    def __init__(self, data_queue, n_val_created, lock):
        super(WriteDataToFile, self).__init__()
        self.n_val_created = n_val_created
        self.data_queue = data_queue
        self.N_DATA = len(self.data_queue[0])
        self.lock = lock
        # self.written_to_file = False

    def run(self):
        self.write_to_file()

    def write_to_file(self):
        while 1:
            sleep(0.001)
            # print(self.n_val_created)
            if self.n_val_created[0] % self.N_DATA == 0:
                self.lock.acquire()
                with open('csv_eeg_data.csv', 'a') as f:
                    # print('write to file...')
                    np.savetxt(f, np.transpose(self.data_queue), delimiter=',')
                self.lock.release()