// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PiggyBank {

    address public owner;
    mapping(address => uint256) public balances;

    event Deposited(address indexed from, uint256 amount);
    event Withdrawn(address indexed to, uint256 amount);

    constructor() {
        owner = msg.sender;
    }

    function deposit() public payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        require(
            balances[msg.sender] + msg.value <= 100 ether,
            "Total balance cannot exceed 100 ether"
        );

        balances[msg.sender] += msg.value;
        emit Deposited(msg.sender, msg.value);
    }

    function withdraw(uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;

        (bool success, ) = payable(msg.sender).call{value: amount}("");
        require(success, "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    function getDonationBalance() public view returns (uint256) {
        return address(this).balance;
    }
}
