# Download node js 16.20.2
# Click menu > network > network name : Localhost 8545
# RPC URL > copypaste from ganache add 
# Chain id 1337 > currency symbol > ETH

# Click on account > add wallet > import wallet > paste private key from ganache> impo



# Create a folder bkc

# npm init -y
# npm install -g truffle
# npm install truffle lite-server
# npx truffle init



# all codes
# File.sol in contracts folder
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract Add {
    uint public lastResult;

    function add(uint a, uint b) public {
        lastResult = a + b;
    }
}

# 1_doploy.js in migration folder 
const Add = artifacts.require("Add");


module.exports=function (deployer){
deployer.deploy(Add);
};

npx truffle compile --all
npx truffle migrate --reset



Copy == Contract address from console 

index.html
<!DOCTYPE html>
<html>
<head>
  <title>Add Contract UI</title>
  <script src="https://cdn.jsdelivr.net/npm/web3@1.10.0/dist/web3.min.js"></script>
</head>
<body>
  <h2>Add Two Numbers (Gas Required)</h2>


  <input id="a" type="number" placeholder="A" />
  <input id="b" type="number" placeholder="B" />
  <button onclick="addNumbers()">Add</button>


  <h3 id="result">Result:</h3>


  <script>
    let web3;
    let contract;
    let account;


    const abi = [
      {
        "inputs": [
          { "internalType": "uint256", "name": "a", "type": "uint256" },
          { "internalType": "uint256", "name": "b", "type": "uint256" }
        ],
        "name": "add",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
      },
      {
        "inputs": [],
        "name": "lastResult",
        "outputs": [
          { "internalType": "uint256", "name": "", "type": "uint256" }
        ],
        "stateMutability": "view",
        "type": "function"
      }
    ];


    const contractAddress = "Paste here";


    async function load() {
      if (window.ethereum) {
        web3 = new Web3(window.ethereum);


        const accounts = await window.ethereum.request({
          method: "eth_requestAccounts"
        });


        account = accounts[0];
        contract = new web3.eth.Contract(abi, contractAddress);
      } else {
        alert("Please install MetaMask");
      }
    }


    async function addNumbers() {
      const a = document.getElementById("a").value;
      const b = document.getElementById("b").value;


      await contract.methods.add(a, b).send({
        from: account
      });


      const result = await contract.methods.lastResult().call();
      document.getElementById("result").innerText = "Result: " + result;
    }


    load();
  </script>
</body>
</html>
