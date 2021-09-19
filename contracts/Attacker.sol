pragma solidity 0.4.24;

contract Attacker{
    address public owner;
    address public target;

    constructor (address _target) public {
        target = _target;
        owner = msg.sender;
    }

    // Needed to receive transfers
    function () payable {}

    function exploit() payable {
    }

    // We shouldn't need this, but if we screw up we'll want our money back
    function gimme() external {
        owner.transfer(address(this).balance);
    }

    function boom() external {
        selfdestruct(owner);
    }
}
