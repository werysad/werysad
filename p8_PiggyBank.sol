// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract PiggyBank {

    address public owner;

    constructor() {
        owner = msg.sender;
    }

    // Deposit ETH
    function deposit() public payable {}

    // Withdraw specific amount
    function withdraw(uint amount) public {

        require(msg.sender == owner, "Only owner can withdraw");
        require(amount <= address(this).balance, "Not enough balance");

        (bool success, ) = payable(owner).call{value: amount}("");
        require(success, "Transfer failed");
    }

    // Check contract balance
    function getBalance() public view returns(uint) {
        return address(this).balance;
    }
}

#1st deploy 
#in value 100000 > deposit 
#chcek balance 
#withdraw
#balance
