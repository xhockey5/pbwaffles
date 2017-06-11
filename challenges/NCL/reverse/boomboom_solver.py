#just try level 1
from manticore import Manticore
import sys

m = Manticore('./NCL-2016-Post-BoomBoom')
m.context['trace'] = []
m.context['input'] = ''
m.context['flag'] = ''

input_addr = 0

@m.hook(0x08048643)
def jump_to_level_2(state):
    state.cpu.EIP = 134514263 #0x0804863F

@m.hook(0x0804879D)
def get_input_addr(state):
    ebp = state.cpu.EBP
    global input_addr
    if type(ebp) == int:
        input_addr = ebp + 32
        print 'input_addr: %s' % hex(input_addr)

@m.hook(0x080487E8)
def passed(state):

    global input_addr
    solution = ''
    print 'made it'
    for i in xrange(0xc):
        sym_char = state.cpu.read_int(input_addr+i, 8)
        concrete_char = state.solve_one(sym_char)
        solution += chr(concrete_char)
    print solution
    m.terminate()

@m.hook(0x080487D9)
def fail(state):
    print 'Bad path, abandoning'
    state.abandon()

def level_one():
    @m.hook(0x08048643)
    def entry(state):
        """ Get the address where our input is stored. In main() """

        global input_addr
        #eax is a pointer to the input buffer
        if type(state.cpu.EAX) == int:
            input_addr = state.cpu.EAX
            print hex(input_addr)

        # create our symbolic input buffer
        buffer = state.new_symbolic_buffer(0x23)

        #store the symbolic buffer
        state.cpu.write_bytes(input_addr, buffer)
    @m.hook(0x0804864B)
    def level_two(state):
        """This can only happen if the first level passed"""
        print 'Reached level 2 somehow'

    # success path
    @m.hook(0x08048798)
    def hook(state):
        """ If pc gets here that means we passed the strcmp. Print out the input manticore used
        to get here. """

        print 'Correct!!!'
        # use the input addr found in an earlier hook
        global input_addr
        solution = ''
        #dref esp
        for i in xrange(0x30):
            sym_char = state.cpu.read_int(input_addr + i, 8)
            concrete_char = state.solve_one(sym_char)
            solution += chr(concrete_char)
        print solution
        m.terminate()
        # do stuff


    # fail path
    @m.hook(0x08048793)
    def hook(state):
        """ If pc gets here that means we failed the strcmp comparison. This state must be abandoned.
        For debug, print out the input manticore used."""

        global input_addr
        input_str = ''
        print 'Baddddd, abandoning'
        state.abandon()
#this might multithread it?
m.workers = 2
m.verbosity = 1 #1 is normal, go higher for more verbose
#input should be length 35 (0x23) with the null terminator
m.run()
