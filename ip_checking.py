class NextIP(object):
    max = 255

    def __init__(self, start_ip, end_ip):
        self.start_ip = [int(i) for i in start_ip.split(".")]
        self.end_ip = [int(i) for i in end_ip.split(".")]
        self.start_ip.reverse()
        self.end_ip.reverse()

    def __iter__(self):
        return self

    def _check(self):
        check = list()
        a_list = list(reversed(self.start_ip))
        b_list = list(reversed(self.end_ip))

        for i in range(4):
            a = a_list[i]
            b = b_list[i]

            if a >= b:
                check.append(True)
            else:
                check.append(False)

            if all(check) and  a > b:
                raise StopIteration

    def _add(self):
        zero = False
        for i in range(4):
            current = self.start_ip[i]
            if zero:
                self.start_ip[i] += 1
                zero = False

            if current >= self.max:
                self.start_ip[i] = 0
                self.zero = True
            else:
                self.start_ip[i] += 1
                break

    def _get_next_ip(self):
        result = reversed(self.start_ip)
        return ".".join([str(i) for i in result])

    def __next__(self):
        self._add()
        self._check()
        return self._get_next_ip()

