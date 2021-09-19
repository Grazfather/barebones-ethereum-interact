pragma solidity 0.4.24;

contract Target{

    address public developer;

    constructor(address _ctfLauncher, address _player) public payable

    {
        developer = msg.sender;
    }

    function () external payable{
        // Anyone can add to the fund
    }
}
