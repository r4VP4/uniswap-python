from pprint import pprint
from uniswap import Uniswap
from timeit import default_timer as timer
address = "0xdf3e18d64bc6a983f673ab319ccae4f1a57c7097" # hardhat test-account!
private_key = "0xc526ee95bf44d8fc405a158bb884d9d1238d99f0612e9f33d006bb0789009aaa"  # hardhat test-account!
version = 3
provider = "http://localhost:8547"    # mainnet-fork hardhat
uniswap_build = Uniswap(
    address=address,
    private_key=private_key,
    version=version,
    provider=provider,
    build_only=True
)

uniswap_send = Uniswap(
    address=address,
    private_key=private_key,
    version=version,
    provider=provider,
    build_only=False
)

# Some token addresses
eth = "0x0000000000000000000000000000000000000000"
bat = "0x0D8775F648430679A709E98d2b0Cb6250d2887EF"
dai = "0x6B175474E89094C44Da98b954EedeAC495271d0F"

# print(uniswap.get_eth_balance())

txdata= uniswap_build.make_trade(eth, dai, 1*10**18)
pprint(txdata)
uniswap_send.make_trade(eth, dai, 1*10**18)

uniswap_send.approve(dai, max_approval=100*10**18)

txdata= uniswap_build.make_trade(dai, eth, 100*10**18)
pprint(txdata)
