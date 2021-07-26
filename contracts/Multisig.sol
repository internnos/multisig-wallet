// SPDX-License-Identifier: MIT
pragma solidity ^0.7.6;

contract MultiSigWallet{

    mapping(address => uint) public owners;
    uint public num_validators;

    // Init constructor
    constructor(address[] memory _owners, uint _num_validators) {
        require(_num_validators > 0, 'number of validators must be greater than 0');
        require(_num_validators <= _owners.length);
        for (uint i = 0; i < _owners.length; i++) {
            address _owner = _owners[i];
            owners[_owner] = i;
            num_validators = i;
        }
        
    }
    
    // function submitTransaction() {};

    // function confirmTransaction() {};

    // function executeTransaction() {};

    // function revertTransaction() {};
}