# Enter your code here. Read input from STDIN. Print output to STDOUT

# MSFT|400
# IBM|1000
# AAPL|500
# AAPL|600
# NFLX|1000
# AMZN|700
# GOGL|300


# void execute_trade(string ticker, unsigned int volume)
class Trade:
    def __init__(self):
        self.hash_map = {}
    
    def execute_trade(self, ticker, volume):
        if ticker in self.hash_map:
            self.hash_map[ticker] += volume
        else:
            self.hash_map[ticker] = volume

    def print_top_n_traded(self, n):
        sorted_hash_map = sorted(self.hash_map.items(), key=lambda x:x[1], reverse=True)

        sorted_hash_map = dict(sorted_hash_map)

        count = 0
        for key, value in sorted_hash_map.items():
            if count < n:
                print(key + "|" + str(value))
                count +=  1
    


my_var = Trade()

my_var.execute_trade("MSFT", 400)
my_var.execute_trade("AMZN", 700)
my_var.execute_trade("IBM", 500)
my_var.execute_trade("AAPL", 300)
my_var.execute_trade("MSFT", 400)
my_var.execute_trade("IBM", 400)
my_var.execute_trade("AAPL", 300)
my_var.execute_trade("NFLX", 200)

print(my_var.print_top_n_traded(5))