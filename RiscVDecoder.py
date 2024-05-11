def decode_riscv_instruction(instruction):

    opcode = int(instruction[25:], 2)
    rd = int(instruction[20:25], 2)
    funct3 = int(instruction[17:20], 2)
    rs1 = int(instruction[12:17], 2)
    rs2 = int(instruction[7:12], 2)
    funct7 = int(instruction[:7], 2)

    if opcode == 0b0110111:
        return f"LUI x{rd}, {int(instruction[12:], 2)}"
    elif opcode == 0b0010011:
        imm = int(instruction[0] * (32 - len(instruction)) + instruction, 2) if instruction[0] == '1' else int(instruction, 2)
        if funct3 == 0b000:
            return f"ADDI x{rd}, x{rs1}, {imm}"
        elif funct3 == 0b100:
            return f"XORI x{rd}, x{rs1}, {imm}"
    elif opcode == 0b0000011:
        imm = int(instruction[0] * (32 - len(instruction)) + instruction, 2) if instruction[0] == '1' else int(instruction, 2)
        if funct3 == 0b000:
            return f"LB x{rd}, {imm}(x{rs1})"
        elif funct3 == 0b001:
            return f"LH x{rd}, {imm}(x{rs1})"
    elif opcode == 0b1100011:
        imm = int(instruction[0] + instruction[24:31] + instruction[1:7] + instruction[20:24] + '0', 2)
        imm = imm if imm < 2048 else imm - 4096
        if funct3 == 0b000 and funct7 == 0b0000000:
            return f"BEQ x{rs1}, x{rs2}, {imm}"
    elif opcode == 0b1100111:
        if funct3 == 0b000 and funct7 == 0b0000000:
            return f"JALR x{rd}, x{rs1}, {int(instruction[20:], 2)}"
    elif opcode == 0b0110011:
        return f"ADD x{rd}, x{rs1}, x{rs2}"
    elif opcode == 0b0100011:
        return f"SW x{rs2}, {int(instruction[0:7], 2)}(x{rs1})"
    else:
        print(f"Unbekannter Befehl: {instruction}")
    return None

def decode_instructions_from_file(file_path):
    with open(file_path, 'r') as file:
        instructions = [line for line in file]

    decoded_instructions = []

    for instruction in instructions:
        print(f"'{instruction}', Länge: {len(instruction)}")
        decoded_instruction = decode_riscv_instruction(instruction)
        print(decoded_instruction)
        decoded_instructions.append(decoded_instruction)

    return decoded_instructions

# BNE und LW