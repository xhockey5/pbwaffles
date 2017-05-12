#just try level 1
from manticore import Manticore
import sys

m = Manticore('./NCL-2016-Post-BoomBoom')
m.context['trace'] = []
m.context['input'] = ''
m.context['flag'] = ''

input_addr = 0

# entry point to level one
#get input addr with this hook
@m.hook(0x08048787)
def entry(state):
    """ Get the address where our input is stored. """

    global input_addr
    #eax is a pointer to the input buffer
    input_addr = state.cpu.EAX
    print 'input adr: %s' % hex(input_addr)

    # commented out code was from a different approach
    # create our symbolic input buffer
    #buffer = state.new_symbolic_buffer(0x22)

    #for i, letter in enumerate(answer):
        #state.add(buffer[i] == ord(letter))

    #store the symbolic buffer
    #state.cpu.write_bytes(input_addr, buffer)
    #for i in xrange(0, 0x22):
        #data = state.solve_one(state.cpu.read_int(input_addr + i, 8))
        #m.context['input'] += chr(data)
    #print m.context['input']
#The below hook was the one that crashed the comp after 16 hours
"""
@m.hook(0x08048798)
def entry(state):
    
    tmp = ''
    print 'nailed it.'
    #edx also points to input, try this if esp fails
    #[esp] is a pointer to the input buffer
    esp = state.cpu.ESP
    # have to account for endianess
    for i in xrange(0, 4):
        temp += state.cpu.read_int(esp + i, 8)
    adr = tmp[-2:] + tmp[-4:-2] + tmp[-6:-4] + tmp[-8:-6]
    input_addr = int(adr, 16)
    print 'input adr: %s' % hex(input_addr)
    #from debugger, input_addr was ff916478
    for i in xrange(0, 0x22):
        solved = state.solve_one(state.cpu.read_int(input_addr + i, 8))
        print solved
        m.context['flag'] += chr(solved)
    print(m.context['flag'])
    m.terminate()
"""
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
m.workers = 1
m.verbosity = 1 #1 is normal, go higher for more verbose
#input should be length 35 (0x23) remember the \x00
m.run()
