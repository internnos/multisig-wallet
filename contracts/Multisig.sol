// SPDX-License-Identifier: MIT
pragma solidity ^0.7.6;

contract MultiSigWallet {

    mapping(address => uint) public owners;

    // Init constructor
    constructor (address[] _owners, uint _num_validators) {
        require(_num_validators > 0, 'number of validators must be greater than 0');
        require(_num_validators <= len(_owners));
        (for uint i = 0; i < len(_owners); i++) {
            owners[i] = _owners;
        }
    }
    
    // function submitTransaction() {};

    // function confirmTransaction() {};

    // function executeTransaction() {};

    // function revertTransaction() {};
}