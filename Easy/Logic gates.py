import sys
import math

n = int(input())
m = int(input())
signal_list_input = {}
logic_gate_list = {}

for i in range(n):
    input_name, input_signal = input().split()
    input_signal = input_signal.replace("-", "1").replace("_", "0")
    signal_list_input[input_name] = input_signal



for i in range(m):
    output_name, _type, input_name_1, input_name_2 = input().split()
    logic_gate_list[i] = {"output_name": output_name, "_type": _type,  "input_name_1": input_name_1,
                          "input_name_2": input_name_2, "result": None}


def logic_fct(signals_list, logic_gate):
    first_signal = signals_list[logic_gate["input_name_1"]]
    second_signal = signals_list[logic_gate["input_name_2"]]
    result = ""

    if logic_gate["_type"] == "AND":
        for i in range(len(first_signal)):
            result += str(int(first_signal[i]) and int(second_signal[i]))

    if logic_gate["_type"] == "OR":
        for i in range(len(first_signal)):
            result += str(int(first_signal[i]) or int(second_signal[i]))

    if logic_gate["_type"] == "XOR":
        for i in range(len(first_signal)):
            result += str(int(first_signal[i]) ^ int(second_signal[i]))

    if logic_gate["_type"] == "NAND":
        for i in range(len(first_signal)):
            result += str(int(not(int(first_signal[i]) and int(second_signal[i]))))

    if logic_gate["_type"] == "NOR":
        for i in range(len(first_signal)):
            result += str(int(not(int(first_signal[i]) or int(second_signal[i]))))

    if logic_gate["_type"] == "NXOR":
        for i in range(len(first_signal)):
            result += str(int(not(int(first_signal[i]) ^ int(second_signal[i]))))

    logic_gate["result"] = result.replace("1", "-").replace("0", "_")
    return logic_gate


for i in range(m):
    logic_gate_list[i] = logic_fct(signal_list_input, logic_gate_list[i])
    print(logic_gate_list[i]["output_name"], logic_gate_list[i]["result"])