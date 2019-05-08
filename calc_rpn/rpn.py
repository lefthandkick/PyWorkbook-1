import sys
import io


class HpCalc:
    """
    Using are few ways to use the class's methods to replace the
    if operation.  I'm looking
    for ways to make the logic work as if a HP calcs
    """
    def __init__(self):
        self.keyb_in = ' '
        self.f_in = 0.0
        self.stack_A = [0.0, 0.0]
        self.stack_B = [0.0, 0.0]
        self.func_map = self.init_operator_map()

    def init_operator_map(self):
        _func_map = {}
        # self.func_map.append({'+': self.add_it})
        _func_map.update({'+': self.add_it})
        _func_map.update({'-': self.sub_it})
        _func_map.update({'*': self.mul_it})
        _func_map.update({'/': self.div_it})
        return _func_map

    def scrub_keyb_in(self, keyIn: str) -> bool:
        try:
            self.f_in = float(keyIn)
            return True
        except (ValueError, TypeError) as err:
            print(err)
            return False



    def push_stack(self, keyIn):
        if self.scrub_keyb_in(keyIn):
            self.stack_A.append(self.f_in)
            self.print_stack()
        else:
            pass

    def pop_stack(self, count):
        v1, v2, v3, v4 = [0.0, 0.0, 0.0, 0.0]
        retBuf = []
        # get the last two numbers
        if len(self.stack_A) > count - 1:
            retBuf = self.stack_A[(-1 * count):]
            # need to replace with delete count
            v3 = self.stack_A.pop()
            v4 = self.stack_A.pop()
            # print(f'Retv {retBuf}')
            return retBuf
        else:
            return (v2, 0)

        # return (6, 6)
        # v1, v2 = self.stack_A[-2:]
        # # Could use for calc but wanted to try the destructure too
        # v3 = self.stack_A.pop()
        # v4 = self.stack_A.pop()

    def clear_stack(self):
        self.stack.clear()
        self.stack = [0.0, 0.0]
        self.print_stack()

    def get_stack(self):
        pass

    # def print_stack(self):
    #     print(f'Stack-B <<: {self.stack_B}')
    #     print(f'Stack-A >>: {self.stack_A}')

    def binary_operation(self):
        v1, v2 = self.pop_stack(2)
        if v1 == 0.0:
            pass
        else:
            # clear and copy pre stack B
            self.stack_B.clear()
            self.stack_B = self.stack_A[:]
            return (v1, v2)

    def div_it(self):
        pass

    def mul_it(self):
        pass

    def sub_it(self):
        print('sub operation')

    def add_it(self):
        op1, op2 = self.binary_operation()
        self.stack_A.append(op1 + op2)
        self.print_stack()


def myName(name: str, age: int) -> int:
    return age


def calc_loop():
    # make the calculator
    hp = HpCalc()

    while hp.keyb_in != 'Z':
        hp.keyb_in = input('Enter #: ')
        #
        # is the value_in v_in an operator?  If so do the operation
        #
        if hp.keyb_in in hp.func_map:
            # this syntax executed the function associated with
            # the operations key
            print(f'Stack-A : {hp.stack_A}')

            (hp.func_map[hp.keyb_in])()

            # print(f'Stack-A : {hp.stack_A}')
        else:
            hp.push_stack(hp.keyb_in)


if __name__ == "__main__":
    calc_loop()
