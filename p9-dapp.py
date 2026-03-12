# AIM: DAPP Application without Front end
# Download node js 16.20.2
# Click menu > network > network name : Localhost 8545
# RPC URL > copypaste from ganache add 
# Chain id 1337 > currency symbol > ETH

# Click on account > add wallet > import wallet > paste private key from ganache> import



# Create a folder bkc

npm init -y
npm install -g truffle
npm install truffle lite-server
npx truffle init

# In contracts folder 
# Create a file add.sol
# Code 
//SPDX-License-Identifier:MIT
pragma solidity ^0.8.0;
contract Add {
   function add (uint a,uint b) public pure returns (uint)
{
   return a + b;
}
}

#Migration folder 
#Create file 1_deploy.js
const Add = artifacts.require("Add");


module.exports=function (deployer){
deployer.deploy(Add);
};


# Now change in truffle-config.js
# version: "0.8.19"
# port: 7545

# after file  check 
# npx truffle compile --all
# npx truffle migrate --reset
