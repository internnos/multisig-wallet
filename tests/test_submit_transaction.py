from brownie import accounts, MultiSigWallet
from brownie.exceptions import VirtualMachineError
import pytest

def test_trx_to_one_of_owner_1():
    address_smart_contract = accounts[0]
    address_eoa_owners = accounts[1:3]
    trx_to = accounts[1]
    trx_amount = "1000 wei"

    multisig_wallet = MultiSigWallet.deploy(address_eoa_owners, 2, {'from': address_smart_contract})

    with pytest.raises(VirtualMachineError) as excinfo:
        multisig_wallet.submitTransaction(trx_to, trx_amount)    
    assert excinfo.value.revert_msg=="cannot send ether to one of the multisig owner"

def test_trx_to_one_of_owner_2():
    address_smart_contract = accounts[0]
    address_eoa_owners = accounts[1:3]
    trx_to = accounts[2]
    trx_amount = "1000 wei"

    multisig_wallet = MultiSigWallet.deploy(address_eoa_owners, 2, {'from': address_smart_contract})

    with pytest.raises(VirtualMachineError) as excinfo:
        multisig_wallet.submitTransaction(trx_to, trx_amount)   
    assert excinfo.value.revert_msg=="cannot send ether to one of the multisig owner"

def test_trx_to_other_account_1():
    address_smart_contract = accounts[0]
    address_eoa_owners = accounts[1:3]
    trx_to = accounts[5]
    trx_amount = "1000 wei"

    multisig_wallet = MultiSigWallet.deploy(address_eoa_owners, 2, {'from': address_smart_contract})
    multisig_wallet.submitTransaction(trx_to, trx_amount)


def test_trx_to_other_account_2():
    address_smart_contract = accounts[0]
    address_eoa_owners = accounts[1:3]
    trx_to = accounts[6]
    trx_amount = "1000 wei"

    multisig_wallet = MultiSigWallet.deploy(address_eoa_owners, 2, {'from': address_smart_contract})
    multisig_wallet.submitTransaction(trx_to, trx_amount)    