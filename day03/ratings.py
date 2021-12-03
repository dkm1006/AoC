import pandas as pd
INPUT_FILE = 'input.txt'


def calculate_power_consumption(input_file=INPUT_FILE): 
    df = read_binary_file(input_file)
    gamma = []
    epsilon = []
    for col in df.columns:
        most_significant = int(df[col].mode().max())
        gamma.append(most_significant)
        epsilon.append(1 - most_significant)
    
    return binary_seq2int(gamma) * binary_seq2int(epsilon)

def calculate_life_support_rating(input_file=INPUT_FILE): 
    df = read_binary_file(input_file)
    generator_rating = calculate_rating(df, most_significant)
    scrubber_rating = calculate_rating(df, lambda s: 1 - most_significant(s))
    return generator_rating * scrubber_rating

def read_binary_file(input_file):
    num_cols = get_line_length(input_file)
    return pd.read_fwf(input_file,
                       widths=[1 for _ in range(num_cols)],
                       names=range(num_cols))

def calculate_rating(df, fn):
    df_temp = df.copy()
    for col in df.columns:
        bit_criteria = fn(df_temp[col])
        df_temp = df_temp[df_temp[col] == bit_criteria]
        if len(df_temp) == 1:
            result = binary_seq2int(df_temp.iloc[0])
            break

    return result

def most_significant(series):
    return int(series.mode().max())

def binary_seq2int(input_seq):
    result = 0
    for index, value in enumerate(reversed(input_seq)):
        result += int(value) * 2 ** index
    
    return result

def get_line_length(input_file):
    with open(input_file, 'r') as f:
        # Get len of 1st line (subtract 1 for newline char)
        return len(next(f)) - 1

if __name__ == '__main__':
    print(f"Power consumption: {calculate_power_consumption()}")
    print(f"Life support rating: {calculate_life_support_rating()}")