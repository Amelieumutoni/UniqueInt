import os

class UniqueInt:
    def __init__(self):
        self.min_val = -1023
        self.max_val = 1023
        self.range_size = self.max_val - self.min_val + 1
        self.seen = [False] * self.range_size
    
    def process_file(self, input_file_path, output_file_path):
        with open(input_file_path, 'r') as infile:
            for line in infile:
                self.read_next_item_from_file(line)
        
        unique_integers = [i + self.min_val for i, seen in enumerate(self.seen) if seen]
        unique_integers.sort()

        with open(output_file_path, 'w') as outfile:
            for num in unique_integers:
                outfile.write(f"{num}\n")

    def read_next_item_from_file(self, line):
        line = line.strip()
        if not line or ' ' in line:
            return
        
        try:
            num = int(line)
            if self.min_val <= num <= self.max_val:
                self.seen[num - self.min_val] = True
        except ValueError:
            return

def main():
    input_dir = '/dsa/hw01/sample_inputs/'
    output_dir = '/dsa/hw01/sample_results/'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    files = os.listdir(input_dir)
    for file in files:
        if file.endswith('.txt'):
            input_file_path = os.path.join(input_dir, file)
            output_file_path = os.path.join(output_dir, file.replace('.txt', '_results.txt'))
            unique_int = UniqueInt()
            unique_int.process_file(input_file_path, output_file_path)

if __name__ == "__main__":
    main()
