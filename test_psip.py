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

def test_sub_operation():
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("5")
    psip.process_input("sub")
    assert psip.op_stack[-1] == 5

def test_idiv_operation():
    psip.op_stack.clear()
    psip.process_input("5.7")
    psip.process_input("2.3")
    psip.process_input("idiv")
    assert psip.op_stack[-1] == 2

def test_mul_operation():
    psip.op_stack.clear()
    psip.process_input("2")
    psip.process_input("5")
    psip.process_input("mul")
    assert psip.op_stack[-1] == 10

def test_abs_operation():
    psip.op_stack.clear()
    psip.process_input("-5")
    psip.process_input("abs")
    assert psip.op_stack[-1] == 5

def test_neg_operation():
    psip.op_stack.clear()
    psip.process_input("5")
    psip.process_input("neg")
    assert psip.op_stack[-1] == -5

def test_ceiling_operation():
    psip.op_stack.clear()
    psip.process_input("9.3")
    psip.process_input("ceiling")
    assert psip.op_stack[-1] == 10

def test_floor_operation():
    psip.op_stack.clear()
    psip.process_input("9.3")
    psip.process_input("floor")
    assert psip.op_stack[-1] == 9

def test_round_operation():
    psip.op_stack.clear()
    psip.process_input("876.5")
    psip.process_input("round")
    assert psip.op_stack[-1] == 877

def test_sqrt_operation():
    psip.op_stack.clear()
    psip.process_input("9")
    psip.process_input("sqrt")
    assert psip.op_stack[-1] == 3

def test_dict_operation():
    psip.op_stack.clear()
    psip.process_input("3")
    psip.process_input("dict")
    result = psip.op_stack[-1]
    assert isinstance(result, dict)
    assert len(result) == 3

def test_length_operation():
    psip.op_stack.clear()
    psip.process_input("5")
    psip.process_input("dict")
    psip.process_input("/key1 1 def")
    psip.process_input("/key2 2 def")
    psip.process_input("/key3 3 def")
    psip.process_input("/key4 4 def")
    psip.process_input("length")
    assert psip.op_stack[-1] == 4

def test_maxlength_operation():
    psip.op_stack.clear()
    psip.process_input("5")
    psip.process_input("dict")
    psip.process_input("/key1 1 def")
    psip.process_input("/key2 2 def")
    psip.process_input("/key3 3 def")
    psip.process_input("/key4 4 def")
    psip.process_input("maxlength")
    assert psip.op_stack[-1] == 5

def test_begin_and_end_operations():
    psip.op_stack.clear()
    psip.process_input("begin") # Extra Dict No 1 begin
    psip.process_input("/key1 104 def")
    psip.process_input("begin") # Extra Dict No 2 begin
    psip.process_input("/key2 205 def")
    psip.process_input("begin") # Extra Dict No 3 begin
    psip.process_input("/key3 306 def")

    assert len(psip.dict_stack) == 3
    assert "/key3" in psip.dict_stack[-1]
    assert "/key2" in psip.dict_stack[-2]
    assert "/key1" in psip.dict_stack[-3]

    psip.process_input("end") # Extra Dict No 3 end
    assert len(psip.dict_stack) == 2
    assert "/key3" not in psip.dict_stack[-1]
    assert "/key2" in psip.dict_stack[-1]
    assert "/key1" in psip.dict_stack[-2]

    psip.process_input("end") # Extra Dict No 2 end
    assert len(psip.dict_stack) == 1
    assert "/key2" not in psip.dict_stack[-1]
    assert "/key1" in psip.dict_stack[-1]

    psip.process_input("end") # Extra Dict No 1 end
    assert len(psip.dict_stack) == 1 # Only the global dict is left

    try:
        psip.process_input("end") # Then we test to see if we can invoke end again ...
        assert False
    except psip.TypeMismatch: # ... and pass the test if we can't!
        pass

def test_def_operation():
    psip.op_stack.clear()
    
    psip.process_input("/key1 10 def")
    assert "/key1" in psip.dict_stack[-1]
    assert psip.dict_stack[-1]["key1"] == 10
    
    psip.process_input("/key2 20 def")
    assert "/key2" in psip.dict_stack[-1]
    assert psip.dict_stack[-1]["key2"] == 20
