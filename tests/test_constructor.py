from brownie import accounts, MultiSigWallet
# from brownie.network.contract.ContractContainer import MultiSigWallet
from brownie.exceptions import VirtualMachineError
import pytest

def test_constructor():
    address_smart_contract=accounts[0]
    address_eoa=accounts[1:3]

    with pytest.raises(VirtualMachineError):
        MultiSigWallet.deploy(address_eoa, 0, {'from': address_smart_contract})