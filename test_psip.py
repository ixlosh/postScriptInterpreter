import psip

def test_add_operation():
    psip.op_stack.clear()
    psip.process_input("1")
    psip.process_input("2")
    psip.process_input("add")
    assert psip.op_stack[-1] == 3

def test_lookup_operation():
    psip.op_stack.clear()
    psip.process_input("/x")
    psip.process_input("2")
    psip.process_input("def")
    psip.process_input("x")
    assert psip.op_stack[-1] == 2

def test_exch_operation():
    psip.op_stack.clear()
    psip.process_input("1")
    psip.process_input("2")
    psip.process_input("exch")
    assert psip.op_stack[-1] == 1
    assert psip.op_stack[-2] == 2

def test_pop_operation():
    psip.op_stack.clear()
    psip.process_input("5")
    psip.process_input("6")
    psip.process_input("pop")
    assert psip.op_stack[-1] == 5

def test_copy_operation():
    psip.op_stack.clear()
    psip.process_input("1")
    psip.process_input("2")
    psip.process_input("3")
    psip.process_input("3")
    psip.process_input("copy")

    assert psip.op_stack[-1] == 3
    assert psip.op_stack[-2] == 2
    assert psip.op_stack[-3] == 1
    assert psip.op_stack[-4] == 3
    assert psip.op_stack[-5] == 2
    assert psip.op_stack[-6] == 1

def test_dup_operation():
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("dup")
    assert psip.op_stack[-1] == 10
    assert psip.op_stack[-2] == 10

def test_clear_operation():
    psip.op_stack.clear()
    psip.process_input("1")
    psip.process_input("2")
    psip.process_input("3")
    psip.process_input("clear")
    psip.process_input("=")
    assert len(psip.op_stack) == 0

def test_count_operation():
    psip.op_stack.clear()
    psip.process_input("1")
    psip.process_input("2")
    psip.process_input("count")
    psip.process_input("=")
    assert psip.op_stack[-1] == 2

def test_div_operation():
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("5")
    psip.process_input("div")
    assert psip.op_stack[-1] == 2
