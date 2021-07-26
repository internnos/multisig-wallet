// SPDX-License-Identifier: MIT
pragma solidity ^0.7.6;

contract MultiSigWallet{

    // remember that we cannot directly
    mapping(address => uint) public owners;
    // _numConfirmationsRequired is the number of owners except the one who submit the transaction
    uint public numConfirmationsRequired;

    // Init constructor
    constructor(address[] memory _owners, uint _numConfirmationsRequired) {
        require(_numConfirmationsRequired > 0, 'number of validators must be greater than 0');
        require(_numConfirmationsRequired <= _owners.length);
        for (uint i = 0; i < _owners.length; i++) {
            address _owner = _owners[i];
            owners[_owner] = i;
        }
        numConfirmationsRequired = owners.length;
        
    }
    
    // function submitTransaction() {};

    // function confirmTransaction() {};

    // function executeTransaction() {};

    // function revertTransaction() {};
}