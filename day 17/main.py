from computer import Computer

C = Computer()

C.A = 32916674
C.B = 0
C.C = 0
C.set_program([2,4,1,1,7,5,0,3,1,4,4,0,5,5,3,0])


C.run()
print(f'''
A: {C.A}
B: {C.B}
C: {C.C}
out: {C.output}''')

print(f'ans: {str(C.output).replace(' ','')}')