from brownie import accounts, MultiSigWallet
from brownie.exceptions import VirtualMachineError
import pytest

def test_zero_owner():
    address_smart_contract=accounts[0]
    address_eoa=[]

    with pytest.raises(VirtualMachineError) as excinfo:
        MultiSigWallet.deploy(address_eoa, 0, {'from': address_smart_contract})
    assert excinfo.value.revert_msg=="number of owners must be greater than 0"

def test_zero_confirmations():
    address_smart_contract=accounts[0]
    address_eoa=accounts[1:3]

    with pytest.raises(VirtualMachineError) as excinfo:
        MultiSigWallet.deploy(address_eoa, 0, {'from': address_smart_contract})
    assert excinfo.value.revert_msg=="number of confirmations must be greater than 0"

def test_duplicate_owners():
    address_smart_contract=accounts[0]
    address_eoa=[accounts[1]]+[accounts[1]]+[accounts[1]]
    with pytest.raises(VirtualMachineError) as excinfo:
        MultiSigWallet.deploy(address_eoa, 2, {'from': address_smart_contract})
    assert excinfo.value.revert_msg=="duplicate owner address detected"


def test_confirmations_exceed_number_of_owners():
    address_smart_contract=accounts[0]
    address_eoa=accounts[1:3]
    with pytest.raises(VirtualMachineError) as excinfo:
        MultiSigWallet.deploy(address_eoa, 4, {'from': address_smart_contract})
    assert excinfo.value.revert_msg=="number of confirmations exceed available owners"


def test_correctness_1():
    address_smart_contract=accounts[0]
    address_eoa=accounts[1:3]

    multisig_wallet=MultiSigWallet.deploy(address_eoa, 1, {'from': address_smart_contract})
    
def test_correctness_2():
    address_smart_contract=accounts[0]
    address_eoa=accounts[1:3]

    multisig_wallet=MultiSigWallet.deploy(address_eoa, 2, {'from': address_smart_contract})