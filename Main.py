from RiscVDecoder import decode_instructions_from_file

def main():

    file_path = "instructions.txt"
    decode_instructions_from_file(file_path)

if __name__ == "__main__":
    main()