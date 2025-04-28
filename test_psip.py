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
    psip.process_input("876.9")
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
    assert psip.dict_stack[-1]["capacity"] == 3
    psip.process_input("end")

def test_length_operation():
    psip.op_stack.clear()

    psip.process_input("/mini")
    psip.process_input("length")
    assert psip.op_stack[-1] == 4
    
    psip.process_input("/project")
    psip.process_input("length")
    assert psip.op_stack[-1] == 7
    
    psip.op_stack.clear()

    psip.process_input("begin")
    psip.process_input("/key1 10 def")
    psip.process_input("/key2 20 def")
    psip.process_input("length")
    assert psip.op_stack[-1] == 2
    psip.process_input("end")

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
    psip.process_input("end")

def test_begin_and_end_operations():
    psip.op_stack.clear()
    psip.process_input("begin") # Extra Dict No 1 begin
    psip.process_input("/key1 104 def")
    psip.process_input("begin") # Extra Dict No 2 begin
    psip.process_input("/key2 205 def")
    psip.process_input("begin") # Extra Dict No 3 begin
    psip.process_input("/key3 306 def")

    assert len(psip.dict_stack) == 4
    assert "key3" in psip.dict_stack[-1]
    assert "key2" in psip.dict_stack[-2]
    assert "key1" in psip.dict_stack[-3]

    psip.process_input("end") # Extra Dict No 3 end
    assert len(psip.dict_stack) == 3
    assert "key3" not in psip.dict_stack[-1]
    assert "key2" in psip.dict_stack[-1]
    assert "key1" in psip.dict_stack[-2]

    psip.process_input("end") # Extra Dict No 2 end
    assert len(psip.dict_stack) == 2
    assert "key2" not in psip.dict_stack[-1]
    assert "key1" in psip.dict_stack[-1]

    psip.process_input("end") # Extra Dict No 1 end
    assert len(psip.dict_stack) == 1 # Only the global dict is left

def test_def_operation():
    psip.op_stack.clear()
    
    psip.process_input("/key1 10 def")
    assert "key1" in psip.dict_stack[-1]
    assert psip.dict_stack[-1]["key1"] == 10
    
    psip.process_input("/key2 20 def")
    assert "key2" in psip.dict_stack[-1]
    assert psip.dict_stack[-1]["key2"] == 20

def test_get_operation():
    psip.op_stack.clear()
    
    psip.process_input("/first")
    psip.process_input("3")
    psip.process_input("get")
    assert psip.op_stack[-1] == "/s"
    
    psip.process_input("/mini")
    psip.process_input("0")
    psip.process_input("get")
    assert psip.op_stack[-1] == "/m"

def test_getinterval_operation():
    psip.op_stack.clear()
    
    psip.process_input("/first_mini_project")
    psip.process_input("0")
    psip.process_input("5")
    psip.process_input("getinterval")
    assert psip.op_stack[-1] == "/first"
    
    psip.process_input("/first_mini_project")
    psip.process_input("11")
    psip.process_input("7")
    psip.process_input("getinterval")
    assert psip.op_stack[-1] == "/project"

def test_putinterval_operation():
    psip.op_stack.clear()
    
    psip.process_input("/first_mini")
    psip.process_input("6")
    psip.process_input("/project")
    psip.process_input("putinterval")
    assert psip.op_stack[-1] == "/first_project"
    
    psip.process_input("/first_project")
    psip.process_input("0")
    psip.process_input("/miniq")
    psip.process_input("putinterval")
    assert psip.op_stack[-1] == "/miniq_project"

def test_eq_operation():
    psip.op_stack.clear()
    
    psip.process_input("1")
    psip.process_input("1")
    psip.process_input("eq")
    assert psip.op_stack[-1] == True
    
    psip.process_input("/project")
    psip.process_input("/projectio")
    psip.process_input("eq")
    assert psip.op_stack[-1] == False

def test_ne_operation():
    psip.op_stack.clear()
    
    psip.process_input("1")
    psip.process_input("1")
    psip.process_input("ne")
    assert psip.op_stack[-1] == False
    
    psip.process_input("/project")
    psip.process_input("/projectio")
    psip.process_input("ne")
    assert psip.op_stack[-1] == True

def test_ge_operation():
    psip.op_stack.clear()
    
    psip.process_input("1")
    psip.process_input("2")
    psip.process_input("ge")
    assert psip.op_stack[-1] == False
    
    psip.process_input("2")
    psip.process_input("1")
    psip.process_input("ge")
    assert psip.op_stack[-1] == True
    
    psip.process_input("/a")
    psip.process_input("/b")
    psip.process_input("ge")
    assert psip.op_stack[-1] == False
    
    psip.process_input("/b")
    psip.process_input("/a")
    psip.process_input("ge")
    assert psip.op_stack[-1] == True

def test_gt_operation():
    psip.op_stack.clear()
    
    psip.process_input("1")
    psip.process_input("2")
    psip.process_input("gt")
    assert psip.op_stack[-1] == False
    
    psip.process_input("2")
    psip.process_input("1")
    psip.process_input("gt")
    assert psip.op_stack[-1] == True
    
    psip.process_input("/a")
    psip.process_input("/b")
    psip.process_input("gt")
    assert psip.op_stack[-1] == False
    
    psip.process_input("/b")
    psip.process_input("/a")
    psip.process_input("gt")
    assert psip.op_stack[-1] == True

def test_le_operation():
    psip.op_stack.clear()
    
    psip.process_input("1")
    psip.process_input("2")
    psip.process_input("le")
    assert psip.op_stack[-1] == True
    
    psip.process_input("2")
    psip.process_input("1")
    psip.process_input("le")
    assert psip.op_stack[-1] == False
    
    psip.process_input("/a")
    psip.process_input("/b")
    psip.process_input("le")
    assert psip.op_stack[-1] == True
    
    psip.process_input("/b")
    psip.process_input("/a")
    psip.process_input("le")
    assert psip.op_stack[-1] == False

def test_lt_operation():
    psip.op_stack.clear()
    
    psip.process_input("1")
    psip.process_input("2")
    psip.process_input("lt")
    assert psip.op_stack[-1] == True
    
    psip.process_input("2")
    psip.process_input("1")
    psip.process_input("lt")
    assert psip.op_stack[-1] == False
    
    psip.process_input("/a")
    psip.process_input("/b")
    psip.process_input("lt")
    assert psip.op_stack[-1] == True
    
    psip.process_input("/b")
    psip.process_input("/a")
    psip.process_input("lt")
    assert psip.op_stack[-1] == False

def test_and_operation():
    psip.op_stack.clear()
    
    psip.process_input("true")
    psip.process_input("false")
    psip.process_input("and")
    assert psip.op_stack[-1] == False
    
    psip.process_input("true")
    psip.process_input("true")
    psip.process_input("and")
    assert psip.op_stack[-1] == True

    psip.process_input("1")
    psip.process_input("1")
    psip.process_input("and")
    assert psip.op_stack[-1] == 1

    psip.process_input("1")
    psip.process_input("2")
    psip.process_input("and")
    assert psip.op_stack[-1] == 0

def test_not_operation():
    psip.op_stack.clear()
    
    psip.process_input("true")
    psip.process_input("not")
    assert psip.op_stack[-1] == False
    
    psip.process_input("false")
    psip.process_input("not")
    assert psip.op_stack[-1] == True
    
    psip.process_input("1")
    psip.process_input("not")
    assert psip.op_stack[-1] == -2
    
    psip.process_input("2")
    psip.process_input("not")
    assert psip.op_stack[-1] == -3

def test_or_operation():
    psip.op_stack.clear()
    
    psip.process_input("true")
    psip.process_input("false")
    psip.process_input("or")
    assert psip.op_stack[-1] == True
    
    psip.process_input("false")
    psip.process_input("false")
    psip.process_input("or")
    assert psip.op_stack[-1] == False
    
    psip.process_input("0")
    psip.process_input("1")
    psip.process_input("or")
    assert psip.op_stack[-1] == 1

    psip.process_input("2")
    psip.process_input("3")
    psip.process_input("or")
    assert psip.op_stack[-1] == 3

def test_if_operation():
    psip.op_stack.clear()
    
    psip.process_input("true")
    psip.process_input("/1,2,add")
    psip.process_input("if")
    assert psip.op_stack[-1] == 3
    
    psip.op_stack.clear()
    psip.process_input("false")
    psip.process_input("/1,2,add")
    psip.process_input("if")
    assert len(psip.op_stack) == 0

def run_all_tests():
    test_add_operation()
    test_lookup_operation()
    test_exch_operation()
    test_pop_operation()
    test_copy_operation()
    test_dup_operation()
    test_clear_operation()
    test_count_operation()
    test_div_operation()
    test_sub_operation()
    test_idiv_operation()
    test_mul_operation()
    test_abs_operation()
    test_neg_operation()
    test_ceiling_operation()
    test_floor_operation()
    test_round_operation()
    test_sqrt_operation()
    test_dict_operation()
    test_length_operation()
    test_maxlength_operation()
    test_begin_and_end_operations()
    test_def_operation()
    test_get_operation()
    test_getinterval_operation()
    test_putinterval_operation()
    test_eq_operation()
    test_ne_operation()
    test_ge_operation()
    test_gt_operation()
    test_le_operation()
    test_lt_operation()
    test_and_operation()
    test_not_operation()
    test_or_operation()
    test_if_operation()

run_all_tests()