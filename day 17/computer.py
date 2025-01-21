class Computer:

    def __init__(self):
        self.A, self.B, self.C = 0, 0, 0
        self.program = []
        self.pnt = 0
        self.output = []
    
    def set_program(self, program):
        self.program = program.copy()

    def run(self):
        while self.pnt < len(self.program):
            self.perform_instruction(self.read_val(), self.read_next_val())
            
    
    def get_output(self):
        return self.output

    def move_pnt(self, jumps = 2):
        self.pnt += jumps

    def read_val(self):
        return self.program[self.pnt % len(self.program)]
    
    def read_next_val(self):
        return self.program[(self.pnt + 1 )% len(self.program)]

    def get_A(self):
        return self.A
    
    def get_B(self):
        return self.B
    
    def get_C(self):
        return self.C

    def combo_val(self, val):
        match val:
            case 4:
                return self.get_A()
            case 5:
                return self.get_B()
            case 6:
                return self.get_C()
            case _:
                return val
            
    def perform_instruction(self, opcode, operand):
        match opcode:
            case 0:
                self.adv(operand)
                self.move_pnt()
            case 1:
                self.bxl(operand)
                self.move_pnt()
            case 2:
                self.bst(operand)
                self.move_pnt()
            case 3:
                self.jnz(operand)
            case 4:
                self.bxc(operand)
                self.move_pnt()
            case 5:
                self.out(operand)
                self.move_pnt()
            case 6:
                self.bdv(operand)
                self.move_pnt()
            case 7:
                self.cdv(operand)
                self.move_pnt()

    def adv(self, operand):
        den = 2 ** self.combo_val(operand)
        self.A = int(self.get_A() / den)
    
    def bxl(self, operand):
        self.B = operand ^ self.get_B()

    def bst(self, operand):
        self.B = self.combo_val(operand) % 8
    
    def jnz(self, operand):
        if self.get_A() == 0:
            self.move_pnt()
        else:
            self.pnt = operand
            
    
    def bxc(self, operand):
        self.B = self.get_C() ^ self.get_B()

    def out(self,operand):
        out = self.combo_val(operand) % 8
        #output
        self.output.append(out)

    def bdv(self, operand):
        den = 2 ** self.combo_val(operand)
        self.B = int(self.get_A() / den)

    def cdv(self, operand):
        den = 2 ** self.combo_val(operand)
        self.C = int(self.get_A() / den)

    def reset(self):
        self.A, self.B, self.C = 0, 0, 0
        self.pnt = 0
        self.output = []

    def find_A(self):
        cur = 35184372088832
        while self.output != self.program:
            self.reset()
            self.A = cur
            if self.A % 100000 == 0:
                print(f'checking: {self.A}')
            self.run()
            cur += 1
        return cur-1