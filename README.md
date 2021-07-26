### Takeaways

1. There is no direct or easy way to get the key of a mapping in solidity. My first idea of removing the duplicate of owners is to store the owner addresses in a mapping.

```
mapping(address => uint) public owners;
constructor(address[] memory _owners, uint _numConfirmationsRequired) {
    for (uint i = 0; i < _owners.length; i++) {
        address _owner = _owners[i];
        owners[_owner] = i;
    }    
}
```
Later on I hope that I can retrieve the owners' keys', but I found this [gem](https://stackoverflow.com/questions/65529667/get-keys-of-solidity-mapping) which states that due to resource efficiency, the Solidity/EVM doesn't store iterable keys. There is a workaround, which is to emit events that can be listened from the clients side(geth, parity, etc), but as I've mentioned before it cannot be done on the contract itself so I'm not taking that path.




2. `list` must be stored on `memory` or on the blockchain a.k.a `storage`.

3. `mapping` doesn't have length. Unlike python where we can directly iterate on `dict`, solidity behaves differently.