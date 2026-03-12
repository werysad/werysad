	// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

contract Donation {
    address public owner;

    mapping(address => uint) public balances;

    event Donated(address indexed from, uint256 amount);

    constructor() {
        owner = msg.sender;
    }

    function donate() public payable {
        require(msg.value > 0, "Donation amount must be greater than zero");

        balances[msg.sender] += msg.value;
        emit Donated(msg.sender, msg.value);
    }

    function getDonationBalance() public view returns (uint256) {
        return address(this).balance;
    }
}
