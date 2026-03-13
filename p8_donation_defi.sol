// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
contract Donation {
 uint public total;
 function donate() public payable {
 total += msg.value;
 }
 function getBalance() public view returns(uint) {
 return address(this).balance;
 }
}

#copy the address paste in "at address" click at address -> then deploy the balance will be updated 
#Value add 5 -> press donate 
#in console chcek output open it and check value should come someting (5000000000000 wei)
