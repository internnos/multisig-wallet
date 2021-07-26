// SPDX-License-Identifier: MIT
pragma solidity ^0.7.6;

contract MultiSigWallet{
    address[] public owners;
    // _numConfirmationsRequired is the number of owners except the one who submit the transaction
    uint public numConfirmationsRequired;
    // mapping if an adress is a valid owner(not a duplicate)
    mapping(address => bool) isOwner;

    // Init constructor
    constructor(address[] memory _owners, uint _numConfirmationsRequired) {
        require(_numConfirmationsRequired > 0, 'number of validators must be greater than 0');
        require(_numConfirmationsRequired <= _owners.length);
        for (uint i = 0; i < _owners.length; i++) {
            address _owner = _owners[i];
            require(!isOwner[_owner]);
            isOwner[_owner] = True
        }
       
        
    }
    
    // function submitTransaction() {};

    // function confirmTransaction() {};

    // function executeTransaction() {};

    // function revertTransaction() {};
}