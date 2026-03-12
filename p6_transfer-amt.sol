//SPDX-License-Identifier: MIT
pragma solidity ^0.8.31;


contract tytoken{
    string public name = "tyToken";
    string public symbol = "TYT";
    uint256 public totalSupply;
    mapping (address => uint256) public balanceOf;


     constructor(uint256 initialSupply ){
         totalSupply = initialSupply ;
         balanceOf[msg.sender] = initialSupply;
     }
    
function transfer(address toWhom , uint256 value) public returns (bool success){
    require(balanceOf[msg.sender] >= value, "Insufficient tokens ");
balanceOf[msg.sender] -= value;
balanceOf[toWhom] += value;
return true;
}
}

#Compile > add initial value in deploy > check name, symbol, total supply 
#Should be according to code
#Now in transfer > to whom : acc2 add > add amt to send
#Balance > acc 1 add> transact 
#Check total supply amt should be deducted 
