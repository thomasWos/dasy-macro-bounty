import dasy
from boa.vyper.contract import VyperContract

def compile(filename: str) -> VyperContract:
    with open(filename) as f:
        ast = dasy.compile(f.read())
        return VyperContract(ast)

contract = compile("block_number.dasy")
print(contract.blockNumber())
