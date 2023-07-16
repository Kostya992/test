import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='concatenation of log a and log b')
parser.add_argument('log_a', type=str, help='Input log_a')
parser.add_argument('log_b', type=str, help='Input log_b')
parser.add_argument('-o', type=str, help='Output log')
args = parser.parse_args()
# Input
df_a = pd.read_json(args.log_a, lines = True)
df_b = pd.read_json(args.log_b, lines = True)
# Joint
df = pd.concat([df_a,df_b]).sort_values('timestamp').reset_index(drop=True)
# Output
df.to_json(args.o, orient = 'records',  lines = True)